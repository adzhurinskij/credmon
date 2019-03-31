# -*- coding: utf-8 -*-

from ftplib import FTP


class CheckFtp():

    def __init__(self, hostname, username, password):
        self.hostname = hostname
        self.username = username
        self.password = password

    def check(self):
        with FTP(host=self.hostname, user=self.username, passwd=self.password) as ftp:
            ftp.pwd()

        return True
