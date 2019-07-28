#Request a name of the file
file_name = input("Enter file name: ")

#Read the inputted file
handle = open(file_name,'r')

myList = list()
#display the content line by line with while loop
for lines in handle:
    print(lines)
    #for line in lines:
    myList.append(lines)



print(myList)

#save the line into list by using append function





