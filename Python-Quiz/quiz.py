print("WELCOME TO PYTHON QUIZ 🐍📚", end="\n\n")

question = (
    "Q1. What is the correct syntax to create a Python function?",
    "Q2. Which of the following data types is mutable in Python?",
    "Q3. What does the 'self' keyword represent in Python?",
    "Q4. How do you open a file in Python for writing?",
    "Q5. What is the result of '3 + 4 * 2' in Python?",
    "Q6. What is the output of the following code snippet?\n x = [1, 2, 3]\n print(x[3])",
    "Q7. What does the 'range()' function in Python return?",
    "Q8. What will be the value of 'x' after executing this code?\n x = 5\n x += 2 * 3",
    "Q9. What is the correct way to comment multiple lines in Python?",
    "Q10. Which of the following is NOT a valid way to create a Python list?"
)

options = [
    ("def my_function()", "function myFunction()", "define my_function()", "func my_function()", "make_function()"),
    ("Integer", "String", "Tuple", "List", "Dictionary"),
    ("A reference to the current instance of the class", "A keyword for static methods", "A variable representing the current method", "A reserved word for class declaration", "A keyword for inheritance"),
    ("open('file.txt', 'w')", "open('file.txt', 'r')", "open('file.txt', 'a')", "open('file.txt')", "write('file.txt')"),
    ("14", "11", "10", "Error", "None of the above"),
    ("An IndexError will be raised", "None", "3", "TypeError", "IndexError"),
    ("A list of integers", "A list of floats", "A list of strings", "A range object", "An iterator"),
    ("11", "10", "5", "6", "None of the above"),
    ("# This is a comment", "''' This is a comment '''", "/* This is a comment */", "/* This is a comment */", "// This is a comment"),
    ("[1, 2, 3]", "(1, 2, 3)", "{1, 2, 3}", "list((1, 2, 3))", "list(range(3))")
]

correctAnswer = (
    "def my_function()",
    "Tuple",
    "A reference to the current instance of the class",
    "open('file.txt', 'w')",
    "11",
    "An IndexError will be raised",
    "A range object",
    "14",
    "''' This is a comment '''",""
)


# FUNCTIONS

def CovertInput(ans):
    
    if ans == "A":
        return 0
    elif ans == "B":
        return 1
    elif ans == "C":
        return 2
    elif ans == "D":
        return 3
    else:
        print("Invalid Input")

def printOptions(option):
    index = 0
    for i in option:
        if index < 4:
            ABC = ["A","B","C","D"]
            print(ABC[index],".", i, end="\n\n")
            index += 1
    
def checkAnswer(ans, answer):
    if ans in answer:
        return True
    else:
        return False
    

def Won(x):
    if x == 9:
        print("You won the game 1CR!!!!")
        return True

def inputValid():
    while True:
        ans = input("Choose Correct Option: ").upper()
        if ans == "A" or ans == "B" or ans == "C" or ans == "D":
            return ans
            break
        
        
# MAIN CODE
correct = 0
index = 0
for i in question:
    if index < len(options):
        print(i, end="\n\n")
        printOptions(options[index])
        ans = inputValid()
        value = CovertInput(ans)
        check = checkAnswer( options[index][value], correctAnswer)
        index += 1
        if check:
            correct += 1
            if Won(correct):
                break
            print("Correct Answer🔥", "Score:", correct, end="\n\n")
        else:
            print("You LOOSE Go LEARN PYTHON, BYE BYE!!💥", "Score:", correct, end="\n\n")
            break

