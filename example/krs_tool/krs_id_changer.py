#!/usr/bin/env micropython
# krs id and baud rate scanner
# 2025.6.21
# by T.Nishimura of AiRRC
#
from krs_driver_for_scaner import *
#
print('Start KRS change ID baudrate=1250000')
krs=KRSdriver()
#
def main():
  sid=krs.id_read()
  print("id now=",sid)
  sid=input("input new id <<")
  print("id now=",sid)
  krs.id_set(int(sid))
#
if __name__ == '__main__':
    main()
#