from array import *
import random
import math

def hextobin(hex):
    binnum = ""
    hexlen = 8
    i = 0
    while i<hexlen:
        if hex[i] == '0':
            binnum = binnum + "0000"
        elif hex[i] == '1':
            binnum = binnum + "0001"
        elif hex[i] == '2':
            binnum = binnum + "0010"
        elif hex[i] == '3':
            binnum = binnum + "0011"
        elif hex[i] == '4':
            binnum = binnum + "0100"
        elif hex[i] == '5':
            binnum = binnum + "0101"
        elif hex[i] == '6':
            binnum = binnum + "0110"
        elif hex[i] == '7':
            binnum = binnum + "0111"
        elif hex[i] == '8':
            binnum = binnum + "1000"
        elif hex[i] == '9':
            binnum = binnum + "1001"
        elif hex[i] == 'a' or hex[i] == 'A':
            binnum = binnum + "1010"
        elif hex[i] == 'b' or hex[i] == 'B':
            binnum = binnum + "1011"
        elif hex[i] == 'c' or hex[i] == 'C':
            binnum = binnum + "1100"
        elif hex[i] == 'd' or hex[i] == 'D':
            binnum = binnum + "1101"
        elif hex[i] == 'e' or hex[i] == 'E':
            binnum = binnum + "1110"
        elif hex[i] == 'f' or hex[i] == 'F':
            binnum = binnum + "1111"
        i = i+1
    return binnum

def binToDec(binary):
     
    res=int(binary,2)
    return res

n = int(input("Cache block size in bytes : "))
numoflines = int((2**17)/n)
#print(numoflines)
cc = [[0,0,0,0] for i in range(0,numoflines)]
bitsofindex = int(math.log(numoflines,2))
bitsofoffset = int(math.log(n,2))
bitsoftag = 32 -bitsofoffset -  bitsofindex


class cache():

    def __init__(self,data):
        self.data=data        
        self.b=hextobin(str(self.data))        #d is 32bit string of decimal instruction         
        self.hb=self.b.zfill(32)
        self.strtag = self.hb[0:bitsoftag]             #strtag is tag in str form
        self.strindex = self.hb[bitsoftag:32-bitsofoffset]          #strindex is index in str form
        self.tag=int(self.strtag)
        self.index=int(self.strindex)
        self.decindex=binToDec(self.strindex)                     #8 characters of hex
        

    def logic(self):

        if(self.tag == cc[self.decindex][0]):
            self.out=1
            return self.out

        elif(self.tag == cc[self.decindex][1] ):
            self.out=1
            return self.out

        elif(self.tag == cc[self.decindex][2] ):
            self.out=1
            return self.out

        elif(self.tag == cc[self.decindex][3] ):
            self.out=1
            return self.out

        elif(cc[self.decindex][0] == 0):
            cc[self.decindex][0] =self.tag
            self.out=0
            return self.out

        elif(cc[self.decindex][1] == 0):
            cc[self.decindex][1]=(self.tag)
            self.out=0
            return self.out

        elif(cc[self.decindex][2] == 0):
            cc[self.decindex][2]=(self.tag)
            self.out=0
            return self.out

        elif(cc[self.decindex][3] == 0):
            cc[self.decindex][3]=(self.tag)
            self.out=0
            return self.out

        list1=[0,1,2,3]
        r=random.choice(list1)
        cc[self.decindex][r]=(self.tag)
        self.out=0

        return self.out

if __name__ == "__main__":
    f = input("enter the file name")
    file = open(f)
    writefile = open("out.txt","w")
    lines = file.readlines()
    for line in lines:
        test = cache(line[4:12])
        y = str(test.logic())
        writefile.write(y+"\n")
    file.close()
    writefile.close()
    writefile = open("out.txt","r")
    tot_no_lines = 0
    no_of_1s = 0
    for line1 in writefile:
        #print(line1)
        tot_no_lines += 1
        if(line1[0] == "1"):
            no_of_1s += 1
    writefile.close()
    hitrate = (no_of_1s / tot_no_lines) * 100
    missrate = 100 - hitrate
    print("hitrate = ",hitrate,"  ","missrate = ",missrate)
    print(tot_no_lines," ",no_of_1s)

