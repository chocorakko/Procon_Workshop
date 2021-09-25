select = input("機能番号(1,2,3)を入力してください：")
select = int(select)

x = input("身長(m)を入力してください：")
y = input("体重(kg)を入力してください：")
x = float(x)
y = float(y)

bmi = y/(x**2)
weight = 22*(x**2)

if select==1:
    print("BMI = %.2f" % bmi)
elif select==2:
    print("適正体重 = %.2f" % weight)
elif select==3:
    if bmi<18.5:
        print("要注意：やせ症の可能性がある")
    elif bmi>=18.5 and bmi<25.0:
        print("基準値")
    else:
        print("要注意：肥満症の可能性がある")