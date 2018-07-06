#!/bin/bash
echo 'ElevenBand_NFCKey Library Installer'
echo 'Dev v1.0-20180706 Developed by T.Morio'
echo -e "\n動作に必要なライブラリをインストールします。\nインストールされるライブラリ:\n・Python-usb\n・nfcpy\n"
echo -n インストールを開始しますか?[Y/n]:
read answer

if [ $answer = "Y" ]; then
        echo 'Python-usbのインストールを行っています...'
        yes | sudo apt install python-usb
        echo 'nfcpyのインストールを行っています...'
        yes | sudo pip install nfcpy
        echo 'インストール完了しました！'
else
        echo 'ライブラリのインストールがキャンセルされました。'
fi
