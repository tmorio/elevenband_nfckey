# elevenband_nfckey
タカラトミー社の「イナズマイレブン イレブンバンド」に内蔵されているNFCを用いて、カードキーシステムを構築するためのプログラムです。  
その他NFCチップでも可能です。  
  
製作方法の記事は小山高専 エレクトロニクス研究部のサイトに載せてありますので、そちらをご確認くださいますようお願い申し上げます。
[(前半)(本当の)0からNFCでカギを操作するソフトを作る。](https://eleken.jp/archives/1758)  
[(後半)(本当の)0からNFCでカギを操作するソフトを作る。](https://eleken.jp/archives/1886)  
  
動作には以下のライブラリが必要です。  
・nfcpy  
  
nfcpyについては次をご覧下さい。[nfcpy/nfcpy](https://github.com/nfcpy/nfcpy)  
    
インストールを行うにはコンソール上(端末)で  
`apt install python-usb`
`pip install nfcpy`
  
この2つのコマンドを実行することでインストールが行えます。  
  
使用を開始する前に、カードの情報を登録する必要があります。  
## イレブンバンド、イレブンライセンスなどのType2規格のチップを用いる場合
1.cardload.pyをroot権限で実行し、カードリーダーにイレブンバンド(NFCチップ)をかざしてください。  
2.ID=XXXXXXXXXXXXXのXの部分をメモしてください。  
3.system.rbファイルを開き、「YourName1」にログに記録する名前、XXXXの部分に先程メモしたコードを正しく入れ、保存してください。  
例:記録する名前がAsuto Inamori、XXXXの部分が0123456789ABCDEFの場合  

    DB = {"Asuto Inamori" => "0123456789ABCDEF",
    	  "YourName2" => "XXXXXXXXXXXXXXX" }

4.以上でカード情報の登録は必要です。  
  
## Felica(交通系ICカードなど)を用いる場合
1.felicaload.pyをroot権限で実行し、カードリーダーにカードをかざしてください。  
2.Type2規格と同じようにカードの登録を行ってください。  
3.system.rbの7行目にある「cardload.py」を「felicaload.py」に変更し保存してください。  
  
登録完了後、「sudo ruby system.rb」とコンソール上(端末上)で入力するとソフトウェアが起動し、カードリーダーが待機状態となります。  

## GPIOの初期設定について
初期状態ではGPIO4がサーボモーターのPWM出力となっています。  
変更する際はlock.pyとunlock.pyのpwmgpioの値を変更することで、PWM出力に使うピンを変更できます。  
  
## 終了方法
Ctrl+Cで終了させるか、バックグラウンドで動かしている場合、kill [PID]でプロセスキルしてください。  

## 注意事項
当プログラムで発生した問題、損害について製作者は責任を負いかねます。  
自己責任でご利用ください。
