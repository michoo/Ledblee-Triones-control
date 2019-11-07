# Ledblee-Triones-control
Ledblee Triones bluetooth controled rgb bulb

https://www.ebay.ca/itm/RGB-RGBW-LED-Bulb-Light-Color-Change-E27-Lamp-Bulbs-Dimmable-Remote-Controller/254240747070

## Preparation
```
sudo hcitool lescan
LE Scan ...
FF:FF:55:E0:98:AA  Triones-FFFF55E098AA
$ sudo gatttool -I
[                 ][LE]> connect FF:FF:55:E0:98:AA 
Attempting to connect to FF:FF:55:E0:98:AA
Connection successful
[FF:FF:55:E0:98:AA][LE]> primary
attr handle: 0x0001, end grp handle: 0x0004 uuid: 0000ffd0-0000-1000-8000-00805f9b34fb
attr handle: 0x0005, end grp handle: 0x0007 uuid: 0000ffd5-0000-1000-8000-00805f9b34fb
[FF:FF:55:E0:98:AA][LE]> char-desc
handle: 0x0001, uuid: 00002800-0000-1000-8000-00805f9b34fb
handle: 0x0002, uuid: 00002803-0000-1000-8000-00805f9b34fb
handle: 0x0003, uuid: 0000ffd4-0000-1000-8000-00805f9b34fb
handle: 0x0004, uuid: 00002902-0000-1000-8000-00805f9b34fb
handle: 0x0005, uuid: 00002800-0000-1000-8000-00805f9b34fb
handle: 0x0006, uuid: 00002803-0000-1000-8000-00805f9b34fb
handle: 0x0007, uuid: 0000ffd9-0000-1000-8000-00805f9b34fb
```
to identify what you can do, use on your smart phone bluetooth app like "Blue Scanner" on Iphone to play with uuid (first digits). Then, you'll identify write, read,... For me 0xffd9 was the input to upload colours. So the handle is 0x0007 (see example below, at the end)


## Color mode command

cmd: 56(11)(22)(33)(44)f0aa
1. Red
1. Green
1. Blue
1. White

## Pattern mode command
cmd: bb(11)(22)44
* 1: Color mode
  * 23: Smooth color
  * 24: ???
  * 25: Smooth color
  * 26: Smooth red
  * 27: Smooth green
  * 28: Smooth blue
  * 29: Smooth yellow
  * 2a: Smooth cyan
  * 2b: Smooth purple
  * 2c: Smooth rgb white
  * 2d: r to g to b 
  * 2e: r to g to b 
  * 2f: r to g to b
  * 30: rgb strobe
  * 31: red strobe
  * 32: green strobe
  * 33: blue strobe
  * 34: strobe...
* 2: Speed

## example of complete command
```
sudo gatttool  -b FF:FF:55:E0:98:AA  --char-write -a 0x0007 -n bb260544
```