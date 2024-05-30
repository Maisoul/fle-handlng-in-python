# file_handling_assignment.py

# File Creation and Writing
try:
    with open("my_file.txt", 'w') as file:
        file.write("Hello, this is the first line.\n")
        file.write("This is the second line with a number: 12345.\n")
        file.write("Third line, another string with a number: 67890.\n")
    print("File created and initial content written successfully.")
except (FileNotFoundError, PermissionError) as e:
    print(f"An error occurred while creating/writing the file: {e}")

# File Reading and Display
try:
    with open("my_file.txt", 'r') as file:
        content = file.read()
    print("\nFile contents after initial writing:")
    print(content)
except (FileNotFoundError, PermissionError) as e:
    print(f"An error occurred while reading the file: {e}")

# File Appending
try:
    with open("my_file.txt", 'a') as file:
        file.write("This is the fourth line, appended to the file.\n")
        file.write("Fifth line, with some text and number: 54321.\n")
        file.write("Sixth line, yet another string with a number: 98765.\n")
    print("Additional content appended successfully.")
except (FileNotFoundError, PermissionError) as e:
    print(f"An error occurred while appending to the file: {e}")

# File Reading and Display after Appending
try:
    with open("my_file.txt", 'r') as file:
        content = file.read()
    print("\nFile contents after appending:")
    print(content)
except (FileNotFoundError, PermissionError) as e:
    print(f"An error occurred while reading the file: {e}")

# Using finally to ensure resources are cleaned up
finally:
    print("\nFile handling operations completed.")
