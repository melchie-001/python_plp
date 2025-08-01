"""
. Personalized Greeting App 👋
Create a program that asks for the user’s name and favorite color, then prints a personalized greeting like: “Hello, [Name]! Your favorite color, [Color], is awesome!”
2. Simple Quiz Game 🎮
Create a multiple-choice quiz with questions about Python, movies, or any fun topic! Display scores at the end and allow the user to play again. 🏆
3. Random Joke Generator 🤣
Build a program that stores a list of jokes and randomly selects one to display every time the user runs it. Add a fun twist with jokes about Python or programming! 🐍💡
"""
#Greeting App

# Store the user's name and favorite color in variables
name="Melichizedek"
favourite_color="Blue"

# Display a personalized greeting using f-string formatting
print(f"Hello, {name}! Your favorite color, {favourite_color}, is awesome!")

# Simple Quiz Game

# Initialize the user's score
score=0

# Dictionary containing quiz questions and their correct answers
questions={"Your best meal:\n(a).Ugali\n(b).Nyama\n(c).Sukuma":"a",
           "Your Best Phone: \n(a).Samsung \n(b).Nokia\n(c).Itel":"b",
           "You best laptop\n(a).HP\n(b).Dell\n(c).Lenovo":"c"}

# Loop through each question and its correct answer
for question, answer in questions.items():
    user_ans=input(question +"\nYour Answer:").lower()

 # Ask the user to answer each question and convert it to lowercase
    if answer==user_ans:
        print("Correct answer")
        score+=1
 # Check if the user's answer is correct
    else:
        print("❌Wrong Answer")
# Show the user's final score
print(f"You got {score} out of {len(questions)}")

#Random Joke Generator
import random# Import Python's built-in random module

# Create a list of fun facts or personal details
details=["my name is Melichizedek", "I am a boy", "I am a comrade at Meru University","I am God fearing"]

# Display one random detail from the list
print("Random details= ")
print(random.choice(details))# Picks and displays a random element from the list



