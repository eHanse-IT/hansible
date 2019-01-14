# Ansible Role: Odoo rules for fail2ban behind Apache proxy

### The Situation
You want to harden your Odoo system against brute-force attacks by blocking IPs for which several login attempts failed.
### The problem
You run Odoo behind ana Apache proxy, and failed login attempts will be logged by Odoo, but only the IP "127.0.0.1" 
is shown in the Odoo logs.
### The solution
Instead of parsing the Odoo logs, we will parse the Apache access logs. A failed Odoo login
will cause Odoo to re-send the login page, which Apache will log as a POST for /web/login.
Because Apache knows the true IP, fail2ban can now work as intended. 
---
## Requirements
 - You run Odoo behind an Apache SSL proxy (port 443).
 - each of your apache vhosts resides in a seperate file, such that you can pinpoint the Odoo vhost file.
 - You have installed fail2ban and it works, for example for sshd.
 ---
## What this role will do
For fail2ban to work, we need to make sure that fail2ban can access the 
specific log entries for requests towards the Odoo system. Therefore:
 - This role will modify your Apache vhost such that the path of the logfile is well-defined.
 - The same path will then be used to create a new jail for fail2ban.
 - A new filter will be created for fail2ban with a regular expression to match the ''POST /web/login'' pattern.
## Role Variables
 - apache_odoo_vhost_file: you point towards the file where your Odoo vhost is defined
 - apache_odoo_vhost_log_path: you define where the vhost will put its logs.
## Example Playbook
    ---
    - name: Install Odoo rules for fail2ban
      vars:
        apache_odoo_vhost_log_path: /var/log/apache2/odoo.log
        apache_odoo_vhost_file: /etc/apache2/sites-available/{{ domain }}.conf
      hosts: all
      roles:
        - ansible-odoo-rules-for-fail2ban

 ---
## License

GNU GENERAL PUBLIC LICENSE

## Author Information

This role was created in 2018 by [Jörg Schumacher](https://www.ehanse.de/).