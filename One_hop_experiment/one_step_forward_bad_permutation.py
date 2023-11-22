from itertools import permutations
import math

nElements = 5

P = list(permutations(range(nElements)))
#print(P)
S=[]
for i in P:
    S.append(list(i))

t = list(range(nElements))
n= len(t)
m = math.ceil((n-1)/2 + 1)

f = open("5.csv", "w")

print("Bad Permutation", "Even Permutation", "ULL", "URR", "ULR", "URL", "List of cycle", "Original Potential", "List Of Potential After Swap", sep="\t", file = f)

# Helper Functions

def l(s):                             # Definitions
    return s[1:m]
    #print(l(s))
def r(s):
    return s[m:n]
    #print(r(s))

def l(t):
    return t[1:m]
    #print(l(t))

def r(t):
    return t[m:n]
    #print(r(t))

def u(s,t):                           #List of Unsettled symbols
    u = []
    for i in range(n):
        if s[i] != t[i]:
            u.append(s[i])
    return u        
    #print(u(s,t)) 

def ull(s,t):                            # List of ULL,URR,ULR,URL guys
        
    return list(set(u(s,t)).intersection(set(l(s))).intersection(set(l(t))))
    #print(ull(s,t))

def urr(s,t):
    return list(set(u(s,t)).intersection(set(r(s))).intersection(set(r(t))))
    #print(urr(s,t))
    #print(urr(s,t)[0])

def ulr(s,t):
    return list(set(u(s,t)).intersection(set(l(s))).intersection(set(r(t))))
    #print(ulr(s,t))

def url(s,t):
    return list(set(u(s,t)).intersection(set(r(s))).intersection(set(l(t))))
    #print(url(s,t))

def cycle(s,t):                          # Cycle structure of permutation
    numbers= list(range(nElements))
    cycles = []
    while len(numbers) > 0 :
        c = []
        n0 = numbers[0]
        c.append(n0)
        m1 = s.index(t[n0])
        numbers.remove(n0) 

        while c[0] != m1 :
            c.append(m1)
            numbers.remove(m1)
            m1 = s.index(t[m1])
        cycles.append(c)
    return cycles   
    #print(cycle(s,t))       

def ListOfCycles(s,t):                          # Gives list Of Cycles whose length greater than 1
    C = [] 
    for i in cycle(s,t):
        if len(i) > 1 :
            C.append(i)
    return C
    #print(NoOfCycles(s,t))

#def Potential(s,t):
                    # Give the potential number of a source with respect to destination
    #if s[0]==0:               

        #return 2*(len(ull(s,t)) + len(urr(s,t))) + (len(ulr(s,t)) + len(url(s,t))) + 2*len(ListOfCycles(s,t)) + 1
    #else:
    # return 2*(len(ull(s,t)) + len(urr(s,t))) + (len(ulr(s,t)) + len(url(s,t))) + len(ListOfCycles(s,t))


#print("Original_Potential = " ,Potential(s,t))

def EvenPermutation(s,t):          # Checking a permutation is even or odd
    count = 0
    for i in ListOfCycles(s,t):
        if len(i) % 2 ==0:
            count += 1
            # else:
            #     return   
    if count % 2 == 0:
        return True
        
    else:
        return False
        
#print("Even" ,EvenPermutation(s,t))
def Potential(s,t):
    if EvenPermutation(s,t) is False and len(urr(s,t))==0 and len(url(s,t))==0:
        return 2*(len(ull(s,t)) + len(urr(s,t))) + (len(ulr(s,t)) + len(url(s,t))) + len(ListOfCycles(s,t)) + 1  
    elif EvenPermutation is True and len(ull(s,t))==0 and len(ulr(s,t))==0:
        return 2*(len(ull(s,t)) + len(urr(s,t))) + (len(ulr(s,t)) + len(url(s,t))) + len(ListOfCycles(s,t)) + 1
    else:
        return 2*(len(ull(s,t)) + len(urr(s,t))) + (len(ulr(s,t)) + len(url(s,t))) + len(ListOfCycles(s,t))

def swap(s,i):  
    newlist=[s[i]]
    newlist.extend(s[1:i])
    newlist.append(s[0])
    newlist.extend(s[i+1:])
    return newlist

def ListOfPotential(s,t):
    if EvenPermutation(s,t) is True:
        list1 = []
        for i in l(s):
            #list1 = []

            #print("")
            k = swap(s,s.index(i))
            list1.append(Potential(k,t))
        return list1
   

    else:
        list2 = []
        for i in r(s):
            #list2 = []
            #print("")
            k = swap(s,s.index(i))
            list2.append(Potential(k,t))
        return list2


def Find_Bad_Permutation(s,t):
    for i in ListOfPotential(s,t):
        if i < Potential(s,t):
            return True
    return False
        
# Main Loop

for s in S:
    bad_permutation = Find_Bad_Permutation(s,t)
    if bad_permutation is False:
       
       print(s, EvenPermutation(s, t), ull(s, t), urr(s, t), ulr(s, t), url(s, t), ListOfCycles(s, t), Potential(s, t), ListOfPotential(s, t), sep = "\t", file = f)
