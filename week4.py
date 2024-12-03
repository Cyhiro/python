def file_read_write():
    try:
        # Ask the user for the input filename
        input_filename = input("Enter the name of the file to read: ").strip()
        
        # Attempt to open the file in read mode
        with open(input_filename, "r") as input_file:
            content = input_file.read()
        
        # Modify the content (example: convert to uppercase)
        modified_content = content.upper()
        
        # Ask the user for the output filename
        output_filename = input("Enter the name of the new file to write: ").strip()
        
        # Write the modified content to the new file
        with open(output_filename, "w") as output_file:
            output_file.write(modified_content)
        
        print(f"Content successfully modified and written to '{output_filename}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except PermissionError:
        print(f"Error: You do not have permission to read or write to one of the files.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the program
file_read_write()
