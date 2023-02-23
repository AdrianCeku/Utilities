from ast import Add, Mult, Sub
from curses.ascii import isdigit
from dataclasses import replace
from hashlib import md5, sha256, sha512
import hashlib
import itertools
from re import T
from time import sleep
from typing_extensions import Self
from xmlrpc.client import boolean
import pyperclip
import string
import time

# Functions
def newNumber(x): 
    try: return(float(x))
    except:
        return(0)

def addNumber(x, y):
    global number
    if y != 0:
        number = x + y
        return(number)

def subNumber(x, y):
    global number
    if y != 0:
        number = x - y
        return(number)

def multNumber(x, y):
    global number
    if y != 0:
        number = x * y
        return(number)

def divNumber(x, y):
    global number
    if y != 0:
        number = x / y
        return(number)

def hashItMd5(x):
    hash = md5(x.encode()).hexdigest()
    return(hash)

def hashItSha256(x):
    hash = sha256(x.encode()).hexdigest()
    return(hash)

def hashItSha512(x):
    hash = sha512(x.encode()).hexdigest()
    return(hash)

def crackItSha256(hash, method):
    try: int(hash, 16)
    except: return("Not hex!")
    else: 
        if len(hash) == 64:
            for pwd_length in range(1,20):
                if method == "d" or method == "dic" or method == "dictionary":
                    print("working...")
                    for pwd in itertools.product(dictionaryList, repeat= pwd_length):
                        pwd = "".join(pwd)
                        if sha256(pwd.encode()).hexdigest() == hash:
                            return(pwd)
                elif method == "d+" or method == "dic+"  or method == "dictionary+":
                    print("working...")
                    for pwd in itertools.product(dictionaryList,"a","b","c","d","x","y","z","A","B","C","D","X","Y","Z","0","1","2","3","4","5","6","7","8","9", repeat= pwd_length):
                        pwd = "".join(str(pwd))
                        if sha256(pwd.encode()).hexdigest() == hash:
                            return(pwd)
                elif method == "b" or method == "brute"  or method == "bruteforce":
                    print("working...")
                    for pwd in itertools.product(string.printable, repeat= pwd_length):
                        pwd = "".join(pwd)
                        if sha256(pwd.encode()).hexdigest() == hash:
                            return(pwd)
        else: return("Not Sha256 hash!")

def crackItSha512(hash, method):
    try: int(hash, 16)
    except: return("Not hex!")
    else: 
        if len(hash) == 128:
            for pwd_length in range(1,20):
                if method == "d" or method == "dic" or method == "dictionary":
                    print("working...")
                    for pwd in itertools.product(dictionaryList, repeat= pwd_length):
                        pwd = "".join(pwd)
                        if sha512(pwd.encode()).hexdigest() == hash:
                            return(pwd)
                elif method == "b" or method == "brute"  or method == "bruteforce":
                    print("working...")
                    for pwd in itertools.product(string.printable, repeat= pwd_length):
                        pwd = "".join(pwd)
                        if sha512(pwd.encode()).hexdigest() == hash:
                            return(pwd)
        else: return("Not Sha512 hash!")

def crackItMd5(hash, method):
    try: int(hash, 16)
    except: return("Not hex!")
    else: 
        if len(hash) == 32:
            for pwd_length in range(1,20):
                if method == "d" or method == "dic" or method == "dictionary":
                    print("working...")
                    for pwd in itertools.product(dictionaryList, repeat= pwd_length):
                        pwd = "".join(pwd)
                        if md5(pwd.encode()).hexdigest() == hash:
                            return(pwd)
                elif method == "b" or method == "brute"  or method == "bruteforce":
                    print("working...")
                    for pwd in itertools.product(string.printable, repeat= pwd_length):
                        pwd = "".join(pwd)
                        if md5(pwd.encode()).hexdigest() == hash:
                            return(pwd)
        else: return("Not MD5 hash!")

def space(i, t):
    while i > 0:
        print()
        sleep(t)
        i -= 1

