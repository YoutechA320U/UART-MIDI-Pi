# UART-MIDI-Pi
RaspberryPi Python用シリアル-MIDI変換プログラム。エクスクルーシブメッセージにも対応

## 概要
このプログラムは、RaspberryPiのUARTでMIDIメッセージをやり取りします。入力、出力共にGM/GS/XG、その他エクスクルーシブメッセージに対応します。

RaspberryPiZeroで使用するとOTG-MIDIとMIDIを併用する事が出来るようになります。

## 開発環境
    OS : Raspbian　stretch
    RaspberryPi : RaspberryPi ZeroWH,RaspberryPi 3B+
    Python : ver2.7
    GM/GS message_test : Timidity++
    XG/Ex message_test : NSX-39(PocketMiku)

## 必要なライブラリ
    pyserial,　python-rtmidi,　argparse

## 使い方
次の手順でRaspberryPiのUARTを有効にしてボーレートを31250bpsに設定します。

1,`uname -r`でLinuxカーネルのバージョンを確認してください。

2,カーネルのバージョンが4.5以上なら`/boot/config.txt`に以下の3行を追加して下さい。

    enable_uart=1
    dtoverlay=pi3-miniuart-bt
    dtoverlay=midi-uart0
3,バージョンが4.5未満なら`/boot/cmdline.txt`の末尾に改行せずに`bcm2708.uart_clock=3000000`を、`/boot/config.txt`に以下の2行を追加して下さい。

    init_uart_clock=2441406
    init_uart_baud=38400
    
4,カーネルのバージョンに関係なく`/boot/cmdline.txt`にある`console=serial0,115200`のような記述を削除して再起動して下さい。

また、このような(※画像は一例です)UART-MIDI変換回路をRaspberryPiに取り付けて下さい。

![SS](https://github.com/YoutechA320U/UART-MIDI-Pi/blob/master/UART-MIDI.png "UART-MIDI_example")

入力はuart-midi_in.py、出力はuart-midi_out.pyです。実行する時はできるだけ優先度を上げてください。ただし、FluidsythやTimidity等のソフトウェアシンセサイザーとこのプログラムを使う場合、それらよりも優先度を上げるとシンセサイザーやOSが処理落ちするので上手く調整してください。

実行すると入力は`UART_MIDI_IN`、出力は`UART_MIDI_OUT`という仮想MIDIポートが作成されます。これを他のMIDIポートに繋いでください。

それぞれ実行時に拡張子の後ろに -dと引数を付けて実行すると、入出力がコンソールに表示されます。

## 備考
エクスクルーシブメッセージのテストはポケットミクで行っています。あまりにも長いメッセージだと読み取りに失敗するかもしれません。

MIDI端子の名前にちなんで`UART_MIDI_IN`、`UART_MIDI_OUT`という仮想MIDIポート名ですが、Linux内部的には`UART_MIDI_IN`は仮想出力、`UART_MIDI_OUT`は仮想入力ポートです。

一度に大量のMIDIメッセージを受信すると処理落ちする事があります。また -d オプションを付けて実行すると入出力をコンソールに表示するので処理が重くなります。

### 参考コード・資料
 * <http://www.samplerbox.org/article/midiinwithrpi>  
 * <https://docs.python.org/ja/2.7/library/functions.html>
 * <https://qiita.com/unchainendo/items/1ea305d87c797ba02450>  
 * <https://github.com/SpotlightKid/python-rtmidi>  

## 履歴
    [2018/08/16] - 初回リリース
    [2018/08/18] - 余計なループ・変数を省いて高速化
    [2018/08/31] – 2018/09/01に取り下げました
    [2018/10/08] – 出力に対応
