
from random import *

users = range(1,51)
users = list (users)

shuffle(users)

winners = sample(users, 4)

shuffle (winners)
print ("-- 당첨자 발표 --")
print ("첫번째 당첨자는 {}번 입니다.".format(winners[0]))
print ("두번째 당첨자는 {}번 입니다.".format(winners[1]))
print ("세번째 당첨자는 {}번 입니다.".format(winners[2]))
print ("네번째 당첨자는 {}번 입니다.".format(winners[3]))
print ("-- 축하합니다. --")