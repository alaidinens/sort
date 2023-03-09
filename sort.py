length= int(input("Length of the word that you are interested: "))
symbols = "0123456789!'()*+,-./:;-<=>?@[\]^_`{|}~"

with open('pelekapasaka.txt', 'r', encoding='utf-8') as f:
    ff = f.readlines()
ff = [new_f.replace( '!', '') for new_f in ff]

for word in sorted(ff):
    space = word.split()
    print(space)

qnt = []

for i in ff:
    #ranges = [range(f[i], f[i-1], 1)]
    for j in range(0, len(ff)):
        if j == length:
        #for j in ff[i]:
            #ff.sort(key = lambda length:len(length))
            qnt.append(i)
        print(qnt)
    
    
    
    

    #for j in ff[i]:
    #    if len(j)==length:
    #        qnt.append(j)
    #   print(qnt)