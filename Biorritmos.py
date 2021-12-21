from datetime import date
import math


birthday = int(input("Your Birth Day: "))
birthmonth = int(input("Your Birth Month: "))
birthyear = int(input("Your Birth Year: "))


birth = date(birthyear, birthmonth, birthday)
sum = date.today() - birth

phisical = (math.sin((2*math.pi*sum.days) / 23))*100
emotional = (math.sin((2*math.pi*sum.days) / 28))*100
intelectual = (math.sin((2*math.pi*sum.days) / 33))*100
intuitional = (math.sin((2*math.pi*sum.days) /38))*100

print("Your phisical level is: ", '% .2f' % phisical)
print("Your emotional level is: ", '% .2f' % emotional)
print("Your intelectual level is: ", '% .2f' % intelectual)
print("Your intuitional level is: ", '% .2f' % intuitional)
