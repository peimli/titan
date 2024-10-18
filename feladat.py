def kisebb(szam1,szam2):
    if szam1 < szam2:
        return(szam1)
    else:
        return(szam2)
print(kisebb(3,1))

def nagyobb(szam1,szam2):
    if szam1 > szam2:
        return(szam1)
    else:
        return(szam2)
print(nagyobb(3,1))

def nezet_kerulet(szam1):
    szam1=szam1*4
    return(szam1)
print(nezet_kerulet(5))

def negyzet_terulet(szam1):
    return szam1*szam1
print(negyzet_terulet(6))

def teglalap_kerulete(szam1,szam2):
    return 2*(szam1+szam2)
print(teglalap_kerulete(4,5))
    
    
