#!/usr/bin/env python
# coding=utf-8
# author:admin[@hackfun.org]
# license:GPL v3
# blog:hackfun.org

RED = "\033[31m"
RESET = "\033[0m"

def error():
    print(RED)
    print("[!] Input error.")
    exit(1)

def encode():
    data = raw_input("[<-] Input data to encode: ")
    print("[->] Output shellcode: ")
    shellcode = ""
    for char in data:
        shellcode += "\\x" + char.encode("hex")
    print(RED)
    print(shellcode)
    exit(0)

def decode():
    data = raw_input("Input data to decode: ")
    if data.find("\\x") == -1:
        error()
    data = data.replace("\\x","")
    try:
        plain = data.decode("hex")
    except TypeError as e:
        error()
    print(RED)
    print(plain)
    exit(0)

def main():
    print("ShellCode encode decode")
    mode = raw_input("[<-] Input %s1[encode]%s or %s2[decode]%s:" % (RED, RESET, RED, RESET))
    if mode == "1" or mode == "encode":
        encode()
    elif mode == "2" or mode == "decode":
        decode()
    else:
        error()

if __name__ == '__main__':
    main()