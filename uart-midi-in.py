# -*- coding: utf-8 -*-
# 必須ライブラリ pyerial, python-rtmidi
import serial
import rtmidi
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
midiout = rtmidi.MidiOut()
midiout.open_virtual_port("UART_MIDI_IN") # 仮想MIDIポートの名前
ser = serial.Serial('/dev/ttyAMA0', baudrate=38400) #シリアル読み取り, ボーレート38400bps
while True:
  data1 = ord(ser.read(1)) #1バイト目
  if data1 >= 246:
      midiout.send_message([data1])
      if args.debug:
         print ('[{}]'.format(data1))
      else:
        pass
      continue
  else:
      data2 = ord(ser.read(1)) #2バイト目
      if 192 <= data1 <= 208 or data1 == 241 or data1 == 243 or data2 >= 246:
         midiout.send_message([data1,data2])
         if args.debug:
            print ('[{}, {}]'.format(data1, data2))
         else :
           pass
         continue
      else:
         data3 = ord(ser.read(1)) #3バイト目
         midiout.send_message([data1,data2,data3])
         if args.debug:
            print ('[{}, {}, {}]'.format(data1, data2, data3))
         else :
           pass
         continue
         
