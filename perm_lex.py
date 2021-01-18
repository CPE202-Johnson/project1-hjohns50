def perm_gen_lex(a): 
    if len(a) <= 1: #returns a singular character 
         return [a]
    perm_lst = []
    for i in range(len(a)):
        char = a[i]
        perm = perm_gen_lex(a[:i] + a[i+1:])
        for p in range(len(a)-1):
            if p == 0:
                put = char + perm[p]
                perm.insert(p, put)
                perm_lst.append(perm[p])
            else:
                put = char + perm[p+1]
                perm.insert(p, put)
                perm_lst.append(perm[p])
    return perm_lst