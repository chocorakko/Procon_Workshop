select = input("乗り物番号(1,2)を入力してください：")
select = int(select)

x = input("身長(cm)を入力してください：")
x = float(x)

if select==1:
    if x<100:
        print("身長が100未満のため、乗れません。")
    elif x>=100 and x<180:
        print("乗れます。料金は800円です。")
    else:
        print("身長が180以上のため、乗れません")
elif select==2:
    if x<100:
        print("身長が100未満のため、乗れません。")
    elif x>=100 and x<180:
        print("乗れます。料金は1,000円です。")
    else:
        print("乗れます。料金は1,200円です。")
