def enkrip2(p,ku):
    k=len(ku)
    c=''
    for i in range(0,len(p)):
        c=c+chr(ord(p[i])+k)
    return c
def deskrip(p,ku):
    k=len(ku)
    c=''
    for i in range(0,len(p)):
        c=c+chr(ord(p[i])-k)
    return c