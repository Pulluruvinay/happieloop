num=int(input("enter the given number:"))
n1,n2=0,1
count=0
if num<=0:
    print("enter a positive number:")
elif num==1:
    print("fibbonacci series upto",num,":")
else:
    print("fibbonacci series:")
    while count <num:
        print(n1)
        r=n1+n2
        n1=n2
        n2=r
        count+=1
        
