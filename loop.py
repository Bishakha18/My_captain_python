 
n=int(input("enter the range of list: "))
 # take a list of inputs and gives out only positive no. in the list
arr = []
for i in range(n):
        s= int(input("enter the  list: "))
        arr.append(s)
        
print("Input list is:",arr)
lists=[]
for i in range(n):
    if arr[i]>0:
        lists.append(arr[i])
        
print(f"positive list is {lists}")

