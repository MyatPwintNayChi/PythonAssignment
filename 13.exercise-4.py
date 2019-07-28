# Create a function that return the largest number in the list


def get_largest_number(input):
    

    largest_number = 0
  
    for number in input:
        
     
        if number >= largest_number:
            largest_number = number
            
            
        

    return largest_number
     
result = get_largest_number([201,92,150,100,200])
print(result)



