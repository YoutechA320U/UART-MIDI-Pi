# -*- coding: utf-8 -*-
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


midiin = rtmidi.MidiIn()
midiin.open_virtual_port("UART_MIDI_OUT") # 仮想MIDIポートの名前
ser = serial.Serial('/dev/ttyAMA0', baudrate=38400) #シリアル読み取り, ボーレート38400bps

timer = time.time()
while True:
  msg = midiin.get_message()
  if msg:
     message, deltatime = msg
     timer += deltatime
     try:
        data1 = message[0]
        data2 = message[1]
        data3 = message[2]
        ser.write(chr(data1))
        ser.write(chr(data2))
        ser.write(chr(data3))
        if args.debug:
           print ('[{}, {}, {}]'.format(data1,data2,data3))
     except:
        ser.write(chr(data1))
        ser.write(chr(data2))
        if args.debug: 
           print ('[{}, {}]'.format(data1,data2))
     continue
