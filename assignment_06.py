user_data:list = []
while True:
    user_input = input("Please enter the student's name (or type 'stop' to finish):")
    if user_input.lower() == "stop":
        break
    
    # Check for duplicate names
    if any(name[1] == user_input for name in user_data):
        print(f"{user_input} is already in the list.")
        continue
    
    # Add the name to the list with an incremented index
    info = (len(user_data) + 1, user_input)
    user_data.append(info)

# Display the final list
print("Complete List of Students (Tuples):")
for index, data in enumerate(user_data, start=1):
    print(f"{data}", end=" ")


print("\nList of Students with IDs:")
for id, name in enumerate(user_data, start=1):
  print(f"ID: {id}, Name:{name}")