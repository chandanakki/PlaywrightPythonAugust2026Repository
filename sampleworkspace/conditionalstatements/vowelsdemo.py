#character="E"
character = input("Enter the Character:")

match character:
    case "A" | "E" | "I" | "O" | "U":
        print(character," is a Vowel")
    case _:
        print("It is not a Vowel")
    