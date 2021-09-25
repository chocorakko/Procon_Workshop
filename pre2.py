x = input("身長(cm)を入力してください：")
x = float(x)
if x<100:
    print("身長が100未満のため、乗れません。")
elif x>=100 and x<180:
    print("乗れます。")
else:
    print("身長が180以上のため、乗れません。")
