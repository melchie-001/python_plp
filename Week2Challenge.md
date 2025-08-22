# 🧠 Python Data Structure Projects for Beginners

This collection of mini-projects helps you practice Python’s most essential data structures: lists, tuples, dictionaries, sets, and list comprehensions. Each task is interactive and designed to build your confidence with real-world logic.

---

## 1. 📋 List Input and Sum Calculator

**Objective:**  
Write a program that accepts user input to create a list of integers. Then, compute and display the sum of all the integers in the list.

**Skills Practiced:**  
- User input  
- List creation  
- Looping or `sum()` function

**Extension Ideas:**  
- Validate input to ensure only integers are added  
- Display the average or maximum value  
- Allow the user to add numbers until they type "done"

  **Explanation**
1. input() gets a string from the user.
2. split() breaks it into a list of strings.
3. List comprehension [int(num) for num in numbers] converts each string to an integer.
4. sum() adds them all up.

---

## 2. 📚 Tuple of Favorite Books

**Objective:**  
Create a tuple containing the names of five of your favorite books. Then, use a `for` loop to print each book name on a separate line.

**Skills Practiced:**  
- Tuples  
- Looping through sequences  
- String formatting

**Extension Ideas:**  
- Add numbering to each book  
- Ask the user to rate each book  
- Store the tuple in a file for future reference
  
**Explanation**  
1. Tuples are immutable sequences, perfect for fixed collections.  
2. The for loop iterates through each item and prints it.

---

## 3. 🧑 Dictionary for Personal Info

**Objective:**  
Write a program that uses a dictionary to store information about a person, such as their name, age, and favorite color. Ask the user for input and store the information in the dictionary. Then, print the dictionary to the console.

**Skills Practiced:**  
- Dictionaries  
- User input  
- Key-value storage

**Extension Ideas:**  
- Add more fields like hobby, location, or favorite food  
- Format the output as a mini bio  
- Save the dictionary to a JSON file
  
**Explanation**   
1. A dictionary stores key-value pairs.  
2. We assign user input to specific keys.  
3. Printing the dictionary shows all stored info.  
---

## 4. 🔗 Set Intersection Finder

**Objective:**  
Write a program that accepts user input to create two sets of integers. Then, create a new set that contains only the elements that are common to both sets.

**Skills Practiced:**  
- Sets  
- User input  
- Set operations (`intersection`)

**Extension Ideas:**  
- Display elements unique to each set  
- Use set union or difference  
- Allow repeated comparisons in a loop

**Explanation**  
1. map(int, ...) converts input strings to integers.  
2. set() removes duplicates and allows set operations.  
3. .intersection() finds shared elements.
---

## 5. ✂️ List Comprehension with Word Filter

**Objective:**  
Create a program that stores a list of words. Then, use list comprehension to create a new list that contains only the words that have an odd number of characters.

**Skills Practiced:**  
- Lists  
- List comprehension  
- String length filtering

**Extension Ideas:**  
- Ask the user to input the words  
- Display both the original and filtered lists  
- Sort the filtered list alphabetically

**Explanation**  
1. len(word) gets the length.  
2. % 2 != 0 checks if it's odd.  
3. List comprehension builds a new list based on the condition.  
---

## 🌟 Bonus Challenge

Try combining these projects into a single interactive app where the user can choose which data structure to explore. You can use a menu system and loop to keep the program running until the user exits.

---

Happy coding, Melichizedek! These projects are perfect for building foundational skills and preparing for more advanced logic and data manipulation. 🚀✨
