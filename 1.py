dict = {"ja": "as", "ty": "tu", "my": "mes", "oni": "jie", "one": "jos", "ona": "ji", "on": "jis",
                "chlodnik": "saltibarsciai", "kot": "katinas"}


def dictionary():
    actionNumber = int(raw_input("If you want to see all words in Polish dictionary - enter 1,\nif you want to add translation to this dictionary - enter number 2,\nif you want to translate a word into Lithuanian - enter 3"))

    def choices(actionNumber):
        if actionNumber > 4:
            print "Wrong number!"
        elif actionNumber == 1:
            print "Polish words we can translate:", dict.keys()
        elif actionNumber == 2:
            def AddTranslation():
                Polish = str(raw_input("Type word in Polish\n"))
                Lithuanian = str(raw_input("Give translation to Lithuanian\n"))
                dict[Polish] = Lithuanian
            AddTranslation()
            print "updated: Polish words we can translate:", sorted(dict.keys())
        elif actionNumber == 3:
            print dict.get(str(raw_input('Type word you want to translate to Lithuanian\n')))
        elif actionNumber == 4:
            print "iki"
        if actionNumber != 4:
            recall = int(raw_input("Do you wanna to continue? Enter 1 to see all words, 2 - add translation, 3 - translate, 4 - exit"))
            return choices(recall)
    choices(actionNumber)
dictionary()
