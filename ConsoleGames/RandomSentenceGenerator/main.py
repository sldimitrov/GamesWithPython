import random
import time

# Initializing a list for the names.
names = ["Stoqn", "Slavi", "Nasko", "Kristiqn", "Slavi Trifanov",
         "Billy", "Krisko", "Rapuncel", "Pesho", "Boyko Borisov",
         "Mariqna", "Teodor", "Atanas", "Viktor", "Grisho Dimitrov",
         "Mike Tyson", "Vladimir Putin", "David Goggins", "The clasher",
         "Will Smith", "Pedro", "Elizabeth"]

# Initializing a list for places.
places = ["South London", "Aytos", "the ghetto", "school",
          "Pazardjik", "Gabrovo", "Atlantic", "Sofia",
          "Arjentina", "Turkey", "BS KS", "the public house",
          "the area", "the arena", "the beach", "the prison"]

# Initializing a list for verbs.
verbs = ["watches", "drinks", "drives", "starts arguing",
         "pissed a", "throws", "kisses", "kick", "punch",
         "takes", "pull up", "spit", "wears"]

# Initializing a list for the nouns.
nouns = ["stones", "cake", "chair", "toy", "laptop", "bikes", "ball", "mouse",
         "bar", "cat", "car", "building", "hat", "stick", "brick", "beer", "drees",
         "bank", "baseball", "bath", "bedroom", "bird", "book", "bonus", "bus", "business"]

# Initializing a list for adverbs.
adverbs = ["slowly", "diligently", "warmly", "coldly", "sadly", "slowly", "rapidly", "extremely",
           "angrily", "calmly", "significantly", "lovely", "downstairs", "proudly", "nearby", "soon",
           "cheerfully", "carelessly", "inside", "madly", "deeply", "curiously", "consciously", "later"]

# Initializing a list for details.
details = ["near the river", "in the part", "at anonymous house", "at school", "in the shelf", "in his thoughts",
           "near the hospital", "down the bridge", "at the strip bar", "under the table", "up to the ceiling"
           "in the DeathZone", "in CS 1.6", "in GTA 5", "in the mountain"]

# Initializing a list for greetings.
greetings = ["bye, bye!", "see you soon!", "can't wait to chat again!", "have a nice day!", "greetings, SD!",
             "much health!", "now buy me a coffee!", "hehehe", "huh", "bruh", "son"]

# Initializing a list to various of saying thanks.
thanks = ["Thank you for", "You're welcome back when you", "Wishing you all the best", "I love you, also",
          "Why you left, i was just starting to", "Ah you, bad boy"]


def random_word(words: list) -> str:
    """
        A simple function that takes: list as parameter
        and returns: str(random choice)
    """
    return random.choice(words)


def start_the_program():
    """
    Define a function to start the program,
    here we also call the Main one.
    """
    print("\nHello, let fun begins!")
    print(3)
    time.sleep(1)
    print(2)
    time.sleep(1)
    print(1)
    time.sleep(1)
    main()


# Define the main function of the program
def main():
    while True:
        """ 
            Choosing random words by calling
            random_word() function
            takes: no arguments
        """
        random_name = random_word(names)
        random_place = random_word(places)
        random_verb = random_word(verbs)
        random_noun = random_word(nouns)
        random_adverb = random_word(adverbs)
        random_detail = random_word(details)

        print(f"{random_name} from {random_place} {random_adverb} {random_verb} {random_noun} {random_detail}.")
        answer = input("Click [Enter] to generate a new one. WRITE [End] to end: \n")

        if answer.lower() == 'end':
            close_the_program()
            break


def close_the_program():
    """"
    We use this function to print and end the program
    takes: no arguments
    """
    random_noun = random_word(nouns)
    random_verb = random_word(verbs)
    random_greet = random_word(greetings)
    random_thanks = random_word(thanks)
    print(f"{random_thanks} {random_verb} my new {random_noun}, {random_greet}")


start_the_program()




