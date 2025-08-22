# File: file_handling_assignment.py

def read_and_write_file():
    """
    Reads an input file and writes a modified version to a new file.
    Example: Converts text to uppercase and adds line numbers.
    """
    try:
        # Prompt user for input filename
        input_filename = input("Enter the name of the file to read: ").strip()

        # Open and read the file
        with open(input_filename, 'r', encoding='utf-8') as infile:
            lines = infile.readlines()

        # Modify content (e.g., convert to uppercase and add line numbers)
        modified_lines = []
        for i, line in enumerate(lines, 1):
            modified_line = f"{i}: {line.strip().upper()}\n"
            modified_lines.append(modified_line)

        # Write to a new file
        output_filename = "modified_" + input_filename
        with open(output_filename, 'w', encoding='utf-8') as outfile:
            outfile.writelines(modified_lines)

        print(f"✅ Successfully created '{output_filename}' with modified content.")

    except FileNotFoundError:
        print(f"❌ Error: The file '{input_filename}' was not found.")
    except PermissionError:
        print(f"❌ Error: You don't have permission to read '{input_filename}'.")
    except IsADirectoryError:
        print(f"❌ Error: '{input_filename}' is a directory, not a file.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")


def main():
    """
    Main function to run the assignment.
    """
    print("📂 File Handling and Exception Handling Assignment\n")
    read_and_write_file()


if __name__ == "__main__":
    main()
