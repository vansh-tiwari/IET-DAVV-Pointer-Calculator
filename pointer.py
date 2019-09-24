theory, pract = map(int, input("Enter no. of theory and practical subjects in space separated integers('Do not count CV and extra subject)\n").split())

# theories = ['maths','ooad','web','toc','network']
# practs = ['ooad','web','toc']

sum = 0
for x in range(1, theory+1):
    sum = sum + (int(input("Theory subject {}: ".format(x))) * 4)

for x in range(1, pract+1):
    sum = sum + (int(input("Practical subject {}: ".format(x))) * 1)

sum = sum + int(input("Extra subject: "))*2
sum = sum + int(input("CV: "))*4

print(sum/30)