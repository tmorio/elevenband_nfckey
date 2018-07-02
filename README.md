# elevenband_nfckey
タカラトミー社の「イナズマイレブン イレブンバンド」に内蔵されているNFCを用いて、カードキーシステムを構築するためのプログラムです。  
NFCチップでも可能です。  
  
動作には以下のライブラリが必要です。  
・nfcpy  
  
インストールを行うにはコンソール上(端末)で  
`brew install libusb`
`pip install nfcpy`
  
この2つのコマンドを実行することでインストールが行えます。  
  
使用を開始する前に、カードの情報を登録する必要があります。  
## イレブンバンド、イレブンライセンスなどのType2規格のチップを用いる場合
1.cardload.pyをsudo権限で実行し、カードリーダーにイレブンバンド(NFCチップ)をかざしてください。  
2.ID=XXXXXXXXXXXXXのXの部分をメモしてください。  
3.system.rbファイルを開き、「YourName1」にログに記録する名前、XXXXの部分に先程メモしたコードを正しく入れ、保存してください。  
例:記録する名前がAsuto Inamori、XXXXの部分が0123456789ABCDEFの場合  

    DB = {"Asuto Inamori" => "0123456789ABCDEF",
    	  "YourName2" => "XXXXXXXXXXXXXXX" }

4.以上でカード情報の登録は必要です。  
  
## Felica(交通系ICカードなど)を用いる場合
1.felicaload.pyをsudo権限で実行し、カードリーダーにカードをかざしてください。  
2.Type2規格と同じようにカードの登録を行ってください。  
3.system.rbの7行目にある「cardload.py」を「felicaload.py」に変更し保存してください。  
  
登録完了後、「sudo ruby system.rb」とコンソール上(端末上)で入力するとソフトウェアが起動し、カードリーダーが待機状態となります。  
  
## 終了方法
Ctrl+Cで終了させるか、バックグラウンドで動かしている場合、kill [PID]でプロセスキルしてください。  
