from itertools import permutations
import math

nElements = 7

P = list(permutations(range(nElements)))
#print(P)
S=[]
for i in P:
    S.append(list(i))

t = list(range(nElements))
n= len(t)
m = math.ceil((n-1)/2 + 1)

# f = open("two_step_forward_output_for n=7.tsv", "w")

# print("Bad Permutation", "Even Permutation", "ULL", "URR", "ULR", "URL", "List of cycle", "Original Potential", "List Of Potential After Swap", sep="\t", file = f)

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
        
def Potential(s,t):
    
    return 2*(len(ull(s,t)) + len(urr(s,t))) + (len(ulr(s,t)) + len(url(s,t))) + len(ListOfCycles(s,t))

def swap(s,i):  #Swap method
    newlist=[s[i]]
    newlist.extend(s[1:i])
    newlist.append(s[0])
    newlist.extend(s[i+1:])
    return newlist

def ListOfPotential_of_one_hop(s,t):
    if EvenPermutation(s,t) is True:
        list1 = []
        for i in l(s):
            k = swap(s,s.index(i))
            list1.append(Potential(k,t))
        #return list1         
        # for i in list1:
        #     if i < Potential(s,t):
        #         return True
        #     else: return False
        for i in list1:
           if i < Potential(s,t):
              return True
        return False                   

    else:
        list2 = []
        for i in r(s):
            k = swap(s,s.index(i))
            list2.append(Potential(k,t))
        # for i in list2:
        #     if i < Potential(s,t):
        #         return True
        #     else: return False    
        #return list2
        for i in list2:
           if i < Potential(s,t):
              return True
        return False 
# def one_step_bad_purmutation(s,t):
#     One_step_bad_permutation_list = []
#     for i in ListOfPotential_of_one_hop(s,t):
#         if i < Potential(s,t) - 1:
#             return True
#     return False

def ListOfPotential_of_two_hop(s,t):
    if EvenPermutation(s,t) is True:
        list1 = []
        for i in l(s):
            k = swap(s,s.index(i))
            list1.append(k)
        #return list1
        list11=[]
        for k in list1:
            for i in r(k):
                k2 = swap(k,k.index(i))
                list11.append(Potential(k2,t))
        for i in list11:
            if i < Potential(s,t) -1:
                return True
        
        return False    
        #return list11                   

    else:
        list2 = []
        for i in r(s):
            #list2 = []
            #print("")
            k = swap(s,s.index(i))
            list2.append(k)
        list22 =[]
        for k in list2:
            for i in l(k):
                k3 = swap(k,k.index(i))
                list22.append(Potential(k3,t))
        for i in list22:
            if i < Potential(s,t) -1:
                return True                    
        return False     

            #list2.append(Potential(k,t))
        #return list22

def Find_Bad_Permutation(s,t):
    
        
   if ListOfPotential_of_one_hop(s,t) is False and ListOfPotential_of_two_hop(s,t) is False:
       return True
   else: return False


f = open("one_step_and_two_step_forward_output_for n=7.tsv", "w")

print("Bad Permutation", "Even Permutation", "ULL", "URR", "ULR", "URL", "List of cycle", "Original Potential", "ListOfPotentialAfteroneSwap", "Potentialafter two swap", sep="\t", file = f)

# Main Loop

for s in S:
    bad_permutation = Find_Bad_Permutation(s,t)
    if bad_permutation is True:
       
        print(s, EvenPermutation(s, t), ull(s, t), urr(s, t), ulr(s, t), url(s, t), ListOfCycles(s, t), Potential(s, t), ListOfPotential_of_one_hop(s,t), ListOfPotential_of_two_hop(s,t), sep = "\t", file = f)


