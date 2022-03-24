 #fungsi mengurutkan nilai bilangan 
def BubbleSort(num):
    for i in range(len(num)-1,0,-1):
        for j in range(i):
            if num[j] > num[j+1]: 
                temp = num[j]
                num[j] = num[j+1]
                num[j+1] = temp
                
num = []
sum = 0
#
print("************Program Bilangan************")
n = int(input('Masukkan Banyak Bilangan : ')) # fungsi untuk memasukan banyaknya bilangan
for i in range(0,n):
    x = int(input('Masukkan bilangan ke : '+ str(i+1) + ' = '))
    #fungsi memasukan bilangan ke 1 dan seterusnya
    num.append(x)   
BubbleSort(num) 
print("\nUrutan bilangan (dari terkecil ke terbesar) =", num)
for j in range(0,n): 
    sum = sum + num[j] 
average = sum/len(num) 
#nilai rata-rata/jumlah atau banyak data 
print("\nNilai rata-rata :", average)
if(len(num) % 2 == 0):
    idx1 = len(num)//2  
    idx2 = (len(num)//2) + 1    
    median = (num[idx1-1]+num[idx2-1])//2
else:
    idx = (len(num)//2)+1 
    median = num[idx-1]        
print("Nilai tengah :", median)
mul = 1 
for k in range(0,int(n)):
    mul = mul * num[k] 
 #looping dengan mengalikan setiap bilangan 
print("Hasil perkalian :", mul)
