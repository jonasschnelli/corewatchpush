#!/usr/bin/env python3
# Copyright (c) 2018 The CoreWatchPush developers
# Distributed under the MIT software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.

from config import *

import sys
import http.client
import urllib.parse

# telegram send message helper
class Notify_Telegram:
    def push(text="test"):
        conn = http.client.HTTPSConnection('api.telegram.org')
        params = urllib.parse.urlencode({'chat_id': Config.notify_telegram_chat_id, 'parse_mode': 'markdown', 'disable_web_page_preview': '1', 'text': text})
        conn.request('POST', '/bot'+Config.notify_telegram_key+'/sendMessage', params, {"Content-type": "application/x-www-form-urlencoded"})
        response = conn.getresponse()
        #print(response.read().decode())

# can be run directly with ./notify_telegram.py <message>
if __name__ == '__main__':
    if len(sys.argv) == 2:
        Notify_Telegram.push(sys.argv[1])