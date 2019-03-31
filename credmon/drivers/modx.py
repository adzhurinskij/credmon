# -*- coding: utf-8 -*-

import requests


class CheckModx():

    def __init__(self, url, username, password):
        self.url = url
        self.username = username
        self.password = password

        self.useragent = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 OPR/57.0.3098.116'

    def check(self):
        data = {
            'login': 1,
            'rememberme': 1,
            'username': self.username,
            'password': self.password,
        }

        resp = requests.post(self.url, data=data)

        if resp.text.find('modx-login-password') == -1:
            return True
        else:
            return False
