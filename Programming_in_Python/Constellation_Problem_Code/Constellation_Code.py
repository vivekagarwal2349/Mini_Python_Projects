def call_mat(n,m): #finding 3x3 matrix of the input point
    a=final_list
    if(((m+1) and (m+2))<input_col and(((n+1) and (n+2))<3)):
        check_mat=[[a[n][m],a[n][m+1],a[n][m+2]],[a[n+1][m],a[n+1][m+1], a[n+1][m+2]], [a[n+2][m], a[n+2][m+1], a[n+2][m+2]]]
        return check_mat
    else:
        return 100 #just to see if the point is within range or not, if not, this is returned


#defining the matrix for A,E,I,O,U    
A=[['.','*','.'],['*','*','*'],['*','.','*']] #A star pattern
#print(A)
E=[['*','*','*'],['*','*','*'],['*','*','*']] #E star pattern
#print(E)
I=[['*','*','*'],['.','*','.'],['*','*','*']] #I star pattern
#print(I)
O=[['*','*','*'],['*','.','*'],['*','*','*']] #O star pattern
#print(O)
U=[['*','.','*'],['*','.','*'],['*','*','*']] #U star pattern
#print(U)    
    
input_col=int(input())  #taking input for column number
final_list=[]
#count_list=[]
for i in range(3):
    input_chars_row=list(str(input()).replace(' ',''))
    final_list.append(input_chars_row[:input_col]) # appending into the final list for the input matrix
    #dummy_list=[]
    #count_list.append(0)
#print(final_list)
#print(count_list)    
    
    

str1=''                               #variable to print the final answer
count_star=0
for i in range (len(final_list[0])):
    item=final_list[0][i]
    #print(item)
    if(item=="#"):
        str1+='#'
    elif(count_star==0):
        #print(i)
        answer=call_mat(0,i)
        
        if(answer==A):
            str1+='A'
            count_star=2
        elif(answer==E):
            str1+='E'
            count_star=2
        elif(answer==I):
            str1+='I'
            count_star=2
        elif(answer==O):
            str1+='O'
            count_star=2
        elif(answer==U):
            str1+='U'
            count_star=2
        elif(answer==100):
            c=1 #end condition
        #print(str1)
       #print(count_star)
    elif(count_star!=0):
        count_star-=1
    #print('c_satr',count_star)
print(str1)

"""

Sample:
############################
INPUT:

12
*.*#.***#.*.

*.*#..*.#***

***#.***#*.*

############################

OUTPUT:

U#I#A

"""



"""
Author: Sanmay Paniker
Github: Soupierbucket
"""
