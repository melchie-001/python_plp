#First challenge
# Accept user input and create a list of integers
numbers = input("Enter integers separated by spaces: ").split()
int_list = [int(num) for num in numbers]

# Compute the sum
total = sum(int_list)

print("The sum of the integers is:", total)

#Second Challenge
# Create a tuple of book names
favorite_books = ("Pilgrim's Progress", "The Bible", "Mere Christianity", "Steps to Christ", "The Great Controversy")

# Print each book on a separate line
for book in favorite_books:
    print(book)


#Third challenge
# Create an empty dictionary
person_info = {}

# Collect user input
person_info["name"] = input("Enter your name: ")
person_info["age"] = input("Enter your age: ")
person_info["favorite_color"] = input("Enter your favorite color: ")

# Print the dictionary
print("Person Information:", person_info)


#fourth challenge
# Get two sets of integers from user input
set1 = set(map(int, input("Enter integers for Set 1 (space-separated): ").split()))
set2 = set(map(int, input("Enter integers for Set 2 (space-separated): ").split()))

# Find common elements
common_elements = set1.intersection(set2)

print("Common elements:", common_elements)

#Fifth challange
# List of words
words = ["faith", "hope", "love", "joy", "peace", "kindness"]

# Filter words with odd number of characters
odd_length_words = [word for word in words if len(word) % 2 != 0]

print("Words with odd number of characters:", odd_length_words)


