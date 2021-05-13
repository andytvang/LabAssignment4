"""
The program will allow a user three tries to guess the correct answer to the question
The question = "What is the capital of California". The answer is "Sacramento".

We first set max_tries = 3. Then create a loop to iterate three times. For each iteration,
we ask the user for the anser (user input). Then based on the answer the user gives, we check  
to see if the user input matches the anser. If so, then print "Correct!", then terminate the loop with a
break statement. 

If the user's answers are incorrect witin the max tries, we print "You have used up your allotment of guesses.",
then print 'The correct answer is California'".
"""
"""
main
    question = "What is the capital of California"
    answer = "California"
    ask(question , answer)

ask
    tries = 0
    loop three times
        increment tries by 1
        ask user input()
        check to see of user input is equal to answer
            if so then, print "Correct" then exit the loop
    If not correct
        print to the user "You have used up your allotment of guesses".
        print the correct answer "The correct answer is 'Sacramento'".

main
"""