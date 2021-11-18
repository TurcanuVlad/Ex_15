a=str(input('Scrieti numele dumneavoastra:'))
l=[]
l.extend(a)
if (ord(l[0])>=65 and ord(l[0])<=90):
    for i in l[1:]:
        if ord(i)>=97 and ord(i)<=122:
            y=True
        else:
            y=False
    if y==False:
        print("Numele este scris incorect")
    else:
        print("Numele este scris corect")
else:
    print('Este scris incorect')