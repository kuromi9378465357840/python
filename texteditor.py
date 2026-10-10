#get the paragraph from user.
paragraph = input("what you wanna type?")

while True: 

    #ask the incorrect word
    incorrect = input("what is the incorrect word/error?")

    #ask the correct word
    correct = input("what is the correct word?")

    #replacement of grammatical errors
    paragraph =(paragraph.replace(incorrect, correct))

    #ask if they want to stop
    choice = input("do you want to fix another error?")
    if choice == "no":
        break #this exits the loop

print("Final paragraph: " + paragraph)