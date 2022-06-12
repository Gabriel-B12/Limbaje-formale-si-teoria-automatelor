
def operatie(b,c,d):
    global prioritate
    if b == "#": return exit()
    if b in "+": return c+"+"+d
    if b in "-": return c+"-"+d
    if b in "*": return c +"*"+ d
    if b in "/": return c +"/"+ d

def pr(a):
    if a=="#": return 0
    if a in "+-": return 1
    if a in "*/": return 2

m=input("Dati expresia aritmetica:")
if m=="":
    print("Eroare! Lipseste expresia.")
    exit()
n="#"+m+"#"
ok=0
prioritate=[0]
print(n)
st_operanzi=[]
st_operatori=[]
st_operatori.append("#")
i=0
while i<len(n):
    i+=1
    if n[i]=="(":
        ok+=1
    elif n[i]==")":
        ok-=1
    else:
        if n[i] not in "#+-*/":
            st_operanzi.append(n[i])
        else:
            st_operatori.append(n[i])
            prioritate.append(pr(n[i])+10*ok)
            nr=len(st_operatori)
            nr1=len(st_operanzi)
            nr2=len(prioritate)

            if prioritate[nr2-1]<=prioritate[nr2-2]:
                a=0;b=0;c=0
                print("Stiva Operatori:", st_operatori, " " * (25 - len(st_operatori) * 5), "Stiva Operanzi:", st_operanzi)
                print(" "*17,prioritate)
                if nr2>=3:
                    a=(prioritate[nr2-1]-pr(st_operatori[nr-1]))//10
                    b=(prioritate[nr2-2]-pr(st_operatori[nr-2]))//10
                    c=(prioritate[nr2-3]-pr(st_operatori[nr-3]))//10
                if a<b and b>c:
                    st_operanzi.append("("+operatie(st_operatori[nr-2],st_operanzi[nr1-2],st_operanzi[nr1-1])+")")
                else:
                    st_operanzi.append(operatie(st_operatori[nr-2],st_operanzi[nr1-2],st_operanzi[nr1-1]))
                st_operatori.pop(nr - 1);st_operatori.pop(nr - 2)
                st_operanzi.pop(nr1 - 1);st_operanzi.pop(nr1 - 2)
                prioritate.pop(nr2-1);prioritate.pop(nr2-2)
                i-=1


