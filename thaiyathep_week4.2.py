import time
def wela():
    vantee = time.localtime()
    d1 = time.strftime("%d %B %Y, %H:%M:%S", vantee)
    print(d1)
NAME = []
SC = []
TT = []
HIT = []
num = int(input("Plese Enter Num of Compettitor : "))
for i in range(num):
    name = input("Plese Enter Compettitor Name : ")
    pts = float(input("Enter PTS Score : "))
    tim = float(input("Enter Time : "))
    NAME.append(name)
    SC.append(pts)
    TT.append(tim)
    HIT.append(pts/tim)
for i in range(num):
    j = i
    for j in range(num):
        if HIT[i] > HIT[j]:
            z,x,c,v = HIT[i],SC[i],TT[i],NAME[i]
            HIT[i],SC[i],TT[i],NAME[i] = HIT[j],SC[j],TT[j],NAME[j]
            HIT[j],SC[j],TT[j],NAME[j] = z,x,c,v
vantee = time.localtime()
a = time.strftime("%A", vantee)
b = time.strftime("%Y", vantee)
print("Shortgun "+a+"Training",b,"\nCondition : 1")
wela()
print("_"*100)
print("{0:-<6}{1:-<6}{2:-<8}{3:-<17}{4:-<12}{5:-<15}{6}".format("NO.","PTS","TIME","COMPETITOR#Name","HIT FACTOR","STATE POINTS","STATE PERCENT"))
print("_"*100)
for i in range(num):
    PO = (HIT[i]/HIT[0])*50
    PE = (PO/(HIT[0]/HIT[0]*50))*100
    print("{0:_<6}{1:_<6}{2:_<8}{3:_<17}{4:_<12}{5:_<15}{6}".format(i+1,int(SC[i]),"%.2f"%TT[i],NAME[i],"%.4f"%HIT[i],"%.4f"%PO,"%.2f"%PE))