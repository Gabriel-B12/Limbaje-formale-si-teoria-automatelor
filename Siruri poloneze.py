
def pr(a):
    if a=="(": return 0
    if a in "+-": return 1
    if a in "*/": return 2

n=input("Dati expresia aritmetica:")
if n=="":
    print("Eroare! Lipseste expresia.")
    exit()
sir_p=""
st_operatori=[]
prioritate=[]
for i in range(0,len(n)):
    if n[i] in "+-*/(":
        st_operatori.append(n[i])
        prioritate.append(pr(n[i]))
        if  len(st_operatori)>2 and prioritate[-1]!=0  and prioritate[-1]<=prioritate[-2] :
            sir_p=sir_p+st_operatori[-2]
            st_operatori.pop(-2)
    elif n[i]==")":
        for j in range(len(st_operatori)-1,-1,-1):
            if st_operatori[j]!="(":
                sir_p=sir_p+st_operatori[j]
                st_operatori.pop(j)
            else:
                st_operatori.pop(j)
                break

    else:
        sir_p=sir_p+n[i]
while len(st_operatori)!=0:
    sir_p=sir_p+st_operatori[-1]
    st_operatori.pop(-1)
print("Sirul polonez genearat: ",sir_p)
print("Verificarea corectitudinii generarii sirului polonez:")
st_operanzi=[]
for i in range(len(sir_p)):
    if sir_p[i] in "+-*/":
        print(st_operanzi)
        if sir_p[i-1] in "+-*/" and pr(sir_p[i-1])<pr(sir_p[i]):
            aux = st_operanzi[-2] + sir_p[i] +"("+ st_operanzi[-1]+")"
        elif len(sir_p)-i>2 and sir_p[i+2] in "+-*/" and pr(sir_p[i])<pr(sir_p[i+2]):
            aux = "("+st_operanzi[-2] + sir_p[i] + st_operanzi[-1]+")"
        else:
            aux = st_operanzi[-2] + sir_p[i] + st_operanzi[-1]
        st_operanzi.pop(-1);st_operanzi[-1]=aux
    else:
        st_operanzi.append(sir_p[i])


print("Expresie rezultata in urma verificarii: ",st_operanzi[0])

