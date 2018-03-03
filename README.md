# hansible
eHanse's ansible configuration files.

## General Usage
Our ansible configurations are supposed to be run via the playbooks "play_apache", "play_odoo" et cetera. They in turn call all the tasks that we find in the 'roles' subfolder. To start with ansible:

1. Install ansible via `apt-get install ansible`.
2. git-clone this repo and `cd` into the directory.
3. Save our vault-password into a `.vaultpw`-file (which is git-ignored): `echo <ourvaultpassword> > .vaultpw `
4. Now your hansible-repo is ready to run. First, perform a a dry run on our servers: ` ansible-playbook playbook.yml -i inventory -u YOURUSER -b -K --vault-password-file=.vaultpw --check `
5. Perform an actual run using the same command without `--check` command: `
ansible-playbook playbook.yml -i inventory -u YOURUSER -s -K --vault-password-file=.vaultpw `

If you intend to run ansible against a single server, look at the name of the server in the inventory.yml and add the parameter `-l SERVERNAME` at the end of the ansible-playbook command.

## Usage of the vault files
* `ansible-vault create <filename>` creates a vault file with <filename> and asks to set a passwd.
* `ansible-vault edit <filename>` asks for the passwd and opens the vault with your default editor (nano or vi)
* `ansible-vault view <filename>` asks for the passwd to view the contents
* `makepasswd --method=sha-512` asks you to enter a passphrase and returns a SHA-512 hash of the passwd.

## How this repo is organized
* host variables can be found directly in the inventory.yml
* general variables can be found in the file `vars`, which in turn references to the file `vault`.
* some more variables can be found in the playbooks, but these are not so important
 

