## UART-MIDI-Pi
RaspberryPi Python2.7用シリアル-MIDI変換プログラム

## 概要
このプログラムは、RaspberryPiのUARTでMIDIメッセージをやり取りします。現在は入力のみです。GM/GS/XG、その他エクスクルーシブに対応します。

## 開発環境
    OS : Raspbian　stretch
    RaspberryPi : RaspberryPi ZeroWH,RaspberryPi 3B+
    Python : ver2.7
    
## 必要なライブラリ
    library :  pyserial,　python-rtmidi,　argparse

## 使い方
予めここ<http://www.samplerbox.org/article/midiinwithrpi>を参考にRaspberryPiのUARTを有効にしてボーレートを31250bpsに設定してください。また、適当なシリアル-MIDI回路をRaspberryPiに取り付けてください。

実行する時はできるだけ優先度を上げてください。ただし、FluidsythやTimidity等のソフトウェアシンセサイザーとこのプログラムを使う場合、それらよりも優先度を上げるとシンセサイザーが処理落ちするので上手く調整してください。

実行すると"SerialMIDI"という仮想MIDI出力ポートが作成されます。これを他のMIDI入力ポートに繋いでください。

python uart-midi.py -dとオプション付けて実行すると、出力がコンソールに表示されます。

## 備考
一度に大量のMIDIメッセージを受信すると処理落ちするので気をつけて下さい。また -d オプションを付けて実行すると出力をコンソールに表示する分処理が重くなります。

### 参考コード・資料
 * <http://www.samplerbox.org/article/midiinwithrpi>  
 * <https://docs.python.org/ja/2.7/library/functions.html>
 * <https://qiita.com/unchainendo/items/1ea305d87c797ba02450>  
 * <https://github.com/SpotlightKid/python-rtmidi>  

## 履歴
    [2018/08/16] - 初回リリース
    [2018/08/18] - 余計なループ・変数を省いて高速化
