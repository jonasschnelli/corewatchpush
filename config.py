class Config:
    #always use a BIP44 account key
    #keys will be derived at <xpub>/0/* and <xpub>/1/* (internal)
    #if you have an ypub or zpub, use Electrums CLI to conert it to xpub ("convert_xkey(<ypub>, "standard")")
    bip44_account_xpubs=[["xpub6BYyMLt46C5p4tQ28bFykNX9HN849dbCnhKQTdCz7dBPBTvDANv66rExpGNZdYXShSemd38NDGo4iEigRjy23ycftPv4vchMKdfTG54LcoX", "My Old Wallet", ["pkh()"]],
                         ["xpub6AqZNvH9ujEmBj9QoKSw7U7jyqy3uPukpTcKDPhhUDE1v2tbHRgXfcKb5MKv2rGYh1Nv2cYyaHEY4zVZ7ACK2DYinTA7G61m2UeR69zdguv", "My New Wallet", ["wpkh()"]],
                         ["xpub6A9rFqRrf5tpnKRLCGdEtUnPJPnjZ4XG48ugxbBtK3mYCdNuNUK8vX4NjGDnfctGkcrJCd2EUDi3chJrGuzKiNT8FWywWUmfijymrgKutSV", "My Other Wallet"]
                        ]

    # the range to derive addresses up to (for each script_type)
    xpub_range=1000

    # default script types to derive if no script type is given in bip44_account_xpubs
    script_types = ["pkh()", "wpkh()", "sh(wpkh())"]

    # bitcoin cli location
    # requires Bitcoin Core 0.18 (or newer)
    bitcoin_cli="/btc/apps/bitcoin-0.18.0/bin/bitcoin-cli"

    # bitcoin
    bitcoin_cli_args="--datadir=/somewhere/bitcoin"

    # name of the wallet
    # WARNING: CoreWatchPush is not really multiwallet capable
    bitcoin_wallet_name="" #use empty string for default wallet

    # optional blockexplorer link
    blockexplorer = "https://bitcointools.jonasschnelli.ch/explorer/index.php?search="

    # push channels (only telegram for now)
    notify_channels=["telegram"]
    #notify_channels=["telegram", "email"] #enable in case you want email and smtp

    # telegram KEY and chat-ID
    # google the internet how to create a bot, get the key as well as a chat-id
    notify_telegram_key="###"
    notify_telegram_chat_id="###"

    # email notification SMTP
    notify_email_receiver = "You <you@yourdomain.com>"
    notify_email_sender = "autosend <autosend@something.com>"
    notify_email_smtphost = "your.smtp.host"
    notify_email_smtpuser = "your_smtp_username"
    notify_email_smtppass = "your_smtp_password"
