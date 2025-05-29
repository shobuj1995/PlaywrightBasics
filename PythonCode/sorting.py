number =[5,1,6,8,4,2,3,9,7]
n=len(number)
for i in range(n):
    for j in range(0,n-i-1):
        if(number[j]>number[j+1]):
            temp=number[j]
            number[j]=number[j+1]
            number[j+1]=temp
print(number)