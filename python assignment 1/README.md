# Write data to a file

assignment_text = """
Assignment 1 - Basic Python

Question 1:
Integer (int): Stores whole numbers. Example: 10, -5, 100
Float (float): Stores decimal numbers. Example: 10.5, 3.14
String (str): Stores text. Example: "Hello"
Boolean (bool): Stores True or False

Question 2:
Name: Lucky
Age: 21
City: Jaipur

Question 3:
Uppercase Name: LUCKY
Total Characters: 5

Question 4:
String Methods:
1. upper()
2. lower()
3. title()
4. replace()
5. len()

Question 5:
Fruits: Apple, Banana, Mango, Orange, Grapes

Question 6:
Updated List: [10, 30, 40, 50, 60]

Question 7:
Artificial Intelligence (AI) enables machines to perform tasks
that normally require human intelligence.

Question 8:
ChatGPT - AI
Google Maps Route Prediction - AI
Calculator - Not AI
Netflix Recommendations - AI
Voice Assistants - AI
"""

# Writing to file
with open("assignment.txt", "w") as file:
    file.write(assignment_text)

print("Data written successfully!")

# Reading from file
with open("assignment.txt", "r") as file:
    content = file.read()

print("\nFile Content:\n")
print(content)