def utilities(up, down, t,):
    space(up, 0)
    print("Hello World!")
    time.sleep(t)
    print(" ____ ___   __  .__.__  .__  __  .__               ")
    time.sleep(t)
    print("|    |   \_/  |_|__|  | |__|/  |_|__| ____   ______")
    time.sleep(t)
    print("|    |   /\   __\  |  | |  \   __\  |/ __ \ /  ___/")
    time.sleep(t)
    print("|    |  /  |  | |  |  |_|  ||  | |  \  ___/ \___ \ ")
    time.sleep(t)
    print("|______/   |__| |__|____/__||__| |__|\___  >____  >")
    time.sleep(t)
    print("                                         \/     \/ ")
    time.sleep(t)
    print("by Sifro ")
    space(down, t)

def end(up, down, t):
    space(up, 0)
    print("Goodbye World!")
    time.sleep(t)
    print(" ____ ___   __  .__.__  .__  __  .__               ")
    time.sleep(t)
    print("|    |   \_/  |_|__|  | |__|/  |_|__| ____   ______")
    time.sleep(t)
    print("|    |   /\   __\  |  | |  \   __\  |/ __ \ /  ___/")
    time.sleep(t)
    print("|    |  /  |  | |  |  |_|  ||  | |  \  ___/ \___ \ ")
    time.sleep(t)
    print("|______/   |__| |__|____/__||__| |__|\___  >____  >")
    time.sleep(t)
    print("                                         \/     \/ ")
    time.sleep(t)
    print("by Sifro ")
    time.sleep(t * 3)
    space(down, t)
    global Running
    Running = False



## Loop Variables
Running = True # Program exit if false

#Math loops
Mathing = False
Adding = False
Subtracting = False
Multiplying = False
Dividing = False

#Crypto loops
Cryptographing = False

# Hashing loops
Hashing = False
HashingSha256 = False
HashingSha512 = False
HashingMd5 = False
Cracking = False

#Bruteforcing loops
BruteForcing = False
BruteForcingSha256 = False
BruteForcingSha512 = False
BruteForcingMd5 = False

# Dictionary Attacking loops
DictionaryAttacking = False
DictionaryAttackingSha256 = False
DictionaryAttackingSha512 = False
DictionaryAttackingMd5 = False

# Dictionary Attacking + loops
DictionaryAttackingPlus = False
DictionaryAttackingPlusSha256 = False
DictionaryAttackingPlusSha512 = False
DictionaryAttackingPlusMd5 = False

# Main varaibles
t = 0.06
number = 0
lastOperationOut = ""
pwd = ""
hash = ""
downHashAndCrack = 6

# Common digit and letter combinations
CommonDigitCombinations = []
CommonLowercaseCombinations = []
CommonUppercaseCombinations = []
CommonLowercaseAndUppercaseCombinations = []

CommonLowercase = ["a","b","c","d","x","y","z"]
for combination in itertools.product(CommonLowercase, repeat = 4):
    CommonLowercaseCombinations.append(combination)

CommonUppercase = ["A","B","C","D","X","Y","Z"]
for combination in itertools.product(CommonUppercase, repeat = 4):
    CommonUppercaseCombinations.append(combination)

for combination in itertools.product(CommonUppercase,CommonLowercase, repeat = 4):
    CommonLowercaseAndUppercaseCombinations.append(combination)

digits = ["0","1","2","3","4","5","6","7","8","9"]
for combination in itertools.product(digits, repeat = 4):
    CommonDigitCombinations.append(combination)

# Main
while Running:
    if t == 0: downHashAndCrack = 8
    utilities(100, downHashAndCrack, t*1.5)
    print("//>Utilities")
    time.sleep(t)
    print()
    time.sleep(t)
    print("[0] = Exit")
    time.sleep(t)
    print("[1] = Math")
    time.sleep(t)
    print("[2] = Cryptography")
    time.sleep(t)
    print()
    time.sleep(t*1.5)
    if t != 0:  # Creating dictionaryList for better dictionary attack performance
        dictionaryList = []
        dictionaryFile = open("dictionary.txt", 'r', errors="replace")
        print("Loading dictionary...")
        for pwd in dictionaryFile.readlines():
            dictionaryList.append(pwd.strip())
        dictionaryFile.close
        print(str(round(len(dictionaryList)/1000000)) + " million entries loaded!")
    t = 0
    print(">What do you want to do? ")
    input_ = input()
    if input_ == "0" or input_ == "end" or input_ == "exit": end(100, 11, 0.01)
    elif input_ == "1" or input_ == "math": Mathing = True
    elif input_ == "2" or input_ == "crypto": Cryptographing = True
    else: print("No valid input detected!")

