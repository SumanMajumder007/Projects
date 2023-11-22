from itertools import permutations
import math
import time

start = time.time()

nElements = 9

P = list(permutations(range(nElements)))
#print(P)
S=[]
for i in P:
    S.append(list(i))

t = list(range(nElements))
n= len(t)
m = math.ceil((n-1)/2 + 1)
     

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

def u(s,t):                           #Unsettled symbols
    u = []
    for i in range(n):
        if s[i] != t[i]:
            u.append(s[i])
    return u        
#print(u(s,t)) 

def ull(s,t):                            # ULL,URR,ULR,URL guys

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

#def Potential(s,t):                # Give the potential number of a source with respect to destination

# return 2*(len(ull(s,t)) + len(urr(s,t))) + (len(ulr(s,t)) + len(url(s,t))) + len(NoOfCycles(s,t))
#print(Potential(s,t))

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

#print(EvenPermutation(s,t)) 

def swap(s,i):  
    newlist=[s[i]]
    newlist.extend(s[1:i])
    newlist.append(s[0])
    newlist.extend(s[i+1:])
    return newlist

def number_of_hops_in_undirected_star_graph(s,t):
    
    count = 0
    while s != t:   #routing proccess
            
        if s[0] != t[0]:  #case 2
            s= swap(s,t.index(s[0]))
            count +=1 
        else:
            for i in range(1,n):
                if s[i] != t[i]:
                   s = swap(s,s.index(s[i]))
                   break
            count += 1
                   

    return count            

def the_ull_symbol(s,t):     # The symbol which is not in the same cycle as s[0]
        first_symbol = s[0]
        the_cycle = None
        for c in cycle(s,t):
            if first_symbol in c:
                the_cycle = c
                break

        k = []
        for element in ull(s,t):
            if element not in c:
                k.append(element)
                break
        return k 
#print(the_ull_symbol(s,t))

def the_urr_symbol(s,t):     # The symbol which is not in the same cycle as s[0]
    first_symbol = s[0]
    the_cycle = None
    for c in cycle(s,t):
        if first_symbol in c:
            the_cycle = c
            break

    k = []
    for element in urr(s,t):
        if element not in c:
            k.append(element)
            break
    return k 
#print(the_urr_symbol(s,t))

def the_ulr_symbol(s,t):     # The symbol which is not in the same cycle as s[0]
        first_symbol = s[0]
        the_cycle = None
        for c in cycle(s,t):
            if first_symbol in c:
                the_cycle = c
                break

        k = []
        for element in ulr(s,t):
            if element not in c:
                k.append(element)
                break
        return k

def the_url_symbol(s,t):     # The symbol which is not in the same cycle as s[0]
        first_symbol = s[0]
        the_cycle = None
        for c in cycle(s,t):
            if first_symbol in c:
                the_cycle = c
                break

        k = []
        for element in url(s,t):
            if element not in c:
                k.append(element)
                break
        return k  

def next_swap(s,t):
        if EvenPermutation(s,t) is True:
            d=[]
            if s == t:
                print("Percel reached it's destination")
            # elif s[0] == t[0]:
            #     if len(ull(s,t) > 0):
            #         d=swap(s,s.index(ull(s,t)[0]))

            elif s[0] in l(t):                                                       # A problem
                d=swap(s,t.index(s[0]))    # Settling Move
            elif s[0] == t[0] or s[0] not in l(t):          # s[0] == t[0] or s[0] is in r(t)

                if len(ull(s,t)) > 0:       # 3a
                    if len(the_ull_symbol(s,t))>0:
                        d=swap(s,s.index(the_ull_symbol(s,t)[0]))
                    else:
                        d=swap(s,s.index(ull(s,t)[0]))

                elif len(ull(s,t)) == 0 and len(ulr(s,t)) > 0:  #3b
                    if len(the_ulr_symbol(s,t)) > 0:
                        d=swap(s,s.index(the_ulr_symbol(s,t)[0]))
                    else:    
                        d=swap(s,s.index(ulr(s,t)[0]))
                elif t[0] in l(s):
                    d = swap(s,s.index(t[0]))
                else:
                    d=swap(s,s.index(l(s)[0]))    #3c

            else:
                return
            return d        

        else:
            d=[]
            if s == t:
                print("Percel reached it's destination")
            elif s[0] in r(t):
                d=swap(s,t.index(s[0]))    # Settling Move
            elif s[0] not in r(t):          # s[0] == t[0] or s[0] is in l(t)

                if len(urr(s,t)) > 0:       # 3a
                    if len(the_urr_symbol(s,t)) > 0:
                        d=swap(s,s.index(the_urr_symbol(s,t)[0]))
                    else:
                        d=swap(s,s.index(urr(s,t)[0]))

                elif len(urr(s,t)) == 0 and len(url(s,t)) > 0:  #3b
                    if len(the_url_symbol(s,t)) > 0:
                        d=swap(s,s.index(the_url_symbol(s,t)[0]))
                    else:
                        d=swap(s,s.index(url(s,t)[0]))
                elif t[0] in r(s):
                    d = swap(s,s.index(t[0]))
                else:
                    d=swap(s,s.index(r(s)[0]))    #3c

            else:
                return
            return d

def No_of_hop_to_reach_destination(s,t):
        count_steps = 0
        while s!= t:
            s=next_swap(s,t)
            count_steps +=1
        return count_steps        
def ratio_of_step_count_btn_directed_and_undirected(s,t):
    if number_of_hops_in_undirected_star_graph(s,t) == 0:
       return 0
    else:
       return No_of_hop_to_reach_destination(s,t)/ number_of_hops_in_undirected_star_graph(s,t)
    
def step_comparing_b2n_two_cases(s,t):
    if No_of_hop_to_reach_destination(s,t) <= 2*number_of_hops_in_undirected_star_graph(s,t) + 3:
        return 0
    else:
        return 1
def step_comparing_b2n_two_cases_2(s,t):
    if No_of_hop_to_reach_destination(s,t) <= 2*number_of_hops_in_undirected_star_graph(s,t) + 4:
        return 0
    else:
        return 1 
           

f = open("9.csv", "w")
print("s", "Even-Permutation", "ull", "urr", "ulr", "url", "ListOfCycle", "d", "d_vector", "d_vec <= 2*d + 3", "d_vec <= 2*d + 4", sep = "\t", file = f)
for s in S:  

    print(s, EvenPermutation(s,t), len(ull(s,t)), len(urr(s,t)), len(ulr(s,t)), len(url(s,t)), len(ListOfCycles(s,t)), number_of_hops_in_undirected_star_graph(s,t), No_of_hop_to_reach_destination(s,t), step_comparing_b2n_two_cases(s,t), step_comparing_b2n_two_cases_2(s,t), sep = "\t", file = f)        

end = time.time()
print("t = ", end - start)













