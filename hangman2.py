import random
def play_hangman():
    word_list = ["python", "java", "kotlin", "javascript", "ruby"]
    word = random.choice(word_list)
    word_letters = set(word)
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    correct_letters = set()
    incorrect_letters = set()
    tries = 6
    ans=""

    while len(word_letters) > 0 and tries>0:
        print("You have", tries, "tries left.")
        print("Available letters:", "".join(alphabet - incorrect_letters - correct_letters))
        user_letter = input("Please guess a letter: ").lower()
        if user_letter in word_letters:
            correct_letters.add(user_letter)
            word_letters.remove(user_letter)
            for i in word_letters:
                for j in  correct_letters:
                    if i==j:
                        ans=ans+i
                    else:
                        ans=ans+"_"
            print(ans)


        else:
            tries -= 1
            incorrect_letters.add(user_letter)
        
        for letter in word:
            if letter in correct_letters:
                print(letter, end=" ")
            else:
                print("_", end=" ")
        print()

    if tries == 0:
        print("You lost! The word was", word)
    else:
        print("You won! The word was", word)

print("HANGMAN")
play_hangman()