# Write code below 💖

import random
question = input()
num = random.randint(1,9)

if num == 1:
  answer = "Yes!, Definitely"
elif num == 2:
  answer = "It is decided so"
elif num == 3:
  answer = "Without a doubt"
elif num == 4:
  answer = "Ask again later"
elif num == 5:
  answer = "Better not tell you now"
elif num == 6:
  answer = "My sources say no"  
elif num == 7:
  answer = "Outlook not so good"
elif num == 8:
  answer = "Very doubtful"
else:
  answer = "error"

print('Question:      ' + question) 
print('Magic 8 Ball:  ' + answer)