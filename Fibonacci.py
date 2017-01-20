#Print Fibonacci series

#Enter number of terms in fibonacci series
n=int(input("Enter number of terms in fibonacci series: "))
n1=0
n2=1
counter=0

if n==1:
    print("Fibonacci series: \n")
    print(n1)
    
elif n==2:
        print("Fibonacci series: \n")
        print(n1)
        print(n2)
        
elif n>2:
            val=n1+n2
            print("Fibonacci series: ")
            print(n1)
            print(n2)
            while counter<n-1:
                val=n1+n2
                print(val)
                n1=n2
                n2=val
                counter+=1

else:
            print("Enter a positive number")
