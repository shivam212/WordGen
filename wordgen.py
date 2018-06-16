import random
import time
a=[chr(i) for i in range(ord('a'),ord('z')+1)]
print('How many letters you want')
n=int(input())
total=int(0)
for i in range(n):
	total+=i
print(f"You will be entering a total of {total} charcters,Best of luck!!!!")
s=''
points=int(0)
t1=time.time()
for i in range(n):
	for j in range(i+1):
		s+=(random.choice(a))
	print(s)
	che=input()
	if(che==s):
		print("You earned one point")
		points+=1
	else:
		print(f"Sorry,better luck next time,you entered {che} instead of {s}")
	s=''
	t2=time.time()
print(f"You took {t2-t1} seconds to type {total} characters")
print(f"Your wpm was {(total/(n/2))/((t2-t1)/60)}")
print(f"You end the game with {points} points out of {n} .Winner Winner Chicken Dinner")