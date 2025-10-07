# 1. Age eligibility for 18-rated movies
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to watch 18-rated movies.")
else:
    print("You are NOT eligible to watch 18-rated movies.")

# 2. Age eligibility for 18, 15, or below 15 rated films
age = int(input("\nEnter your age, we will tell you what you can watch!: "))
if age >= 18:
    print("You can watch films rated 18, 15, or below 15.")
elif age >= 15:
    print("You can watch films rated 15 or below 15.")
else:
    print("You can only watch films rated below 15.")

# 3. Suggestions based on emotion
emotion = input("\nHow are you feeling today? ")
if emotion == "happy":
    print("That's great! Keep smiling and enjoy your day.")
elif emotion == "sad":
    print("Sorry to hear that. Maybe talk to a friend or watch a funny movie.")
elif emotion == "angry":
    print("Take a deep breath. Try going for a walk to calm down.")
elif emotion == "tired":
    print("Rest is important. Consider taking a short nap.")
elif emotion == "good":
    print("Awesome! Keep up the positive vibes.")
elif emotion == "bad":
    print("Everyone has bad days. Remember, it's okay to feel this way sometimes.")
elif emotion == "homesick":
    print("It's tough being away from home. Maybe call a family member or friend after school. the time difference is 7 hours crazy!")
else :  print("Thanks for sharing. Take care of yourself!")   

# 4. Film recommendations by genre
genre = input("\nWhat genre of film do you enjoy? ").lower()
if genre == "action":
    print("Recommendations: Mad Max: Fury Road, John Wick, Die Hard")
elif genre == "comedy":
    print("Recommendations: Superbad, The Hangover, Monty Python and the Holy Grail")
elif genre == "drama":
    print("Recommendations: The Shawshank Redemption, Forrest Gump, Parasite")
elif genre == "sci-fi":
    print("Recommendations: Interstellar, Blade Runner 2049, The Matrix")
elif genre == "horror":
    print("Recommendations: The Conjuring, Get Out, A Quiet Place")
elif genre == "romance":
    print("Recommendations: The Notebook, La La Land, Pride and Prejudice")
else:
    print("Sorry, no recommendations for that genre.")

# 5. Simple calculator
print("\nSimple Calculator")
firstnumber =int(input("Enter the first number: "))
secondnumber =int(input("Enter the second number: "))
operation = input("Choose an operation (plus, minus, multiply, divide): ")
if operation == "plus":
    result = firstnumber + secondnumber
    print("The result after adding your 2 numbers is : " , result)
elif operation == "minus":
    result = firstnumber - secondnumber
    print("The result after minusing your 2 numbers is : " , result)
elif operation == "multiply":
    result = firstnumber * secondnumber
    print("The result after multiplying your 2 numbers is: ", result)
elif operation == "divide":
    result = firstnumber / secondnumber
    print("The result after dividing your 2 numbers is: ", result) 


