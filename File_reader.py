def modify_content(text):
    """
    A simple function that modifies the file content.
    Here, we'll convert everything to uppercase as an example.
    You can change this logic if needed.
    """
    return text.upper()


def main():
    # Ask the user for the input file name
    input_file = input("Enter the name of the file to read: ")

    try:
        # Try opening and reading the file
        with open(input_file, "r") as f:
            content = f.read()

        # Modify the content
        modified_content = modify_content(content)

        # Create a new file name for the modified content
        output_file = "modified_" + input_file

        # Write the modified content to the new file
        with open(output_file, "w") as f:
            f.write(modified_content)

        print(f"Modified content has been written to {output_file}")

    except FileNotFoundError:
        print("Error: The file you entered does not exist. Please try again.")
    except PermissionError:
        print("Error: You don’t have permission to read this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
