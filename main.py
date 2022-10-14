import wordle

begin_message = """
'##:::::'##::'#######::'########::'########::'##:::::::'########:
 ##:'##: ##:'##.... ##: ##.... ##: ##.... ##: ##::::::: ##.....::
 ##: ##: ##: ##:::: ##: ##:::: ##: ##:::: ##: ##::::::: ##:::::::
 ##: ##: ##: ##:::: ##: ########:: ##:::: ##: ##::::::: ######:::
 ##: ##: ##: ##:::: ##: ##.. ##::: ##:::: ##: ##::::::: ##...::::
 ##: ##: ##: ##:::: ##: ##::. ##:: ##:::: ##: ##::::::: ##:::::::
. ###. ###::. #######:: ##:::. ##: ########:: ########: ########:
:...::...::::.......:::..:::::..::........:::........::........::
"""
print(begin_message.replace("#", f"{wordle.Colors.yellow}#{wordle.Colors.base}"))

if __name__ == '__main__':
    while True:
        guess = wordle.GuessWord(word_str=input(f"[{wordle.GuessWord.counter}]>"))
        if guess.word_str == "h":
            list_values = list(wordle.GuessWord.alphabet.values())
            for element in list_values:
                print(element, end=" " if list_values[-1] != element else "\n")
            continue
        if guess.check_valid():
            guess.apply_guess()
            guess.check_perfect_guess()
            guess.next_try()
            guess.check_game_loss()
        # print(wordle.GuessWord.counter)






