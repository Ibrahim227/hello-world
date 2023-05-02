import time #time module


name = input("Please enter your name: ")    # Ask the user for his/her name
great = f"\tHello {name} ! \n"
msg = "Welcome to my Github profile !"
end_msg = "\t Good Bye \n"

# print great and msg
print(great, msg)
time.sleep(1.5) # wait for 1.5s before displaying the remain message

#multiple print function
print("#########################################")
print("# First Name: Maman Sani                #")
print("# Last Name: Ibrahim                    #")
print("# Contact : +227 93325219               #")
print("# Email: mamansani.ibrahim01@gmail.com  #")
print("# Status : Student | Python Entusiast   #")
print("#########################################")

time.sleep(1) # wait for 1s before displaying the end message
print(f"{end_msg}")
