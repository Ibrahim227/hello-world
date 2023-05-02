import time


name = input("Please enter your name: ")
great = f"\tHello {name} ! \n"
msg = "Welcome to my Github profile !"
end_msg = "\t Good Bye \n"
# print great and msg
print(great, msg)
time.sleep(1) # wait for 0.7s before displaying the remain message

print("#########################################")
print("# First Name: Maman Sani                #")
print("# Last Name: Ibrahim                    #")
print("# Email: mamansani.ibrahim01@gmail.com  #")
print("# Status : Student | Python Entusiast   #")
print("#########################################")

time.sleep(1) # wait for 1s before displaying the end message
print(f"{end_msg}")
