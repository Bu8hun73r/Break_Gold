#!/usr/bin/python3
#-*- Coding:utf-8 -*-
from time import sleep as sl
from os import *
from pathlib import * 
from menu import *
from ahmil_functions import *

print(loading_message)

sl(1)

print(BG_logo)
print(menu)

choice = int(input("[+] Please Enter The Action's wished > "))
check = True

if choice == 0:
   pass 

elif choice == 1:
  scan()


elif choice == 2:
    # locate phone number  scipt goes here
    number = input("[+] Please Type The Number Wished > ")
    locate_number(number)
    input("Type Any Key To Finish ! ")






elif choice == 3:


    INFOS = uname_res(devicename = f'{socket.gethostname()}',  version = f'{VERSION}')
    print(f"\nWelcome To Power", end=" ")
    sl(0.7)
    print("BGT", end = " ")
    sl(0.5)
    print(f"\n{INFOS[0]} Using Power BGT ~ {INFOS[1]} \n ")
    sl(1)
    ## Power Ahmilter goes here !

    while True:
        BASE_DIR = Path(__file__).resolve().parent.parent
        command = input(f"{getcwd()} $ ")
        if command == '1' or command == 'scan':
           scan()
        elif command == "help" or command == "Help":
           print(PBGTH.__doc__) 
        elif command == '' or command == ' ':
          print("No Command")
          question = input("Needing help ? (y/n) ")
          if question == "y" or question == "Y" or question == "yes" or question == "Yes" or question == 'help':
              print(Help.__doc__)
          elif question == "n" or question == "N" or question == "no" or question == "No":
            pass
        else:
            print(system(command),"\n")












































