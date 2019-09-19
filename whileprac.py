secret_word = "Khan"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = raw_input("Enter Guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print ("out of guesses, YOU LOOOSE!")
else:
    print ("YOU WIN!")
