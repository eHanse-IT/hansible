# hansible
eHanse's ansible configuration files.

## General Usage
Ansible is a command line program to configure servers. When starting ansible, 
you need to define _what_ you want to configure, and _where_ you want it to configure.
The _what_ is defined by the playbook. The _where_ is defined by the inventory file.
If you do not want to manage all servers, use the '-l _hostname_' parameter when starting ansible.

The playbooks ("play_odoo" et cetera) in turn call all the tasks 
that we find in the 'roles' subfolder. Before starting with ansible, 
you need to install it and write the vault password in a file that is 
accessible to ansible, but will not be synced to git. Here is how to do it.

## Installation 

1. Install ansible via `apt-get install ansible`.
2. git-clone this repo and `cd` into the directory.
3. Save our vault-password into a `.vaultpw`-file (which is git-ignored) by pasting it into that file or by 
`echo <ourvaultpassword> > .vaultpw `
4. Now your hansible-repo is ready to run. First, perform a a dry run on our servers using hte --check parameter: ` ansible-playbook playbook.yml -i inventory -u YOURUSER -b -K --vault-password-file=.vaultpw --check -l oaprod`
5. Perform an actual run using the same command without `--check` command: `
ansible-playbook playbook.yml -i inventory -u YOURUSER -b -K --vault-password-file=.vaultpw -l oaprod`

ALWAYS use the -l parameter to define the host! Otherwise, ALL hosts will be changed!


## Usage of vault files
Vault files help us to store passwords and private keys, that are not supposed to be seen in public, safely and encrypted. In this way, we can upload a vault to GitHub safely.
* `ansible-vault create <filename>` creates a vault file with <filename> and asks to set a passwd.
* `ansible-vault edit <filename>` asks for the passwd and opens the vault with your default editor (nano or vi)
* `ansible-vault view <filename>` asks for the passwd to view the contents
* `makepasswd --method=sha-512` asks you to enter a passphrase and returns a SHA-512 hash of the passwd.

## How this repo is organized
* general variables can be found in the file `vars`, which in turn references to the file `vault`.
* host variables can be found directly in the inventory.yml
* some more variables can be found in the playbooks, but these are not so important
 

