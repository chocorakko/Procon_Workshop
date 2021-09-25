x = input("点数(100点満点)を入力してください：")
x = float(x)

if x>=90:
    print("特優")
elif x>=80 and x<90:
    print("優")
elif x>=70 and x<80:
    print("良")
elif x>=60 and x<70:
    print("可")
else:
    print("不可")
