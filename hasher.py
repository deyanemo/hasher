import sys
import os
import hashlib
import string

logo = '''
     888
     888
     888
 .d88888  .d88b.  888  888  8888b.  88888b.   .d88b.  88888b.d88b.   .d88b.
d88" 888 d8P  Y8b 888  888     "88b 888 "88b d8P  Y8b 888 "888 "88b d88""88b
888  888 88888888 888  888 .d888888 888  888 88888888 888  888  888 888  888
Y88b 888 Y8b.     Y88b 888 888  888 888  888 Y8b.     888  888  888 Y88..88P
 "Y88888  "Y8888   "Y88888 "Y888888 888  888  "Y8888  888  888  888  "Y88P"
                       888
                  Y8b d88P
                   "Y88P"
                   File Hasher 1.0v
                   ALL RIGHTS RESEVED To
                   DEYANEMO 2017(C)
'''
print(logo)
done = '''
`7MM"""Yb.     .g8""8q. `7MN.   `7MF'`7MM"""YMM  OO
  MM    `Yb. .dP'    `YM. MMN.    M    MM    `7  88
  MM     `Mb dM'      `MM M YMb   M    MM   d    ||
  MM      MM MM        MM M  `MN. M    MMmmMM    ||
  MM     ,MP MM.      ,MP M   `MM.M    MM   Y  , `'
  MM    ,dP' `Mb.    ,dP' M     YMM    MM     ,M ,,
.JMMmmmdP'     `"bmmd"' .JML.    YM  .JMMmmmmMMM db
'''
def letsDoThis():
    print(NotHashedFile)
    print(DesHashedFile)
    print("Methods : ")
    print("     1- MD5")
    print("     2- SHA1")
    print("     3- SHA224")
    print("     4- SHA256")
    print("     5- SHA384")
    print("     6- SHA512")
    Methods = input("What Method To use : ")
    Methods = int(Methods)

    if Methods == 1 and NotHashedFile and DesHashedFile :
        print("You choosed MD5")
        file = open(NotHashedFile , "r+")
        deyan = file.readlines()
        file.close()
        str1 = ''.join(deyan)
        file2 = open(DesHashedFile ,"w+")
        file2.write("#HashedWithMd5")
        for line in str1:
            md5 = hashlib.md5(line.encode("utf")).hexdigest()
            print(md5)
            file2.write(md5)
        print(done)
    elif Methods ==2 and NotHashedFile and DesHashedFile:
        print("You choosed SHA1")
        file = open(NotHashedFile , "r+")
        deyan = file.readlines()
        file.close()
        str1 = ''.join(deyan)
        file2 = open(DesHashedFile ,"w+")
        file2.write("#HashedWithSHA1")
        for line in str1:
            md5 = hashlib.sha1(line.encode("utf")).hexdigest()
            print(md5)
            file2.write(md5)
        print(done)
    elif Methods ==3 and NotHashedFile and DesHashedFile:
        print("You choosed SHA224")
        file = open(NotHashedFile , "r+")
        deyan = file.readlines()
        file.close()
        str1 = ''.join(deyan)
        file2 = open(DesHashedFile ,"w+")
        file2.write("#HashedWithSHA224")
        for line in str1:
            md5 = hashlib.sha224(line.encode("utf")).hexdigest()
            print(md5)
            file2.write(md5)
        print(done)
    elif Methods ==4 and NotHashedFile and DesHashedFile:
        print("You choosed SHA256")
        file = open(NotHashedFile , "r+")
        deyan = file.readlines()
        file.close()
        str1 = ''.join(deyan)
        file2 = open(DesHashedFile ,"w+")
        file2.write("#HashedWithSHA384")
        for line in str1:
            md5 = hashlib.sha256(line.encode("utf")).hexdigest()
            print(md5)
            file2.write(md5)
        print(done)
    elif Methods ==5 and NotHashedFile and DesHashedFile:
        print("You choosed SHA384")
        file = open(NotHashedFile , "r+")
        deyan = file.readlines()
        file.close()
        str1 = ''.join(deyan)
        file2 = open(DesHashedFile ,"w+")
        file2.write("#HashedWithSHA384")
        for line in str1:
            md5 = hashlib.sha384(line.encode("utf")).hexdigest()
            print(md5)
            file2.write(md5)
        print(done)
    elif Methods ==6 and NotHashedFile and DesHashedFile:
        print("You choosed SHA512")
        file = open(NotHashedFile , "r+")
        deyan = file.readlines()
        file.close()
        str1 = ''.join(deyan)
        file2 = open(DesHashedFile ,"w+")
        file2.write("#HashedWithSHA512")
        for line in str1:
            md5 = hashlib.sha512(line.encode("utf")).hexdigest()
            print(md5)
            file2.write(md5)
        print(done)
    else:
        print("Please Choose From The list above ^")
        print("Please Enter a File To Hash And a Destination")
NotHashedFile = input("File Name To Hash : ")
DesHashedFile = input("Hashed File Destination : ")
letsDoThis()
