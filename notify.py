#!/usr/bin/env python3
# Copyright (c) 2018 The CoreWatchPush developers
# Distributed under the MIT software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.

from config import *

from notify_telegram import *
from notify_email import *

import json
import subprocess
import sys
from datetime import datetime

class Bitcoin_CLI:
    def call(method, args=[]):
        cmdbase = [Config.bitcoin_cli]
        if len(Config.bitcoin_cli_args) > 0:
            cmdbase.append(Config.bitcoin_cli_args)
        if len(Config.bitcoin_wallet_name) > 0:
            cmdbase.append("-rpcwallet="+Config.bitcoin_wallet_name)
        cmd = cmdbase
        cmd.append(method)
        if len(args) > 0:
            cmd = cmd + args
        result = subprocess.run(cmd, stdout=subprocess.PIPE)
        return result.stdout.decode()
    
if __name__ == '__main__':
    if len(sys.argv) >= 2 and (sys.argv[1] == "rescan"):
        args = []
        if len(sys.argv) == 4:
            args.append(sys.argv[2])
            args.append(sys.argv[3])
        Bitcoin_CLI.call("rescanblockchain", args)
        
    if len(sys.argv) == 2 and (sys.argv[1] == "import" or sys.argv[1] == "importtest"):
        for xpub_array in Config.bip44_account_xpubs:
            xpub = xpub_array[0]
            script_array = Config.script_types
            label = "undefined"
            if len(xpub_array) >= 2:
                label = xpub_array[1]
            if len(xpub_array) == 3:
                script_array = xpub_array[2]
    
            for script_type in script_array:
                parsed_ext = json.loads(Bitcoin_CLI.call("getdescriptorinfo", [script_type.replace("()", "("+xpub+"/0/*)")]))
                parsed_int = json.loads(Bitcoin_CLI.call("getdescriptorinfo", [script_type.replace("()", "("+xpub+"/1/*)")]))
                if sys.argv[1] == "importtest":
                    print("XPUB TEXT, label: "+label+"\n")
                    print(script_type)
                    print(Bitcoin_CLI.call("deriveaddresses", [parsed_ext['descriptor'], "10"]))
                else:
                    parsed = json.loads(Bitcoin_CLI.call("importmulti", ['[{"desc": "'+parsed_ext['descriptor']+'", "range": '+str(Config.xpub_range)+', "watchonly": true, "internal": false, "timestamp": 0, "label": "'+label+'"}]', '{"rescan": false}']))
                    parsed = json.loads(Bitcoin_CLI.call("importmulti", ['[{"desc": "'+parsed_int['descriptor']+'", "range": '+str(Config.xpub_range)+', "watchonly": true, "internal": true, "timestamp": 0}]', '{"rescan": false}']))
                    
        
    if len(sys.argv) == 2 and len(sys.argv[1]) == 64:
        txid = sys.argv[1]
        parsed = json.loads(Bitcoin_CLI.call("gettransaction", [txid, "true"]))
        time = str(datetime.fromtimestamp(parsed['time']))
        text = "*new transaction*\n"
        text += "*time:* "+time+"\n"+"*confirmations:* "+str(parsed['confirmations'])+"\n"+"*txid:* "+parsed['txid']+"\n";
        
        if len(parsed['details']) > 0:
            for item in parsed['details']:
                label=""
                if item.get('label'):
                    label = item['label']+" / "
                if item['category'] == "send":
                    text += "\U0001F534"
                else:
                    text += "\U00002705"
                text += "*"+item['category']+"* amount: "+str(item['amount'])+" via: "+label+item['address']+"\n"

        parsed = json.loads(Bitcoin_CLI.call("getbalances"))
        text += "*New trusted balance:* "+str(parsed['watchonly']['trusted'])+"\n"
        text += "*New untrusted balance:* "+str(parsed['watchonly']['untrusted_pending'])+"\n"
        if (len(Config.blockexplorer) > 0):
            text += "[Blockexplorer]("+Config.blockexplorer+txid+")\n"
        Notify_Telegram.push(text)        if "telegram" in Config.notify_channels: 
            Notify_Telegram.push(text)
        if "email" in Config.notify_channels:
            Notify_SMTP.push(text)