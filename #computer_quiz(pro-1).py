# computer quiz game
score =0
play = input("do you want to play game ")
if (play.lower()!="yes"):
    exit()
answer1 = input("who is the prime minister of india? ")
if (answer1.lower()=="narendra modi"):
    score += 1
    print("correct answer")
else:
    print ("wrong answer")
answer2 = input("who is the president of india? ")
if (answer2.lower()=="ram nath kovind"):
    score += 1
    print("correct answer")
else:
    print ("wrong answer")
answer3 = input("who is the cheif minister of telangana state? ")
if (answer3.lower()=="kalvakuntla chandra shekhar rao"):
    score += 1
    print("correct answer")
else:
    print ("wrong answer")
answer4 = input("which award in india is the highest civilian award? ")
if (answer4.lower()=="bharat ratna"):
    score += 1
    print("correct answer")
else:
    print ("wrong answer")
print(score)
if(score==4):
    print("congragulation :) ")
elif(score==3):
    print("congragulation :) ")
elif(score==2):
    print("better luck next time! ")
else:
    print("please try again properly! ")