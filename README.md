## UART-MIDI-Pi
RaspberryPi Python2.7用シリアル-MIDI変換プログラム

※※重要※※ uart-midi-out.pyはまだ正常に動作しないので、実行しないで下さい

## 概要
このプログラムは、RaspberryPiのUARTでMIDIメッセージをやり取りします。入力はGM/GS/XG、その他エクスクルーシブに対応します。

## 開発環境
    OS : Raspbian　stretch
    RaspberryPi : RaspberryPi ZeroWH,RaspberryPi 3B+
    Python : ver2.7

## 必要なライブラリ
    pyserial,　python-rtmidi,　argparse

## 使い方
予めここ<http://www.samplerbox.org/article/midiinwithrpi>を参考にRaspberryPiのUARTを有効にしてボーレートを31250bpsに設定してください。また、適当なシリアル-MIDI回路をRaspberryPiに取り付けてください。

入力はuart-midi_in.py.出力はuart-midi_out.pyです。実行する時はできるだけ優先度を上げてください。ただし、FluidsythやTimidity等のソフトウェアシンセサイザーとこのプログラムを使う場合、それらよりも優先度を上げるとシンセサイザーが処理落ちするので上手く調整してください。

実行すると入力は"UART_MIDI_IN"出力は"UART_MIDI_OUT"という仮想MIDI出力ポートが作成されます。これを他のMIDIポートに繋いでください。

それぞれpython *.py -dと-dオプション付けて実行すると、入出力がコンソールに表示されます。

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
    [2018/08/31] – 出力にも対応
    [2018/09/01] – 出力にも対応を取り下げ
