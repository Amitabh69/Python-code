from time import *
import random as r

def mistake(paratest,usertest):                        #creating function to match existed para and user input para
      error = 0
      for i in range(len(paratest)):                   # range will define how many time the paratest will be checked and -
                                                       # -len will find the lenght of the para it wiil execute tiil the  number -1

            try:                                       # to counter the out of range error if the usertest exceeds the paratest
                  if paratest[i] != usertest[i]:
                        error = error + 1              # to increase the value of error
            except:
                  error = error + 1
      return error                                      # returning the value of error

def speed_time(start_time, end_time,user_input):        # function to find time difference
      delay_time=end_time - start_time
      round_of_time= round(delay_time,2)                # round fuction rounds the time and 2 is round of time
      speed = len(user_input)/round_of_time             # len will give the lenght of user_input including special character
      return round(speed)

while True:
      check = input("Ready to test : yes/no")
      if check == 'yes':
            test = ["I am a good boy"]                   # you can take any paragraph
            test1 = r.choice(test)                       # to check only one text from the list
            print("******typing speed******")
            print(test1)
            print()
            print()                                      # to give line break
            time_1 = time()                              # calling time function
            testinput = input("Enter-")                  # taking user input
            time_2 = time()                              # time after typing paragraph by the user

            print('speed:', speed_time(time_1, time_2, testinput), "word/sec")
            print('Error :', mistake(test1, testinput))
      elif check == 'no':
            print('Thank you')
            break
      else:
             print("wrong input")



