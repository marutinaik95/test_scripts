# read the number elements to be stored in list
n = int(input("Enter the number elements : "))
num_list = []
for num in range(0,n):
    elements = int(input("Enter the elements : "))
    num_list.append(elements)
average_of_list = sum(num_list)/n
print("average of elements in list : ",average_of_list)