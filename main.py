import random
import wordList as words
import func as f

def play_game():
    print("Welcome to Wordle Game!")
    chosen_word = random.choice(words.easy_words)
    is_playing = True
    word_length = len(chosen_word)
    tries = 6
    print("You have {} tries".format(tries))
    while is_playing:
        guess = f.get_word_of_length(word_length)
        f.check_word(guess, chosen_word)
        tries = tries-1
        if guess == chosen_word:
            is_playing=False
            print("Congratulations! You won!")
        elif tries==0:
            print("Sorry,you lost,the word was " + chosen_word)
            is_playing=False
    answer = input("Thank you for playing!\nPlay again? y/n")
    if answer == "y":
        play_game()
    else:
        print("Thank you for playing")


play_game()