# Mathing loops
    while Mathing:
        utilities(100, 4, 0)
        print("//>Utilities/>Math")
        print()
        print("[0] = Back")
        print("[1] = Addition")
        print("[2] = Subtraction")
        print("[3] = Multiplication")
        print("[4] = Division")
        print("[5] = Copy to clipboard")
        print("[6] = Set to 0")
        print()
        print(">Your number is: " + str(number) + ". What do you want to do? ")
        input_ = input()
        
        if input_ == "0" or input_ == "back" or input_ == "exit" or input_ == "end": Mathing = False
        elif input_ == "1" or input_ == "add": Adding = True
        elif input_ == "2" or input_ == "sub": Subtracting = True
        elif input_ == "3" or input_ == "mult": Multiplying = True
        elif input_ == "4" or input_ == "div": Dividing = True
        elif input_ == "5" or input_ == "copy": pyperclip.copy(number)
        elif input_ == "6" or input_ == "reset": number = 0

        else: print("No valid input detected")

        while Adding:
            utilities(100, 10, 0)
            print("//>Utilities/>Math/>Addition")
            print()
            print("[0] = Back")
            print()
            print(">[Addition] Your number is: " + str(number) + ". Adding... ")
            input_ = input()
            if input_ == "0" or input_ == "back" or input_ == "exit" or input_ == "end": Adding = False
            else: addNumber(number, newNumber(input_))
        
        while Subtracting:
            utilities(100, 10, 0)
            print("//>Utilities/>Math/>Addition")
            print()
            print("[0] = Back")
            print()
            print(">[Subtraction] Your number is: " + str(number) + ". Subtracting... ")
            input_ = input()
            if input_ == "0" or input_ == "back" or input_ == "exit" or input_ == "end": Subtracting = False
            else: subNumber(number, newNumber(input_))
        

        while Multiplying:
            utilities(100, 10, 0)
            print("//>Utilities/>Math/>Multiplication")
            print()
            print("[0] = Back")
            print()
            print(">[Multiplication] Your number is: " + str(number) + ". Multiplying... ")
            input_ = input()
            if input_ == "0" or input_ == "back" or input_ == "exit" or input_ == "end": Multiplying = False
            else: multNumber(number, newNumber(input_))
        

        while Dividing:
            utilities(100, 10, 0)
            print("//>Utilities/>Math/>Division")
            print()
            print("[0] = Back")
            print()
            print(">[Division] Your number is: " + str(number) + ". Dividing... ")
            input_ = input()
            if input_ == "0" or input_ == "back" or input_ == "exit" or input_ == "end": Dividing = False
            else: divNumber(number, newNumber(input_))
        
