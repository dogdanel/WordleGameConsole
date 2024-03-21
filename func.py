from colorama import Fore
def get_word_of_length(length):
    while True:
        word = input(f"Please enter a word with {length} letters: ")
        if len(word) == length:
            return word
        else:
            print(f"Word must have exactly {length} letters. Try again.")

def check_word(guess,chosen_word):
    for i in range(len(guess)):
        if guess[i] == chosen_word[i]:
            print(Fore.GREEN + guess[i] + Fore.WHITE, end="")
        elif guess[i] in chosen_word:
            print(Fore.YELLOW + guess[i] + Fore.WHITE, end="")
        else:
            print(Fore.RED + guess[i] + Fore.WHITE, end="")
    print("\n")
