import phonenumbers
from phonenumbers import geocoder, carrier
import socket, time
from menu import *



'''\
    This file contains all Break gold 's functions.
    In fack it's like a package that contains more 
    functionality's code than others...
    Just for BG project!
'''    








s = socket.socket()

def locate_number(number):

    accepting_list = ['Y','y','yes', 'Yes','Yup','yup','YES','OK','ok']
    refusing_list = ['N','n','Non','non','NON']

    if int(len(number)) <= 9:
        print("Please Make Sure You Have Put \nThe Country's Code.")
        print("If Done type [Y or y]\nElse (to add it) [N or n]", end='')
        warn = input('>')

        # SO IN THIS CASE, WE'LL CHECK THE USER'S ANSWER
        # TO SEE (While His/Her Answer Is ) IN BOTH
        # LISTS (Lists Above accepting_list AND refusing_list)
       
        
        if warn in accepting_list:
            print("OKay !\n")
            
        elif warn in refusing_list:
            country_code = input("Country Code (+nn/+nnn) >")
            if not country_code.startswith('+'):
                country_code = '+'+country_code
            number = f'{country_code}{number}'
    elif int(len(number)) > 9:
        if not number.startswith('+'):
            number = '+'+number
        elif number.startswith('00'):
            number.replace('00', '+')
            
    country_h = phonenumbers.parse(number, "CH")
    
    # THEN JUST UNDERMENTIONED, IN complete_info VARIABLE, 
    # IF THE USER HAVE TYPE THE EXACT NUMBER WITH A VALIDE COUNTRY CODE
    # HE/SHE 'LL GET A GOOD RESULT THAT WILL BE THE COUNTRY'S NAME OF THAT NUMBER.
    # ELSE IT(the complete_info var) WILL RETURN AN EMPTY STRING THAT'S None.
    
    complete_info = geocoder.description_for_number(country_h, "en")

    # TO AVOID ANY DYSFUNCTIONS, Break Gold WILL CHECK THE complete_info VARIABLE'S VALUE:
    # If IT RETURN AN EMPTY STRING, OR None VALUE !
    # Break Gold WILL APOLOGIZE AND THEN BREAK.
    # THE IMPORTANT THING IS THIS ONE: Break Gold WILL TELL THE USER WATH TO DO.
     
    if complete_info == '':
        print("Sorry Break Gold Can't Find Any information.\n")
        time.sleep(0.5)
        print("\t"+"*"*3+"Check Out Of Your Country Code And Retry"+"*"*3)
        quit()
    # IF THE VARIABLE complete_info ISN'T None,
    # Break Gold WILL SHOW THE COUNTRY'S NAME OF THIS NUMBER.
            
    country_hs = phonenumbers.parse(number, "RO")
    service_useds = carrier.name_for_number(country_h, "en")
    print(f"\n\nINFO : {number} Checking ...")
    print(f"Country : {complete_info}")
    print(f"Service Used : {service_useds}")

#####  ###  ### ###
###    PORT'S SCAN PART OR TESTING PART
####   ### ### ###

def scan(ipaddr = "", port = 1):
    wish = input("[y/n] Would You Like To Scan Your?> ")
    if wish == 'y':
        ipaddr = socket.gethostbyname(socket.gethostname())
        print("Just My Self !")
    else:
        ipaddr = input("Target > ")
        ipsplit = ipaddr.split('.')
    
        if not ipsplit[0].isnumeric():
            print("Getting Host's IP ...")
            ipaddr = socket.gethostbyname(ipaddr)
            time.sleep(1)
            print(f"IP: {ipaddr}")
            time.sleep(1)
        elif ipsplit[0].isnumeric():
            ipaddr = socket.gethostname(ipaddr)
            print(f"Getting Address By Name... ")
            print(f"Name Found : {ipaddr}")
        else:
            print("Sorry Address Not Found")
            quit()

        while ipaddr == '':
            print('PLZ Enter The host ip :', end = '')
            ipaddr = input()

        print("Checking For Target ...")
        time.sleep(1)
        print("Valide Address !")
        print("Starting up ...\n")

        for port in range(10, 101, 5):
            check(ipaddr, port)
            if port == 100:
                set_succeful_message(ipaddr)
            port += 1


def check(ipaddr, port):
    try:
        counter = 0
        #time.sleep(1/299792458)
        s.connect((ipaddr, port))
        print(f"Port {port} Is Open")
        counter += 1
    except:
        print(f"Port {port} Is Closed ")
        if counter == 0:
            return counter - 1
        else:
            return counter + 1



def set_succeful_message(ipaddr, counter = 1):
    print("[+] INFO::")
    print(f"Host Scaned {ipaddr} \nAction Has Succefully Finished  !\n{counter} Ports Are Open\n")



def uname_res(devicename, version):
    return devicename, version
    

def PBGTH():
    """Usage: Power BGT
  Command [Options]

  Options:

     -h      --help             To show this help and pass
     -V      --VERSION          To show the Power BGT's version
     -o      --osinfo           Operating system's info
     etc..."""






