# Problème 1 jour 1

#if __name__=='__main__':
  #  f = open("day 1.txt", "r")
# data = f.read().split("\n")
# dataInt=[]
#Technique 1 : list Comprehension
    #  data = [ int(d) for d in data ]


#Technique 2 : i est un compteur
# for i in range (0, len(data)):
# data[i]=int(data[i])

#Technique 3 : d est un iterateur
#    for d in data :
#       dataInt.append(int(d))

# print(data)

#cpt = 0
#for i in range(0, len(data)-1):
# n1 = data[i]
# n2 = data[i+1]


    #if n1<n2:
#   cpt = cpt + 1

#  print(cpt)


# Problème 2 jour 1

if __name__=='__main__':
    f = open("day 1.txt", "r")
    data = f.read().split("\n")
    dataInt=[]

cpt = 0
for i in range (0, len(data)-3):
    n1 = int(data[i])
    n2 = int(data[i+1])
    n3 = int(data[i+2])
    n4 = int(data[i+3])
    if (n1 + n2 + n3) < (n2 + n3 + n4):
        cpt = cpt + 1

print(cpt)