theory, pract = map(int, input("Enter no. of theory and practical subjects in space separated integers('Do not count CV and extra subject)\n").split())

# theories = ['maths','ooad','web','toc','network']
# practs = ['ooad','web','toc']
g = {"f":0,"p":4,"c":5,"b":6,"b+":7,"a":8,"a+":9,"o":10}
l=[]

for x in range(1, theory+1):
    s = (str(input("Theory subject {}: ".format(x))))
    l.append(g[s]*4)
for x in range(1, pract+1):
    p1= (str(input("Practical subject {}: ".format(x))) * 1)
    l.append(g[p1]*1)
e =  str(input("Extra subject: "))
l.append(g[e]*2)
cv = str(input("CV: "))
l.append(g[cv]*4)
print(sum(l)/30)

