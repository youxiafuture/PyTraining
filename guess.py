# coding:utf-8

import random;

def input_guess_number(a,b):
    if(b > a):
        print "bigger than it,try again!"
        return False
    elif(b < a):
        print "smaller than it,try again!"
        return False
    else:
        print "you win! number is %d" % a
        return True

if __name__ == "__main__":
    origin = random.randint(1,100)
#    print origin
    num = 0
    result = False
    while(result == False):
        print "input your guessed number : "
        num = raw_input()
        result = input_guess_number(int(origin),int(num))
    else:
        print "The end."