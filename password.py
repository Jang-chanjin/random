import random

pw = input("바꾸려는 비밀번호를 입력하세요: ")

pw = list(pw)

random.shuffle(pw)

pw = str(pw[:3]) + random.choice('Helppw') + random.choice('Helppw')  + "!!"
#print(pw)
newpw = "".join(pw)
print ("바꾼 비밀번호는 {}입니다.".format(newpw))
