# hansible
eHanse's ansible configuration files.

## General Usage

1. Install ansible via `apt-get install ansible`.
2. Clone this repo and `cd` into the directory.
3. Save our vault-password into a `.vaultpw`-file (which is git-ignored): `echo <ourvaultpassword> > .vaultpw `
4. Now your hansible-repo is ready to run. First, perform a a dry run on our servers: ` ansible-playbook playbook.yml -i inventory -u YOURUSER -s -K --vault-password-file=.vaultpw --check `
5. Perform an actual run using the same command without `--check` command: `
ansible-playbook playbook.yml -i inventory -u YOURUSER -s -K --vault-password-file=.vaultpw `

## Usage of the vault files
* `ansible-vault create <filename>` creates a vault file with <filename> and asks to set a passwd.
* `ansible-vault edit <filename>` asks for the passwd and opens the vault with your default editor (nano or vi)
* `ansible-vault view <filename>` asks for the passwd to view the contents
* `makepasswd --method=sha-512` asks you to enter a passphrase and returns a SHA-512 hash of the passwd.

## Ansible best practices
* Normally, the _roles_ subfolder will contain subfolders where each subfolder is a _role_ consisting of _vars_, _tasks_, _handlers_ etc. This is a complicated folder structure. To make it easier, we have some plain playbooks in the _roles_ subfolder. This does not follow the ansible standard folder structure, but is easier to read, as everything for a role is in one file.
* _Roles_ which we cloned from external sources have their own subfolder in the _roles_ subfolder.
* _Vaults_: A best practice approach for this is to start with a `group\_vars` subdirectory named after the group. Inside of this subdirectory, create two files named `vars` and `vault`. Inside of the vars file, define all of the variables needed, including any sensitive ones. Next, copy all of the sensitive variables over to the vault file and prefix these variables with `vault\_`. You should adjust the variables in the vars file to point to the matching vault_ variables using jinja2 syntax, and ensure that the vault file is vault encrypted.

