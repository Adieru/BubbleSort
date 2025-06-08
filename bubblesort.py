#Declaring array
arr = [1,5,7,8,11,23]

#Lenght of the array
len_arr = len(arr)

#The bubble sort loop
for i in range(len_arr - 1):
    for j in range(len_arr - 1 - i):
        
        #Sorting descending order
        if(arr[j] < arr[j + 1]):
            arr[j],arr[j+1] = arr[j+1], arr[j]
            
print(arr)
        
        
