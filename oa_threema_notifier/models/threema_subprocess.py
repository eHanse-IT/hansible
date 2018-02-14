# -*- coding: utf-8 -*-
# Copyright 2018 eHanse IT & Consulting UG
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from openerp import models, api, fields
from subprocess import Popen, PIPE, STDOUT
import logging

_logger = logging.getLogger(__name__)

class ThreemaSubprocess(models.Model):


#     da ThreemaSubprocess von model.Model erbt, müssen wir erstmal den Constructor aufrufen?
#     sowas wie def __init__(self, ...) ?

    _name='threema_subprocess'

    @api.multi
    def write_threema_message(self):
        message = "Hallo Joerg. Diese Nachr..."
        receiver = "77W2BCK2"
        sender= "*OATRADE"
        api_key = "___"
        priv_path = "/opt/odoo/custom/addons/privkey.sec"
        #compile shell command; encode message as bystring
        commandstring = '/usr/local/bin/threema-gateway send_e2e '
        commandstring = commandstring + receiver + ' ' + sender + ' ' + api_key + ' ' + priv_path
        byte_msg = message.encode(encoding='utf-8')
        #send message out
        process = Popen(commandstring, stdout=PIPE, stdin=PIPE, stderr=STDOUT, shell=True)
        stdout, stderr = process.communicate(input=byte_msg)
        #stderr = process.communicate(input=byte_msg)[1]
        _logger.info('Writing Threema message log ....')
        _logger.info(stdout)
        _logger.info(stderr)
        return stdout

    @api.multi
    def write(self, vals):
	return

    @api.model
    def create(self,vals):
        return

