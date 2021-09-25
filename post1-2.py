x = input("身長(m)を入力してください：")
y = input("体重(kg)を入力してください：")
x = float(x)
y = float(y)

bmi = y/(x**2)
print("BMI = %.2f" % bmi)

if bmi<18.5:
    print("低体重")
elif bmi>=18.5 and bmi<25.0:
    print("普通体重")
elif bmi>=25.0 and bmi<30.0:
    print("肥満1度")
elif bmi>=30.0 and bmi<35.0:
    print("肥満2度")
elif bmi>=35.0 and bmi<40.0:
    print("肥満3度")
else:
    print("肥満4度")
