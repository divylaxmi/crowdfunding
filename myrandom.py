import random

def randomnum():
    num=random.randrange(100000,999999)
    return num
    
def randomalphanum():
    charvalue="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    s=""
    for i in range(1,5):
        index = random.randrange(0,36)
        s = s + charvalue[index]
    return s
