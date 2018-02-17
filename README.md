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

