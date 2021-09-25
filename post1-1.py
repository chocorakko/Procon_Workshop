a=input("整数ａを入力してください：")
b=input("整数ｂを入力してください：")
a=int(a)
b=int(b)

for i in range(1, a+1):
	for j in range(1, b+1):
		print('%3d' % (i*j), end="\t")
	print()