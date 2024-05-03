"""f = open('example.txt','r')
f_content = f.read()
f.close()

print(f_content)"""

"""f = open('my_file.txt','w')
f.writelines(['\n wellington','\n 0726124006','\n willy@gmail.com'])
f.close()"""

"""f = open('my_file.txt','r')
f_content = f.readlines()
f.close()

print(f_content)"""

f = open('my_file.txt','a')
f.writelines(['\n john','\n 0708345367','\n jon@gmail.com'])
f.close()

f_object = open('my_file.txt','r')
f_content = f_object.read()
f_object.close()

print(f_content)

try:
      with open("my_file.txt", "w") as file:
            file.write("Hello, this is line 1.\n")
            file.write("12345 is a number.\n")
            file.write("This is line 3 with some special characters: !@#$%^&*\n")
except FileNotFoundError:
        print("File not found or cannot be created.")
except PermissionError:
        print("Permission denied to create or write to the file.")
else:
        print("File 'my_file.txt' created successfully.")