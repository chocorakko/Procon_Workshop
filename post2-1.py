divider = 1
#count = 0
for i in range(1, 101):
    for j in range(2, i+1):
        if i%j==0:
            divider = j
            break
    if i==1:
        print("%3d 素数ではない" % i)
    elif divider==i:
        #count += 1
        print("%3d 素数" % i)
    else:
        print("%3d 素数ではない" % i)
#print("count %3d" % count)