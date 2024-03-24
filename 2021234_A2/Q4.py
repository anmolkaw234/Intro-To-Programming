import random

words = ["Poxer", "Writy", "Fyren", "Gizmo", "Jivvy", "Lixiv", "Mivvy", "Naxal", "Quiff", "Riven", "Sengi", "Tuyer", "Uvula", "Vogue", "Wizen", "Xysts", "Yowie", "Zippy", "Apsis", "Bower", "Cower", "Dower", "Eager", "Fiver", "Giver", "Hiker", "Ivied", "Jowar", "Knead", "Lying", "Miter", "Nerve", "Ovals", "Prawn", "Quell", "Rower", "Sower", "Taper", "Unlit", "Vents", "Wager", "Xysts", "Yacht", "Zonal", "Abash", "Bemix", "Cower", "Diner", "Eager", "Folly"]


index = random.randint(0, len(words)-1)
word = words[index]
tries = 6

while tries > 0:
    guess = input("Enter a 5 character string: ")
    if guess == word:
        print("Congratulations! You guessed the word correctly.")
        break
    else:
        result = ""
        other = ""
        for i in range(len(word)):
            if guess[i] == word[i]:
                result += guess[i]
            elif guess[i] in word:
                other += guess[i]
            else:
                result += "-"
        print(result)
        print("Other characters present: ", other)
        tries -= 1
        if tries == 0:
            print("Sorry, you have reached the maximum number of tries. The word was ", word)

