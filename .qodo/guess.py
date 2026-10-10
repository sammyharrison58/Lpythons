import random
columns =['customer_id', "order_date", "total_amount", "status"]
word = random.choice(columns)
guessed =set()
attempts = 4

while attempts > 0:
    display = " ".join(c if c in guessed else "_" for c in word)
    print(f'Word: {display}  Attempts left: {attempts}')
    guess = input("Guess a letter: ").lower()
    if guess in guessed:
        print(f"You've already guessed '{guess}'. Try again.")
        continue
    guessed.add(guess)
    if guess not in word:
        attempts -= 1
        print(f"'{guess}' is not in the word.")
    if all(c in guessed for c in word):
        print(f"Congratulations! You've guessed the word: '{word}'")

else:
    print(f"Sorry, you've run out of attempts. The word was: '{word}'")