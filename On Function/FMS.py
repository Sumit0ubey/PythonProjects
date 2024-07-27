# FMS: File Management System

import os


def create_file(filename):
    try:
        with open(filename, 'x') as f:
            print(f'File name {filename} - Created Successfully! ')
    except FileExistsError:
        print(f'File {filename} already exists! ')
    except Exception as E:
        print("An error occurred \n Error: ", E)


def view_files():
    files = os.listdir()
    if not files:
        print('No files in directory!')
    else:
        print("Files in directory: \n")
        for file in files:
            print(file)


def delete_file(filename):
    try:
        os.remove(filename)
        print(f'{filename} has been deleted successfully!')
    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print("An error occurred \n Error: ", e)


def read_file(filename):
    try:
        with open(filename, 'r') as f:
            contents = f.readlines()
            print(f"Content of {filename}: ")
            for content in contents:
                print(content)
            print()
    except FileNotFoundError:
        print(f'File Not Found')
    except Exception as e:
        print("An error occurred \n Error: ", e)


def edit_file(filename):
    try:
        with open(filename, 'a') as f:
            content = input('Enter data to add: ')
            f.write(content + "\n")
            print(f'Content added to {filename} successfully!')
    except FileNotFoundError:
        print(f"{filename} doesn't esists!")
    except Exception as e:
        print("An error occurred: \n Error: ", e)


def main():
    while True:
        print(" " * 10, '~ File Management App ~', " " * 10, "\n")
        print('1: Create File')
        print('2: View All Files')
        print('3: Read File')
        print('4: Edit File')
        print('5: Delete File')
        print('6: Exit')

        choice = int(input("Enter your choice [1-6] = "))

        if choice == 1:
            filename = input("Enter name of file: ")
            create_file(filename)
        elif choice == 2:
            view_files()
        elif choice == 3:
            filename = input("Enter name of file: ")
            read_file(filename)
        elif choice == 4:
            filename = input("Enter name of file: ")
            edit_file(filename)
        elif choice == 5:
            filename = input("Enter name of file: ")
            delete_file(filename)
        elif choice == 6:
            break
        else:
            print("Wrong Selection")


if __name__ == "__main__":
    main()
