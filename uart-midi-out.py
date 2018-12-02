# -*- coding: utf-8 -*-
# 必須ライブラリ pyerial, python-rtmidi
import time
import rtmidi
import serial
import argparse

# パーサーを作る
parser = argparse.ArgumentParser(
            add_help=True, # -h/?help オプションの追加
            )

# 引数の追加
parser.add_argument('-d', '--debug', help='show midi message',
                    action='store_true') #デバッグモード追加

# 引数を解析する
args = parser.parse_args()

# MIDIポート設定
midiin = rtmidi.MidiIn()
midiin.open_virtual_port("UART_MIDI_OUT") # 仮想MIDIポートの名前
ser = serial.Serial('/dev/ttyAMA0', baudrate=38400) #シリアル読み取り, ボーレート38400bps
midiin.ignore_types(sysex=False, timing=True, active_sense=True)
timer = time.time()
while True:
      msg = midiin.get_message()
      if msg:
         message, deltatime = msg
         timer += deltatime
         if args.debug:
            print (message)
         else :
           pass
         outmidi = [chr(i) for i in message]
         ser.write(outmidi)
         continue
