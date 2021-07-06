from random import randrange


def SaveFile(path,data):
    file = open(path,'a',encoding='utf-8')
    file.writelines(data)
    file.close()
def SaveFileRandom(path,nlines):
    file = open(path,'a',encoding='utf-8')
    for l in range(nlines):
        for i in range(nlines):
            file.write(str(randrange(-100,100)) + ';')
        file.write('\n')
    file.close()

def ReadFile(path,symsplit):
    lstSP=[]
    file=open(path,'r',encoding='utf-8')
    for line in file:
        data=line.strip()
        lst=data.split(symsplit)
        lstSP.append(lst)
    file.close()
    return lstSP

def XuatSP(lstSP):
    for row in lstSP:
        for element in row:
            print(element,end='\t')
        print()
    print()

def XuatSoAm(lstSP):
    for row in lstSP:
        for element in row:
            if int(element) < 0:
                print(element,end='\t')
        print()
    print()

def SortSP(lstSP):
    for i in range(len(lstSP)):
        for j in range(len(lstSP)):
            a=lstSP[i]
            b=lstSP[j]
            if a[2] > b[2]:
                # Hoán vị
                lstSP[i]=b
                lstSP[j]=a