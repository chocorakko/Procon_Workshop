select = input("機能番号(1,2,3)を入力してください：")
select = int(select)

x = input("中間試験の点数(100点満点)を入力してください：")
y = input("期末試験の点数(100点満点)を入力してください：")
z = input("課題点(20点満点)を入力してください：")
x = float(x)
y = float(y)
z = float(z)

avg=(x+y)/2
year=(avg*0.80)+z

if select==1:
    print("中間・期末試験の平均点 = %.2f 点" % avg)
elif select==2:
    print("通年成績 = %.2f 点" % year)
elif select==3:
    if year>=90:
        print("特優")
    elif year>=80 and year<90:
        print("優")
    elif year>=70 and year<80:
        print("良")
    elif year>=60 and year<70:
        print("可")
    else:
        print("不可")