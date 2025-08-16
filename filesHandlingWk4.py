try:
    with open("emple.txt","r") as file:
        # file.write("Melichizedek is not a good boy")
        print(file.read())
except:
    FileNotFoundError
    print("The file does not exist. Rename it correctly!!")

# with open("example.txt","r"):
#     print(file.read())
    

