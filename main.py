#main.py
questions= ("Q1. How do you insert COMMENTS in Python code?: ",
            "Q2. How do you create a list in Python?: ",
            "Q3. Who developed Python Programming Language?: ",
            "Q4. Which type of Programming does Python support?: ",
            "Q5. Which of the following is the correct extension of the Python file?: ",
            "Q6. Which keyword is used for function in Python language?:  ",
            "Q7. Which of the following is the truncation division operator in Python?: ",
            "Q8. What will be the output of the following Python code? x='abcd'"
                 "for i in x:"
                 "print(i.upper()) : ",
            "Q9. Which one of the following is not a keyword in Python language?: ",
            "Q10. Which of the following is a Python tuple?: ",
            "Q11. Which of these in not a core data type?: ",
            "Q12. Select all options that print----  hello-how-are-you . ",
            "Q13. What will be the output of the following Python code?----print (''abc DEF''.capatalize()) : ",
            "Q14. What will be the output of the following Python expression?    round(4.576): ",
            "Q15. A while loop in Python is used for what type of iteration?: ",
            "Q16. Which one is NOT a legal variable name?: ",
            "Q17. Which method can be used to return a string in upper case letters?: ",
            "Q18. Which method can be used to replace parts of a string?: ",
            "Q19. Which collection does not allow duplicate members?: ",
            "Q20. How do you start writing an if statement in Python?: ")

options =(  ("A. $ ","B. comments","C. # ","D. * "),
            ("A. By enclosing items in square brackets [] ","B. By using parentheses () ","C. By using curly braces {}","D. By using angle brackets <> "),
            ("A. Wick van Rossum ","B. Rasmus Lerdorf ","C. Ayaan Masood","D. Guido van Rossum"),
            ("A. structured programming ","B. object-oriented programming ","C. functional programming ","D. all of the mentioned "),
            ("A. (.python) ","B. (.py) ","C. (.p) ","D. (ide) "),
            ("A. Function ","B. int ","C. main ","D. def "),
            ("A. - ","B. % ","C. // ","D. / "),
            ("A. abcd ","B. ABcD ","C. ABCD ","D. all of the above "),
            ("A. pass","B. eval ","C. assert ","D. nonlocal "),
            ("A. {11,32,3} ","B. [1,2,3] ","C. (1,5,7) ","D. {} "),
            ("A. Lists ","B. Tuples ","C. Dictionary ","D. Class "),
            ("A. print(‘hello’, ‘how’, ‘are’, ‘you’) ","B. print(‘hello-‘ + ‘how-are-you’) ","C. print(‘hello’ + ‘-‘ + ‘how’ + ‘-‘ + ‘are’ + ‘you’) ","D. print(‘hello’, ‘how’, ‘are’, ‘you’ + ‘-‘ * 4)"),
            ("A. abc def ","B. ABC DEF ","C. Abc Def","D. Abc def "),
            ("A. 5 ","B. 4.6 ","C. 4 ","D. 4.5 "),
            ("A. discriminant ","B. indefinite ","C. definite","D. indeterminate"),
            ("A. _myvar ","B. my-var ","C. Myvar ","D. my_var"),
            ("A. upperCase() ","B. toUpperCase() ","C. uppercase() ","D. upper() "),
            ("A. switch() ","B. repl() ","C. replaceString() ","D. replace() "),
            ("A. SET ","B. List ","C. Tuple ","D. String "),
            ("A. if(x>y) ","B. if x>y: ","C. if x>y then ","D. (x>y)if "))

answers = ("C","A","D","B","B","D","C","A","B","C","D","B","D","A","B","B","D","D","A","B")
guesses=[]
score = 0
question_num = 0

for question in questions:
         print("----------------------------------------------------------------")
         print("----------------------------------------------------------------")
         print(question)

         for option in options[question_num]:

             print(option)
         print("----------------------------------------------------------------")
         print("----------------------------------------------------------------")
         guess = input("                   YOUR ANSWER : ").upper()
         guesses.append(guess)
         if guess == answers[question_num]:
             score+=1
             print("CORRECT")
         else:
             print("INCORRECT")
             print(f"{answers[question_num]}  is the correct answer")
         question_num += 1


print("-------------------------------------")
print("             RESULT                  ")
print("-------------------------------------")

print(" correct answers: ",end="")
for answer in answers:
    print(answer,end=" ")
print()

print(" your guesses: ",end="")
for guess in guesses:
    print(guess,end=" ,")
print()

score=score/len(questions)*100
print(f"your score is:{score}%")
print("-----------------------------------------------------------------------------------------------------------------------------------------------")




