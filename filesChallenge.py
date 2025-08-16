'''Challenge: Create a program that reads a text file, processes its content, and writes the results to a new file.

📌 Task Requirements:
Create a file called input.txt and write at least five lines of text into it.
Write a Python script to:
Read the contents of input.txt.
Count the number of words in the file.
Convert all text to uppercase.
Write the processed text and the word count to a new file called output.txt.
Print a success message once the new file is created.'''

with open("input.txt", "w") as file:
    file.write("Write a Python script to")
    file.write("Read the contents of input.txt.")
    file.write("Count the number of words in the file.")
    file.write("Convert all text to uppercase.")
    file.write("Write the processed text and the word count to a new file called output.txt.")

with open("input.txt","r") as file:
    data=file.read()
    length=len(data.split())
    uppercase=data.upper()

with open("output.txt","w") as file:
    file.write("PROCESSED TEXT BELOW \n")
    file.write(uppercase)
    file.write(f"\n \nWordcount= {length}")
    
print("Successfully Processed, Cheers!!")
