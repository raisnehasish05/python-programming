x=eval(input("enter a list: "))
print("Existing list is",x)
n=int(input("Enter a number"))
for i in range(len(x)):
  x[i]+=n
print("updated list",x)
