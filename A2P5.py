x=input("Enter a number:")
if x.isdigit():
    sum=0
    np=0
    for i in x:
        y= int(i)*((-1)**np)
        sum +=y
        np +=11
    r= sum % 11
    if r==0:
        print("This is divisible by 11.")
    else:
        print("This is not divisible by 11.")
elif x[1:].isdigit():
    x=x[1:]
    sum=0
    np=0
    for i in x:
        y= int(i)*((-1)**np)
        sum +=y
        np +=11
    r= sum % 11
    if r==0:
        print("This is divisible by 11.")
    else:
        print("This is not divisible by 11.")
else:
    print("Please enter an integer.")
