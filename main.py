a = [0,0,1,1]
b = [0,1,0,1]


kon = []
for i in range(4):
     if (a[i] and b[i]) == True:
         kon.append(1)
     else:
         kon.append(0)

print("Конъюнкция A B: ", kon)

diz = []
for i in range(4):
    if (a[i] or b[i]) == True:
       diz.append(1)
    else:
     diz.append(0)
print("Дизъюнкция A B: ", diz)

otc= []
for i in range(4):
    if (not a[i]) == True:
        otc.append(1)
    else:
        otc.append(0)
print("отриц A : ", otc)

otr = []
for i in range(4):
    if (not b[i]) == True:
        otr.append(1)
    else:
        otr.append(0)
print("отриц B : ", otr)

imp =[]
for i in range(4):
    if (not a[i] or b[i]) == True:
        imp.append(1)
    else:
        imp.append(0)
print("имплекация A B :", imp)

print ("A\tB\tкон\tдиз\t-A\t-B\tимп")
for i in range(4):
    print(f"{a[i]}\t{b[i]}\t{kon[i]}\t{diz[i]}\t{otc[i]}\t{otr[i]}\t{imp[i]}")


