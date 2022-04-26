import re
def oneHot(n):
    m = {}

    for i in range(n):
        nl = [0 for i in range(n)]
        nl[i] = 1
        m[i] = nl
    return m

def reg(l):
    d = []
    for i in l:
        d += [re.sub('[\W_]+', '', i)]
    print(d)

    r = list(filter(('').__ne__, d))

    return r


def  windowOneHot(m , n):
    fl = []

    for i in range(n):
        nl = []
        nl += [m[i]]
        ml = []
        if i==0:
            for j in range(i+1 , i+k+1):
               ml += [m[j]]
            nl += [ml]
        elif i==n-1:
            for j in range(n-2 , (n-1)-k-1 , -1):
                ml += [m[j]]
            nl += [ml[ : : -1]]
        else:
            q = i-1
            w = i+1
            ic = 0
            jc = 0
            while q>=0 and ic<k:
                ml += [m[q]]
                q -= 1
                ic += 1
            ml = ml[ : : -1]

            print(ml , j)
            while w<=n-1 and jc<k:
                ml += [m[w]]
                w += 1
                jc += 1
            print(ml)

            nl += [ml]

        fl += [nl]

    return fl


def finalList(f):
    fl = []

    for i in f:
        nl = []
        nl += [i[0]]
        n = len(i[1][0])
        l = []
        for j in range(n):
            d = 0
            for k in i[1]:
                d = d or k[j]
            l += [d]
        nl += [l]
        fl += [nl]

    return fl


s = input("Enter Sentence : ").strip()
k = int(input("Enter Window Size : "))
l = s.split()


d = reg(l)  #REMOVING EVERYTING EXCEPT LETTERS FROM WORDS
print(l , d)


n = len(d)
m = oneHot(n)   #ONE HOT ENCODING OF THE SENTENCE
print(m)


f = windowOneHot(m , n) #ONE HOT WITH WINDOW SPACE
print(f)


fl = finalList(f)   #ONE HOT WITH MERGED WINDOW SPACE
print(fl)
