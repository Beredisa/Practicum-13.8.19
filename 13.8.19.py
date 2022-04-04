n = int(input("Количество блетов = "))
c = input("Возраст ( вводить через запятую) = ")
summ = 0
L = c.split(",")
l = list(map(int,L))

for i in l :
   if i<18 :
     summ += 0
     continue
   elif 18<=i<=25 :
     summ  += 990
     continue
   elif 25<i :
     summ += 1390
     continue

if n < 3 :
    summ += 0
else :
    summ *=0.9

print("Сумма к оплате  = ",int(summ),"руб.")
print("Приятного просмотра!")

