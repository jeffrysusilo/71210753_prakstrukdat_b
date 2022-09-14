range_data=int(input('masukan range data : '))
diction={}
for x in range (range_data):
    if x % 2 == 0:
        import math
        faktorial = math.factorial(x)
        diction[x]=faktorial
print(diction)
data = int(input("Data ditampilkan :"))

if data not in diction:
    print("data tidak ditemukan")
else:
    print("Value dari",data, "adalah", diction[data])