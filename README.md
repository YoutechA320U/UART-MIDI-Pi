## UART-MIDI-Pi
RaspberryPi Python2.7用シリアル-MIDI変換プログラム

## 概要
このプログラムは、RaspberryPiのUARTでMIDIメッセージをやり取りします。現在は入力のみです。GM/GS/XG、その他エクスクルーシブに対応します。

## 必須ライブラリ
　　pyserial　python-rtmidi　argparse

## 開発環境
    OS : Raspbian　stretch
    RaspberryPi : RaspberryPi ZeroWH,RaspberryPi 3B+
    Python : ver2.7

## 使い方
できるだけ優先度を上げて実行してください。実行すると"SerialMIDI"という仮想MIDI出力ポートが作成されます。これを他のMIDI入力ポートにつないでください。-d オプション付けて実行すると、出力がコンソールに表示されます。

### 参考コード・資料
 * <http://www.samplerbox.org/article/midiinwithrpi>  
 * <https://docs.python.org/ja/2.7/library/functions.html>
 * <https://qiita.com/unchainendo/items/1ea305d87c797ba02450>  
 * <https://github.com/SpotlightKid/python-rtmidi>  

## 履歴 / History
