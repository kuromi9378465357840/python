import random

words = ["python", "java", "javascript", "ruby", "html", "css", "react", "angular", "vue", "node"]
word = random.choice(words)
attempts = 0

while True:
    guess = input("Guess the word: ").strip().lower()
    attempts +=1
    if guess == word:
        print("You got it in", attempts,"attempts!")
        break
    else:
        print("Wrong guess!")
        print("Hint: The word has", len(word), "letters.")