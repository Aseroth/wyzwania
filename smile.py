

smiles = [':)', ':-)', ':D', ';~)']

k=input()

def smileTest(k):
    y=0
    for x in range(len(k)):
        res = any(ele in k for ele in smiles)
        if res==True:
            y+=1
    print(res)


def smile2(k):
    res = False
    c=0
    for i in smiles:
        if(k.find(i)!=-1):
            c+=1
    if(c>=1):
        res=True
        print(c)


def kkk(k):
    c=[]
    for x in range(len(smiles)):
        c.append(k.count(smiles[x]))
    
    print(sum(c))

kkk(k)