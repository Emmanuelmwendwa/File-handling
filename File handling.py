def create_file():
    try:
        # Create a new text file in write mode
        with open("my_file.txt", "w") as file:
            # Write at least three lines of text to the file
            file.write("Hello, this is line 1.\n")
            file.write("12345\n")
            file.write("Line 3: End of writing.\n")
    except PermissionError:
        print("Permission denied to create file.")
    except Exception as e:
        print(f"An error occurred: {e}")
    else:
        print("File created successfully.")

def read_file():
    try:
        # Open the file in read mode
        with open("my_file.txt", "r") as file:
            # Read and display the contents of the file
            print("Content of my_file.txt:")
            print(file.read())
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def append_file():
    try:
        # Open the file in append mode
        with open("my_file.txt", "a") as file:
            # Append three additional lines of text
            file.write("This is a new line appended.\n")
            file.write("Another appended line.\n")
            file.write("Final line appended.\n")
    except PermissionError:
        print("Permission denied to append to file.")
    except Exception as e:
        print(f"An error occurred: {e}")
    else:
        print("Content appended successfully.")

if __name__ == "__main__":
    create_file()  # Create a new file
    read_file()    # Read and display its contents
    append_file()  # Append additional lines to the file
