# Assignment 1 - Basic Python
# ---------------------------------------------------------
# Question 1:
# Explain the difference between the following data types
# with examples:
# Integer (int)
# Float (float)
# String (str)
# Boolean (bool)

# Answer:
# Integer (int):
# Stores whole numbers without decimal points
# Example: 10, -5, 100

# Float (float):
# Stores numbers with decimal points
# Example: 10.5, 3.14, -2.7

# String (str):
# Stores text enclosed in single or double quotes
# Example: "Hello", 'Python'

# Boolean (bool):
# Stores only two values: True or False
# Example: True, False

# ---------------------------------------------------------
# Question 2:
# Write a Python program to create three variables:
# name, age, city
# Store your details in them and print the values.

name = "Lucky"
age = 21
city = "Jaipur"

print("Name:", name)
print("Age:", age)
print("City:", city)

# ---------------------------------------------------------
# Question 3:
# Write a Python program that:
# Takes a user's name as input.
# Prints the name in uppercase.
# Prints the total number of characters in the name.

name = input("Enter your name: ")

print("Uppercase Name:", name.upper())
print("Total Characters:", len(name))

# ---------------------------------------------------------
# Question 4:
# Explain any five commonly used string methods in Python
# with examples.

# Answer:
# 1. upper()
# Converts all characters to uppercase
# Example:
# "python".upper() -> "PYTHON"

# 2. lower()
# Converts all characters to lowercase
# Example:
# "PYTHON".lower() -> "python"

# 3. title()
# Converts the first letter of each word to uppercase
# Example:
# "hello world".title() -> "Hello World"

# 4. replace()
# Replaces a specified word or character
# Example:
# "I like Java".replace("Java", "Python")
# Output: "I like Python"

# 5. len()
# Returns the total number of characters in a string
# Example:
# len("Python")
# Output: 6

# ---------------------------------------------------------
# Question 5:
# Create a list containing the names of five fruits.
# Print the complete list.
# Print the first and last element.
# Print the total number of items in the list.

fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes"]

print("Complete List:", fruits)
print("First Element:", fruits[0])
print("Last Element:", fruits[-1])
print("Total Items:", len(fruits))


# ---------------------------------------------------------
# Question 6:
# Create a list of numbers [10, 20, 30, 40, 50]
# Add 60 to the list.
# Remove 20 from the list.
# Print the updated list.

numbers = [10, 20, 30, 40, 50]

numbers.append(60)
numbers.remove(20)

print("Updated List:", numbers)

# ---------------------------------------------------------
# Question 7:
# What is Artificial Intelligence (AI)?
# Explain its importance and mention any four real-life
# applications of AI.

# Answer:
# Artificial Intelligence (AI) is a technology that enables
# machines and computers to perform tasks that normally
# require human intelligence, such as learning, reasoning,
# decision-making, and problem-solving

# Importance of AI:
#  Saves time and increases efficiency
#  Automates repetitive tasks
# Improves decision-making using data
# Enhances user experience

# Four real-life applications of AI:
#  ChatGPT and chatbots
#  Voice assistants (Alexa, Siri, Google Assistant)
#  Recommendation systems (Netflix, YouTube)
#  Google Maps route prediction

# ---------------------------------------------------------
# Question 8:
# Identify whether the following are examples of AI and
# explain why.

# ChatGPT:
# Yes, it is an AI application because it understands and
# generates human-like text

# Google Maps Route Prediction:
# Yes, it uses AI to analyze traffic patterns and suggest
# the best routes

# Calculator:
# No, it is not AI because it follows fixed mathematical
# rules and does not learn from data

# Netflix Recommendations:
# Yes, it uses AI to analyze user preferences and suggest
# movies and shows
# Voice Assistants (Alexa/Siri):
# Yes, they use AI to understand voice commands and
# respond intelligently