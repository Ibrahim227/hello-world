import time #time module


name = input("Please enter your name: ")    # Ask the user for his/her name
last_name = input("Please enter your Last Name:")
numb = input("enter your number: ")
email: input("Enter your email:")
status: input("Enter your status:")

great = f"\tHello {name} ! \n"
msg = "Welcome to my Github profile !"
end_msg = "\t Good Bye \n"

# print great and msg 
print(great, msg)
time.sleep(1.5) # wait for 1.5s before displaying the remain message

#multiple print function
print("#########################################")
print(f"# First Name: {name}                   #")
print(f"# Last Name: {last_name}               #")
print(f"# Contact : {numb}                     #")
print(f"# Email: {email}                       #")
print(f"# Status : {status}                    #")
print("#########################################")

time.sleep(1) # wait for 1s before displaying the end message
print(f"{end_msg}")
