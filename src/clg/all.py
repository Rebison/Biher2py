from program10 import main as pgm10
import program8 as pgm8

def swap_variable():
    x = 5
    y = 10
    temp = x 
    x = y
    y = temp
    print(f'The value of x after swapping: {x}') 
    print(f'The value of y after swapping: {y}')

def dist_btw_2pts():
    x1=int(input("Enter x1: ")) 
    y1=int(input("Enter y1: ")) 
    x2=int(input("Enter x2: ")) 
    y2=int(input("Enter y2: "))
    result= ((((x2 - x1 )**2) + ((y2-y1)**2) )**0.5)
    print("Distance between",(x1,y1),"and",(x2,y2),"is : ",result)


def total_mark():
    mark = [] 
    tot = 0
    print("Enter Marks Obtained in 5 Subjects: ") 
    #for i in range(5):
        #mark.insert(i,int(input()))
    mark.extend(input().split(' '))
    #    mark.insert(i,input())
    for i in range(5):
        tot = tot + int(mark[i])
    #tot = sum(mark)
    avg = tot/5
    calc_grade(avg)
    
def calc_grade(avg):
    if (avg>=91 and avg<=100): 
        print("Your Grade is A1")
    elif (avg>=81 and avg<=91): 
        print("Your Grade is A2")
    elif (avg>=71 and avg<=81): 
        print("Your Grade is B1")
    elif (avg>=61 and avg<=71): 
        print("Your Grade is B2")
    elif (avg>=51 and avg<=61): 
        print("Your Grade is C1")
    elif (avg>=41 and avg<=51): 
        print("Your Grade is C2")
    elif (avg>=33 and avg<=41): 
        print("Your Grade is D")
    elif (avg>=21 and avg<=33): 
        print("Your Grade is E1")
    elif (avg>=0 and avg<=21): 
        print("Your Grade is E2")
    else:
        print("Invalid Input!")

def SumOfSeries():
    n=int(input("Enter the number of terms: ")) 
    sum1=0
    for i in range(1,n+1):
        sum1=sum1+(1/i)
    print("The sum of series is",round(sum1,2))
    
def gcd(a,b):
    if(b==0): 
        return a
    else:
        return gcd(b,a%b) 

def remove_vowels(s): 
    new_str=" "
    for i in s:
        if i in "aeiouAEIOU": 
            pass
        else:
            new_str+=i
    print("The String without vowel is:",new_str) 

def add2matrix():
    X=[[2,5,4],[1,3,9],[7,6,2]]
    Y=[[1,8,5],[7,3,6],[4,0,9]]
    result=[[0,0,0],[0,0,0],[0,0,0]]
    for i in range(len(X)): 
        for j in range(len(Y)):
            result[i][j]=X[i][j]+Y[i][j] 
    for r in result:
        print(r)

Dict={0:0, 1:1}
def fibo(n):
    if n not in Dict:
        val=fibo(n-1)+fibo(n-2)
        Dict[n]=val 
    return Dict[n]

count=0
c='y'
while 'y'==c.lower():
    print("="*20)
    print(f'{" Lab programs ":*^20}')
    print("="*20)

    print("1. Swap value of two variables\n\
2. Distance between two points\n\
3. Grade of Students using the marks scored in All Subjects\n\
4. Find the Sum of Series 1/n^2\n\
5. Calculate Gcd Using Recursive Function\n\
6. Re-displays the string after removing vowels\n\
7. Add Two Matrices using Nested Lists\n\
8. \n\
9. Calculate Fib(n) using dictionary\n\
10. calculate the percentage of vowels and consonants in the file.\n\
")

    try:
        choice=int(input("Enter your choice: "))
        
    except ValueError:
        print("Invalid Input")

    except KeyboardInterrupt:
        print("Bye Bye!!")
        break

    else:
        if choice>11:
            print("Enter the choice number from 1 to 8")
            continue
        
        print(f"{'Program Begins':-^30}")
        if choice==1:
            swap_variable()

        elif choice==2:
           dist_btw_2pts()

        elif choice==3:
            total_mark()

        elif choice==4:
            SumOfSeries()

        elif choice==5:
            a=int(input("Enter first number:")) 
            b=int(input("Enter second number:")) 
            GCD=gcd(a,b)
            print("GCD is: ",GCD)
            
        elif choice==6:
            str=input("Enter a string:") 
            remove_vowels(str)
            
        elif choice==7:
            add2matrix()
            
        elif choice==8:
            pgm8.main()

        elif choice==9:
            n=int(input("Enter the value of n:")) 
            print("Fibonacci(", n,")= ", fibo(n))

        elif choice==10:
            pgm10.main()          

        print(f"{'Program End':-^30}")

    count+=1
    c=input("Do you want to continue (Y/N): ")
    print("\n")

else:
    print("Number of time loop executed",count)
    print("Bye Bye!!")

