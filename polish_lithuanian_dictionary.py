import sqlite3

connection = sqlite3.connect("C:/Users/Kristina/Desktop/1.db")

Zodynas = connection.execute("SELECT * FROM Zodynas")


def set_translation(polish, lithuanian):
    polish_lithuanian_dictionary[polish] = lithuanian


def get_translation(translated_to_polish):
    SQL = "SELECT Lithuanian FROM Zodynas WHERE Polish = \"" + translated_to_polish + "\""
    translated_to_polish = connection.execute(SQL)
    return translated_to_polish.fetchone()[0]


def get_translated_words():
    all_words = ""
    for record in Zodynas:
        if all_words == "":
            all_words = all_words + record[1]
        else:
            all_words = all_words +", "+ record[1]
    print all_words


def print_words_in_dictionary():
    print "Polish words we can translate:", get_translated_words()

def translate_to_lithuanian():
    print get_translation(str(raw_input('Type word you want to translate to Lithuanian\n')))


def play_translation(answer, random_polish):
    random_lithuanian = connection.execute("SELECT Lithuanian FROM Zodynas WHERE Polish\"" + random_polish + "\"").fetchone()[0]
    if answer == random_lithuanian:
        print "saunuolis"
    else:
        print "bandyk dar karta"
    play()

def play():
    random_polish = connection.execute("SELECT Polish FROM Zodynas order by random() limit 1;").fetchone()[0]
    print "how in Lithuanian is " + "'" + random_polish + "'?\n"
    answer = str(raw_input('Enter translation\n'))
    play_translation(answer, random_polish)

def perform_action(action_number):
    if action_number > 4:
        print "Wrong number!"
    elif action_number == 1:
        print_words_in_dictionary()
    elif action_number == 2:
        play()
    elif action_number == 3:
        translate_to_lithuanian()
    if action_number != 4:
        perform_action(int(raw_input(
            "Do you wanna to continue? Enter 1 to see all words, 2 - get a quiz, 3 - translate, 4 - exit\n")))
    else:
        print "See you soon! Iki!"


perform_action(int(raw_input(
    "If you want to see all words in Polish dictionary - enter 1,\n" +
    "if you want to play a game - enter number 2,\n" +
    "if you want to translate a word into Lithuanian - enter 3\n")))

connection.close()