CoreWatchPush
=====================================

What is CoreWatchPush?
----------------

Watch a bunch of xpubs via Bitcoin Core and get notifications on new transactions.

Currently supported is Telegram as push notification channel.

Setup
-------------------

* Make sure you have the right xpub(s) in your `config.py`
* **Make sure you use an empty wallet** (Multiwallet is currently not well suppored)
* Set the path to your Bitcoin-CLI as well as the optional datadir in `config.py`

* **Make sure your `bitcoin.conf` has set `-walletnotify=/path/to/notify.py`

Test your import
```
./notify.py importtest
```

Import your xpubs
```
./notify.py import
```

Rescan old blocks
```
./notify.py rescan
#OR#
./notify.py rescan <fromheight> <toheight>
```
