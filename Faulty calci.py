#Design a calci which will solve operations except
#45*3=555,56+9,56/6=4


print("Operation: +,-,*,/")
Opt=input("Enter the Operation to perform: ")
n1=int(input("Enter First Number: "))
n2=int(input("Enter Second Number: "))


if Opt=="+":
    if n1==56 and n2==9:
        print("77")
    else:
        print("Addition = ",n1+n2)
elif Opt=="-":
    print("Subtraction : ",n1-n2)
elif Opt=="*":
    if n1==45 and n2==3:
        print("Multiplication : ",555)
    else:
        print("Multiplication : ",n1*n2)
elif Opt=="/":
    if n1==56 and n2==4:
        print("DIVIDE : ",4)
    else:
        print("DIVIDE : ",n1/n2)
else:
    print("Plz selecct correct option")



