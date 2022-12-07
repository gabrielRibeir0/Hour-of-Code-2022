print("Hello World!")

nome = "Gabriel"
sobremome = "Ribeiro"
print("Hello " + nome + " " + sobremome)

#----------------------
pi = 3.14
n1 = 6 
n2 = 2

print(n1 + n2) #soma
print(n1 * n2) #multiplicação
print(n1 ** n2) #exponenciação
print(n1 / n2) #divisão
print(n1 // n2) #divisão inteira

print(str(n1) + " Hello World")
print(int("10"))

#--------------------
names = ["Daniel","Pedro","Joaquim"]
names[0] = "Carlos"
print(names)
print(names[0] + " " + names[1] + " " + names[2])

names.append("Daniel")
print(names)

names.insert(1,"João")
print(names)

names.remove("Pedro")
print(names)

#------------------------
price = 3
if price >= 1:
  tax = 0.2
else:
  tax = 0
print(tax)

produto = "phone"
if produto == "food":
  tax = 0.05
elif produto == "phone":
  tax = 0.25
elif produto == "clothes":
  tax = 0.10

#-------------------
for name in ["Daniel", "Pedro", "Joaquim"]:
  print(name)

objects = ["phone", "desk", "tv"]
for i in range(len(objects)):
  print(objects[i])

i = 0
while(i < len(objects)):
  print(objects[i])
  i = i + 1

#-------------------------

def sum_numbers(n1,n2):
  return n1 + n2

print(sum_numbers(2,4))
print(sum_numbers(2,2) + sum_numbers(4,4))