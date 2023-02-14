num_student = int(input("How many students are registering: "))   # Ask user how many students are registering

for i in range(num_student):                     # repeat the question based on the number of student registering
    id = int(input("Enter id number: "))         # ask the user for the id numbers
    i += 1
    register = open("reg_form.txt","r+")         # Open the text file
    register.write(f"{id} \n")                   # Write the id numbers on the text file
    register.readline()                          # Read the text file line

register.close                               # Close the text file