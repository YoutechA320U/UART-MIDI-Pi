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
midiout.open_virtual_port("SerialMIDI") # 仮想MIDIポートの名前
ser = serial.Serial('/dev/ttyAMA0', baudrate=38400) #シリアル読み取り, ボーレート38400kbps
databyte = 0
data1 = 0
data2 = 0
data3 = 0
while True:
  databyte += 1
  if databyte == 1:
     data1 = ord(ser.read(1)) # 1byte目
     if data1 == 247:
         midiout.send_message([data1]) #0xf7 = 247 があったらここまで出力して1byte目に戻る
         databyte = 0
         if args.debug:
            print ('[{}]'.format(data1))
         else :
            pass
     else:
         pass
  if databyte == 2:
     data2 = ord(ser.read(1)) # 2byte目
     if data1 >= 192 and data1 <= 208 or data2 == 247: 
         midiout.send_message([data1,data2]) #3byte目まで無いメッセージがある場合出力して1byte目に戻る
         databyte = 0
         if args.debug:
            print ('[{}, {}]'.format(data1, data2))
         else :
            pass
     else:
         pass
  if databyte == 3 :
     data3 = ord(ser.read(1)) # 3byte目
     midiout.send_message([data1,data2,data3]) #3byteのメッセージを出力して1byte目に戻る
     databyte = 0
     if args.debug:
        print ('[{}, {}, {}]'.format(data1, data2, data3)) 
     else :
        pass