# Cryptographing loops
    while Cryptographing:
        lastOperationOut = ""
        utilities(100, 8, 0)
        print("//>Utilities/>Cryptography")
        print()
        print("[0] = Back")
        print("[1] = Hashing")
        print("[2] = Cracking")
        print()
        print(">What do you want to do? ")
        input_ = input()
        
        if input_ == "0" or input_ == "back" or input_ == "exit" or input_ == "end": Cryptographing = False
        elif input_ == "1" or input_ == "hash" or input_ == "hashing":  Hashing = True
        elif input_ == "2" or input_ == "crack" or input_ == "cracking":  Cracking = True

    # Hashing loops
        while Hashing:
            downHashAndCrack = 6
            if lastOperationOut != "": downHashAndCrack -= 1
            utilities(100, downHashAndCrack, 0)
            print("//>Utilities/>Cryptography/>Hashing")
            print()
            print("[0] = Back")
            print("[1] = Sha256")
            print("[2] = Sha512") 
            print("[3] = MD5 (Unsafe)")
            print("[4] = Copy last hash to clipboard")
            print()
            if lastOperationOut != "": print(lastOperationOut)
            print("> What do you want to do? ")
            input_ = input()

            if input_ == "0" or input_ == "back" or input_ == "exit" or input_ == "end": Hashing = False
            elif input_ == "1" or input_ == "sha256": HashingSha256 = True
            elif input_ == "2" or input_ == "sha512": HashingSha512 = True
            elif input_ == "3" or input_ == "md5": HashingMd5 = True
            elif input_ == "4" or input_ == "copy": pyperclip.copy(hash)

            while HashingSha256:
                downHashAndCrack = 8
                if lastOperationOut != "": downHashAndCrack -= 1
                utilities(100, downHashAndCrack, 0)
                print("//>Utilities/>Cryptography/>Hashing/>Sha256")
                print()
                print("[0] = Back")
                print("[1] = Paste from clipboard")
                print("[2] = Copy to clipboard")
                print()
                if lastOperationOut != "": print(lastOperationOut)
                print("> Which string do you want to hash? ")
                input_ = input()
                if input_ == "1" or input_ == "paste":input_ = pyperclip.paste()
                if input_ == "0" or input_ == "back": HashingSha256 = False
                elif input_ == "2" or input_ == "copy": pyperclip.copy(hash)
                else: 
                    hash = hashItSha256(input_)
                    lastOperationOut = "Your hash for \"" + input_ + "\" is: " + hash

            while HashingSha512:
                downHashAndCrack = 8
                if lastOperationOut != "": downHashAndCrack -= 1
                utilities(100, downHashAndCrack, 0)
                print("//>Utilities/>Cryptography/>Hashing/>Sha512")
                print()
                print("[0] = Back")
                print("[1] = Paste from clipboard")
                print("[2] = Copy to clipboard")
                print()
                if lastOperationOut != "": print(lastOperationOut)
                print("> Which string do you want to hash? ")
                input_ = input()
                if input_ == "1" or input_ == "paste":input_ = pyperclip.paste()
                if input_ == "0" or input_ == "back": HashingSha512 = False
                elif input_ == "2" or input_ == "copy": pyperclip.copy(hash)
                else: 
                    hash = hashItSha512(input_)
                    lastOperationOut = "Your hash for \"" + input_ + "\" is: " + hash

            while HashingMd5:
                downHashAndCrack = 8
                if lastOperationOut != "": downHashAndCrack -= 1
                utilities(100, downHashAndCrack, 0)
                print("//>Utilities/>Cryptography/>Hashing/>MD5")
                print()
                print("[0] = Back")
                print("[1] = Paste from clipboard")
                print("[2] = Copy to clipboard")
                print()
                if lastOperationOut != "": print(lastOperationOut)
                print("> Which string do you want to hash? ")
                input_ = input()
                if input_ == "1" or input_ == "paste":input_ = pyperclip.paste()
                if input_ == "0" or input_ == "back": HashingMd5 = False
                elif input_ == "2" or input_ == "copy": pyperclip.copy(hash)
                else: 
                    hash = hashItMd5(input_)
                    lastOperationOut = "Your hash for \"" + input_ + "\" is: " + hash

    # Cracking loops
        while Cracking:
            lastOperationOut = ""
            utilities(100, 7, 0)
            print("//>Utilities/>Cryptography/>Cracking")
            print()
            print("[0] = Back")
            print("[1] = Brute Force")
            print("[2] = Dictionary Attack")
            print("[3] = Dictionary Attack Plus (momentarily non functional)")
            print()
            print("> What do you want to do? ")
            input_ = input()

            if input_ == "0" or input_ == "back" or input_ == "exit" or input_ == "end": Cracking = False
            elif input_ == "1" or input_ == "brute" or input_ == "bruteforce" or input_ == "brute force": BruteForcing = True 
            elif input_ == "2" or input_ == "dic" or input_ == "dictionary" or input_ == "dictionary attack" or input_ == "dictionaryattack": DictionaryAttacking = True
            elif input_ == "3" or input_ == "dic+" or input_ == "dictionary+" or input_ == "dictionary attack+" or input_ == "dictionaryattack+": DictionaryAttackingPlus = True

            while BruteForcing:
                downHashAndCrack = 6
                if lastOperationOut != "": downHashAndCrack -= 1
                utilities(100, downHashAndCrack, 0)
                print("//>Utilities/>Cryptography/>Cracking/>Brute Force")
                print()
                print("[0] = Back")
                print("[1] = Crack Sha256")
                print("[2] = Crack Sha512")
                print("[3] = Crack MD5")
                print("[4] = Copy last password to clipboard")
                print()
                if lastOperationOut != "": print(lastOperationOut)
                print(">What do you want to do? ")
                input_ = input()

                if input_ == "0" or input_ == "back" or input_ == "exit" or input_ == "end": BruteForcing = False
                elif input_ == "1" or input_ == "sha256": BruteForcingSha256 = True
                elif input_ == "2" or input_ == "sha512":  BruteForcingSha512 = True
                elif input_ == "3" or input_ == "md5": BruteForcingMd5 = True
                elif input_ == "4" or input_ == "md5": pyperclip.copy(pwd)

                while BruteForcingSha256:
                    downHashAndCrack = 8
                    if lastOperationOut != "": downHashAndCrack -= 2
                    utilities(100, downHashAndCrack, 0)
                    print("//>Utilities/>Cryptography/>Cracking/>Brute Force/>Sha256")
                    print()
                    print("[0] = Back")
                    print("[1] = Paste from clipboard")
                    print("[2] = Copy to clipboard")
                    print()
                    if lastOperationOut != "": print(lastOperationOut)
                    print("> For which Hash do you want to find the password? ")
                    input_ = input()
                    if input_ == "1" or input_ == "paste":input_ = pyperclip.paste()
                    if input_ == "0" or input_ == "back": BruteForcingSha256 = False
                    elif input_ == "2" or input_ == "copy": pyperclip.copy(pwd)
                    else: 
                        pwd = crackItSha256(input_,"b")
                        if pwd == "Not hex!" or pwd == "Not Sha256 hash!":lastOperationOut = "No valid Sha256 hash detected!"
                        else:lastOperationOut = "Password found! It is: " + str(pwd) + "\nHash: " + input_

                while BruteForcingSha512:
                    downHashAndCrack = 8
                    if lastOperationOut != "": downHashAndCrack -= 2
                    utilities(100, downHashAndCrack, 0)
                    print("//>Utilities/>Cryptography/>Cracking/>Brute Force/>Sha512")
                    print()
                    print("[0] = Back")
                    print("[1] = Paste from clipboard")
                    print("[2] = Copy to clipboard")
                    print()
                    if lastOperationOut != "": print(lastOperationOut)
                    print("> For which Hash do you want to find the password? ")
                    input_ = input()
                    if input_ == "1" or input_ == "paste":input_ = pyperclip.paste()
                    if input_ == "0" or input_ == "back": BruteForcingSha512 = False
                    elif input_ == "2" or input_ == "copy": pyperclip.copy(pwd)
                    else: 
                        pwd = crackItSha512(input_, "b")
                        if pwd == "Not hex!" or pwd == "Not Sha512 hash!":lastOperationOut = pwd
                        else:lastOperationOut = "Password found! It is: " + pwd + "\nHash: " + input_
            
                while BruteForcingMd5:
                    downHashAndCrack = 8
                    if lastOperationOut != "": downHashAndCrack -= 2
                    utilities(100, downHashAndCrack, 0)
                    print("//>Utilities/>Cryptography/>Cracking/>Brute Force/>MD5")
                    print()
                    print("[0] = Back")
                    print("[1] = Paste from clipboard")
                    print("[2] = Copy to clipboard")
                    print()
                    if lastOperationOut != "": print(lastOperationOut)
                    print("> For which Hash do you want to find the password? ")
                    input_ = input()
                    if input_ == "1" or input_ == "paste":input_ = pyperclip.paste()
                    if input_ == "0" or input_ == "back": BruteForcingMd5 = False
                    elif input_ == "2" or input_ == "copy": pyperclip.copy(pwd)
                    else: 
                        pwd = crackItMd5(input_,"b")
                        if pwd == "Not hex!" or pwd == "Not MD5 hash!":lastOperationOut = pwd
                        else:lastOperationOut = "Password found! It is: " + pwd + "\nHash: " + input_
            
            
            
            while DictionaryAttacking:
                downHashAndCrack = 6
                if lastOperationOut != "": downHashAndCrack -= 2
                utilities(100, downHashAndCrack, 0)
                print("//>Utilities/>Cryptography/>Cracking/>Dictionary Attack")
                print()
                print("[0] = Back")
                print("[1] = Crack Sha256")
                print("[2] = Crack Sha512")
                print("[3] = Crack MD5")
                print("[4] = Copy last password to clipboard")
                print()
                if lastOperationOut != "": print(lastOperationOut)
                print(">What do you want to do? ")
                input_ = input()

                if input_ == "0" or input_ == "back" or input_ == "exit" or input_ == "end": DictionaryAttacking = False
                elif input_ == "1" or input_ == "sha256": DictionaryAttackingSha256 = True
                elif input_ == "2" or input_ == "sha512":  DictionaryAttackingSha512 = True
                elif input_ == "3" or input_ == "md5": DictionaryAttackingMd5 = True
                elif input_ == "4" or input_ == "md5": pyperclip.copy(pwd)

                while DictionaryAttackingSha256:
                    downHashAndCrack = 8
                    if lastOperationOut != "": downHashAndCrack -= 2
                    utilities(100, downHashAndCrack, 0)
                    print("//>Utilities/>Cryptography/>Cracking/>Dictionary Attack/>Sha256")
                    print()
                    print("[0] = Back")
                    print("[1] = Paste from clipboard")
                    print("[2] = Copy to clipboard")
                    print()
                    if lastOperationOut != "": print(lastOperationOut)
                    print("> For which Hash do you want to find the password? ")
                    input_ = input()
                    if input_ == "1" or input_ == "paste":input_ = pyperclip.paste()
                    if input_ == "0" or input_ == "back": DictionaryAttackingSha256 = False
                    elif input_ == "2" or input_ == "copy": pyperclip.copy(pwd)
                    else: 
                        pwd = crackItSha256(input_, "d")
                        if pwd == "Not hex!" or pwd == "Not Sha256 hash!":lastOperationOut = "No valid Sha256 hash detected!"
                        elif pwd == "Not found on list!":lastOperationOut ="Password is not on list!"
                        else:lastOperationOut = "Password found! It is: " + pwd + "\nHash: " + input_

                while DictionaryAttackingSha512:
                    downHashAndCrack = 8
                    if lastOperationOut != "": downHashAndCrack -= 2
                    utilities(100, downHashAndCrack, 0)
                    print("//>Utilities/>Cryptography/>Cracking/>Dictionary Attack/>Sha512")
                    print()
                    print("[0] = Back")
                    print("[1] = Paste from clipboard")
                    print("[2] = Copy to clipboard")
                    print()
                    if lastOperationOut != "": print(lastOperationOut)
                    print("> For which Hash do you want to find the password? ")
                    input_ = input()
                    if input_ == "1" or input_ == "paste":input_ = pyperclip.paste()
                    if input_ == "0" or input_ == "back": DictionaryAttackingSha512 = False
                    elif input_ == "2" or input_ == "copy": pyperclip.copy(pwd)
                    else: 
                        pwd = crackItSha512(input_, "d")
                        if pwd == "Not hex!" or pwd == "Not Sha512 hash!":lastOperationOut = pwd
                        else:lastOperationOut = "Password found! It is: " + pwd + "\nHash: " + input_
            
                while DictionaryAttackingMd5:
                    downHashAndCrack = 8
                    if lastOperationOut != "": downHashAndCrack -= 2
                    utilities(100, downHashAndCrack, 0)
                    print("//>Utilities/>Cryptography/>Cracking/>Dictionary Attack/>MD5")
                    print()
                    print("[0] = Back")
                    print("[1] = Paste from clipboard")
                    print("[2] = Copy to clipboard")
                    print()
                    if lastOperationOut != "": print(lastOperationOut)
                    print("> For which Hash do you want to find the password? ")
                    input_ = input()
                    if input_ == "1" or input_ == "paste":input_ = pyperclip.paste()
                    if input_ == "0" or input_ == "back": DictionaryAttackingMd5 = False
                    elif input_ == "2" or input_ == "copy": pyperclip.copy(pwd)
                    else: 
                        pwd = crackItMd5(input_, "d")
                        if pwd == "Not hex!" or pwd == "Not MD5 hash!":lastOperationOut = pwd
                        else:lastOperationOut = "Password found! It is: " + pwd + "\nHash: " + input_

            while DictionaryAttackingPlus:
                downHashAndCrack = 6
                if lastOperationOut != "": downHashAndCrack -= 2
                utilities(100, downHashAndCrack, 0)
                print("//>Utilities/>Cryptography/>Cracking/>Dictionary Attack Plus")
                print()
                print("[0] = Back")
                print("[1] = Crack Sha256")
                print("[2] = Crack Sha512")
                print("[3] = Crack MD5")
                print("[4] = Copy last password to clipboard")
                print()
                if lastOperationOut != "": print(lastOperationOut)
                print(">What do you want to do? ")
                input_ = input()

                if input_ == "0" or input_ == "back" or input_ == "exit" or input_ == "end": DictionaryAttacking = False
                elif input_ == "1" or input_ == "sha256": DictionaryAttackingPlusSha256 = True
                elif input_ == "2" or input_ == "sha512":  DictionaryAttackingPlusSha512 = True
                elif input_ == "3" or input_ == "md5": DictionaryAttackingPlusMd5 = True
                elif input_ == "4" or input_ == "md5": pyperclip.copy(pwd)

                while DictionaryAttackingPlusSha256:
                    downHashAndCrack = 8
                    if lastOperationOut != "": downHashAndCrack -= 2
                    utilities(100, downHashAndCrack, 0)
                    print("//>Utilities/>Cryptography/>Cracking/>Dictionary Attack Plus/>Sha256")
                    print()
                    print("[0] = Back")
                    print("[1] = Paste from clipboard")
                    print("[2] = Copy to clipboard")
                    print()
                    if lastOperationOut != "": print(lastOperationOut)
                    print("> For which Hash do you want to find the password? ")
                    input_ = input()
                    if input_ == "1" or input_ == "paste":input_ = pyperclip.paste()
                    if input_ == "0" or input_ == "back": DictionaryAttackingPlusSha256 = False
                    elif input_ == "2" or input_ == "copy": pyperclip.copy(pwd)
                    else: 
                        pwd = crackItSha256(input_, "d+")
                        if pwd == "Not hex!" or pwd == "Not Sha256 hash!":lastOperationOut = "No valid Sha256 hash detected!"
                        elif pwd == "Not found on list!":lastOperationOut ="Password is not on list!"
                        else:lastOperationOut = "Password found! It is: " + pwd + "\nHash: " + input_

                while DictionaryAttackingPlusSha512:
                    downHashAndCrack = 8
                    if lastOperationOut != "": downHashAndCrack -= 2
                    utilities(100, downHashAndCrack, 0)
                    print("//>Utilities/>Cryptography/>Cracking/>Dictionary Attack Plus/>Sha512")
                    print()
                    print("[0] = Back")
                    print("[1] = Paste from clipboard")
                    print("[2] = Copy to clipboard")
                    print()
                    if lastOperationOut != "": print(lastOperationOut)
                    print("> For which Hash do you want to find the password? ")
                    input_ = input()
                    if input_ == "1" or input_ == "paste":input_ = pyperclip.paste()
                    if input_ == "0" or input_ == "back": DictionaryAttackingPlusSha512 = False
                    elif input_ == "2" or input_ == "copy": pyperclip.copy(pwd)
                    else: 
                        pwd = crackItSha512(input_, "d+")
                        if pwd == "Not hex!" or pwd == "Not Sha512 hash!":lastOperationOut = pwd
                        else:lastOperationOut = "Password found! It is: " + pwd + "\nHash: " + input_
            
                while DictionaryAttackingPlusMd5:
                    downHashAndCrack = 8
                    if lastOperationOut != "": downHashAndCrack -= 2
                    utilities(100, downHashAndCrack, 0)
                    print("//>Utilities/>Cryptography/>Cracking/>Dictionary Attack Plus/>MD5")
                    print()
                    print("[0] = Back")
                    print("[1] = Paste from clipboard")
                    print("[2] = Copy to clipboard")
                    print()
                    if lastOperationOut != "": print(lastOperationOut)
                    print("> For which Hash do you want to find the password? ")
                    input_ = input()
                    if input_ == "1" or input_ == "paste":input_ = pyperclip.paste()
                    if input_ == "0" or input_ == "back": DictionaryAttackingPlusMd5 = False
                    elif input_ == "2" or input_ == "copy": pyperclip.copy(pwd)
                    else: 
                        pwd = crackItMd5(input_, "d+")
                        if pwd == "Not hex!" or pwd == "Not MD5 hash!":lastOperationOut = pwd
                        else:lastOperationOut = "Password found! It is: " + pwd + "\nHash: " + input_

#58c99e0afb626c7cbebc4614fdf11f7f42db71b73cbb8d5176493a550334bb2582424a9cb676e92f498a4f1c5957924a586b19a239bd0d008264497366d12355