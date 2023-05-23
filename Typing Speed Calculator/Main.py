from time import *
import random as r

def mistake(partest, usertest):
    error = 0 
    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i]:
                error = error + 1
        except:
            error = error + 1
    return error 

def speed_time(time_s, time_e, userinput):
    time_delay = time_e - time_s
    time_R = round(time_delay, 2)
    speed = len(userinput) / time_R
    return round(speed)

test = ["The quick brown fox jumps over the lazy dog", "Beginning to type stuff that makes sense.", "Welcome to this world", "Hello my name is"] 
test1 = r.choice(test)
print("        ********Typing Speed********")
print("Print the given sentence to calculate your typing")
print(test1)
print()
print()
time_1 = time()
testinput = input("Type the sentence: ")
time_2 = time()

print('Speed: ', speed_time(time_1, time_2, testinput), "w/sec")
print("Error: ", mistake(test1, testinput))
