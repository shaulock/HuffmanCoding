from imports import isfile

# This function will get the file path from user and confirm that the file exists
# return type -> str
def get_file_path() -> str:
    """
    Anyone can exit the program if they press ctrl + C, 
    so instead of printing an error message, we will print a custom message
    """
    try:

        path = input("Enter the path to the file : ")
        # the isfile function returns True if a file exists, else it returns False, 
        # we will ask the user to try again when it returns false
        if isfile(path):
            # since it was a real file, we will just return the path
            return path
        else:
            # it wasn't a real file, so we print a custom message and then recursively call our function again
            print("File Does Not Exist! Try Again...")
            return get_file_path()

    except KeyboardInterrupt:
        print("OK. Bye.")
        exit(0)

# This function will get the string from file
# return type -> str
def get_string() -> str:
    # Using the function we made to get the file
    file = get_file_path()
    # using with open, so we don't have to worry about closing the file
    with open(file, 'r') as f:
        # Returning the string that we read
        return f.read()

# This function will send the string from the file to the caller function
# Return type -> str
def read() -> str:
    return get_string()