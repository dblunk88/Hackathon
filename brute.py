import logging
import threading
import time
password = input("ENTER ZEH PASSWORD: ")
print("Muhchines arr fihring, Mahster")

def main():
    fourLetter('A','Z')
    fiveLetter('A','Z')

def fourLetter(beginChar,endChar):
    check = "{}{}{}{}"
    for a in range(ord(beginChar),ord(endChar)+1):
        for b in range(ord('A'),ord('Z')+1):
            for c in range(ord('A'),ord('Z')+1):
                for d in range(ord('A'),ord('Z')+1):
                    textCheck = check.format(chr(a),chr(b),chr(c),chr(d))
                    passCheck(textCheck)

def fiveLetter(beginChar,endChar):
    check = "{}{}{}{}{}"
    for a in range(ord(beginChar),ord(endChar)+1):
        for b in range(ord('A'),ord('Z')+1):
            for c in range(ord('A'),ord('Z')+1):
                for d in range(ord('A'),ord('Z')+1):
                    for e in range(ord('A'),ord('Z')+1):
                        textCheck = check.format(chr(a), chr(b), chr(c), chr(d),chr(e))
                        passCheck(textCheck)


def passCheck(check):
    if check == password:
        print(check)
        exit(0)


if __name__== "__main__":
  main()