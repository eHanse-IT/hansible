# hansible
eHanse's ansible configuration files.

## General Usage
Ansible is a command line program to configure servers. Ansible only needs a local installation and connects to servers via SSH. When starting ansible, you need to define _what_ you want to configure, and _where_ you want it to configure.
The _what_ is defined by the **playbook**. The _where_ is defined by the **inventory** file. Secret passwords that are not supposed to be accessible the the public are stored in the **vault** file.
The playbooks ("play_odoo" et cetera) in turn call all the tasks  that we find in the 'roles' subfolder. Before starting with ansible, you need to install it and write the vault password in a file that is accessible to ansible, but will not be synced to git. Here is how to do it.

## Installation 

1. Install ansible via `apt-get install ansible`, after adding PPA:
https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html#latest-releases-via-apt-ubuntu
2. git-clone this repository.
3. This repository contains submodules. Run `git submodule update --init` to clone them too.
4. `cd` into the cloned directory `hansible`.
5. Get our vault password from Keepass and save to a new a `.vaultpw`-file (which is git-ignored by our above gitignore file) by pasting it into that file or by 
`echo <ourvaultpassword> > .vaultpw `
6. Now your hansible-repo is ready to run. First, perform a a dry run on our servers using hte --check parameter: ` ansible-playbook playbook.yml -i inventory.yml -u YOURUSER -b -K --vault-password-file=.vaultpw --check -l oaprod`
7. Perform an actual run using the same command without `--check` command: `
ansible-playbook playbook.yml -i inventory.yml -u YOURUSER -b -K --vault-password-file=.vaultpw -l YOUR-HOSTNAME`

Obviously, you need to replace YOURUSER with your linux admin username.
ALWAYS use the -l parameter to define the host! Otherwise, ALL hosts will be changed!


## Usage of vault files
Vault files help us to store passwords and private keys, that are not supposed to be seen in public, safely and encrypted. In this way, we can upload a vault to GitHub safely.
* `ansible-vault create <filename>` creates a vault file with <filename> and asks to set a passwd.
* `ansible-vault edit <filename>` asks for the passwd and opens the vault
with your default editor (nano or vi)
* `ansible-vault view <filename>` asks for the passwd to view the contents
* `makepasswd --method=sha-512` asks you to enter a passphrase and returns a SHA-512 hash of the passwd.

## How this repo is organized
* general variables can be found in the file `vars`, which in turn references to the file `vault`.
* host variables can be found directly in the inventory.yml
* some more variables can be found in the playbooks, but these are not so important
 
## How to initially configure a server in 5 steps
- go to the website of the VServer service provider, install a fresh Ubuntu and _copy_ the new root password to your clipboard
- Open a Terminal and run: 'ssh-keygen -f "/home/joerg/.ssh/known_hosts" -
R 123.123.123.123' to remove any old SSH keys connected to that IP
- In the same terminal, try to login once to get the new SSH key: ssh root@123.123.123.223.
You can cancel the login after you have accepted the new SSH Key.
- Run the Bootstrapping playbook play_00_bootstrap.yml first. As this
is the first time Ansible connects to a server, you need to run as _root_,
you need to connect to port 22 and you need to pass the SSH password (which
is the same as the root password in your clipboard). Observe that you
need to replace the _ehtes_ variable with the name of your server.
ansible-playbook play_00_bootstrap.yml -i inventory.yml -u root -b -K --vault-password-file=.vaultpw -l ehtest --ask-pass
- Run all other playbooks to your liking:
ansible-playbook play_01_essentials.yml -i inventory.yml -u joerg -b -K --vault-password-file=.vaultpw -l ehtest
