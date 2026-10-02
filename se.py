a = [0,0,1,1]
b = [0,1,0,1]

mor1 =[]
for i in range(4):
     if not(a[i]and b[i]) == True:
         mor1.append(1)
     else:
         mor1.append(0)
print("закон де моргана:",mor1)

mor2 =[]
for i in range(4):
     if not a[i] or not b[i] == True:
         mor2.append(1)
     else:
         mor2.append(0)
print("закон де моргана2:",mor2)

print ("A\tB\tмор1\tмор2")
for i in range(4):
    print(f"{a[i]}\t{b[i]}\t{mor1[i]}\t{mor2[i]}")

ble =[]
for i in range(4):
    if a[i] or(a[i]and b[i]) == True:
        ble.append(1)
    else:
        ble.append(0)
print("формула:",ble)

blu =[]
for i in range(4):
    if a[i] and (a[i]or b[i]) == True:
        blu.append(1)
    else:
        blu.append(0)
print("формула2:",blu)

print ("A\tB\tфор1\tфор2")
for i in range(4):
    print(f"{a[i]}\t{b[i]}\t{ble[i]}\t{blu[i]}")