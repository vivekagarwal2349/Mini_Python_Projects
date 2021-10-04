n,q=list(map(int,input().split()))
ans=list(map(int,input().split()[:n]))
c2=0
a=[]
b=[]
final=[]
#print(ans)
prime=[]
c1=q
c=2
prime_numbers = 0


########################################
def isprime(x):
    if x >= 2:
        for y in range(2,x):
            if not ( x % y ):
                return False
    else:
        return False
    return True
########################################
while(c1!=0):
    if(isprime(c)==True):
        c1-=1
        prime.append(c)
        c+=1
    else:
        c+=1
########################################

while(q!=0):
    b=[]
    a=[]
    for i in range(len(ans)):
        i=ans.pop()
        #print('i=',i)
        if(i%prime[c2]==0):
            b.append(i)
        else:
            a.append(i)
    #print("a=",a)
    #print("b=",b)
    ans=a
    final=final+b[::-1]
    #print("ans=",ans)
    #print("final=",final)
    #print("q=",q)
    q-=1
    c2+=1
    
final=final+a[::-1]
#print(a)
#print(final)
for i in final:
    print(i)




"""
SAMPLE

#INPUT:
5 2
3 3 4 4 9

#OUTPUT:
4
4
9
3
3
"""
