def read_and_modify_file(input_filename, output_filename):
    try:
        # Open the input file in read mode
        with open(input_filename, 'r') as file:
            # Read the content of the file
            content = file.read()
            
            # Modify the content (For example, converting all text to uppercase)
            modified_content = content.upper()

        # Open the output file in write mode
        with open(output_filename, 'w') as file:
            # Write the modified content to the new file
            file.write(modified_content)
        print(f"Modified content has been written to '{output_filename}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except PermissionError:
        print(f"Error: You don't have permission to read or write to the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Main program
def main():
    # Ask the user for the input file name
    input_filename = input("Enter the name of the file to read: ")
    
    # Ask the user for the output file name
    output_filename = input("Enter the name of the new file to write to: ")

    # Call the function to read, modify, and write the file
    read_and_modify_file(input_filename, output_filename)

# Run the main function
if __name__ == "__main__":
    main()
