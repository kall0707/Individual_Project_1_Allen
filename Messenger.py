import os

name = "Kyra Allen"

file_name = input("Enter a messenger file name: ")

if os.path.exists(file_name):
    print("\n--- Contents of '{file_name}' ---")
    with open(file_name, "r") as file:
        print(file.read())
    print("---------------------------\n")
else:
    print("File '{file_name}' not found. Creating a new file...")
    with open(file_name, "w") as file:
        pass
    
user_message = input("Enter your message: ")

formatted_message = f"[{name}]: {user_message}\n"

with open(file_name, "a") as file:
    file.write(formatted_message)
    
print("Your message has been saved to '{file_name}'!")