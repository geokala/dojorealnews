import random
import re

TEMPLATES = (
    "You won't believe what {person} was found doing with {object}",
    "{person}'s {object} kills {nn} on highway",
    "Scientists claim {object} causes cancer",
    "{object} found on moon - police arrest {person}",
    "{person} ate my {object}, sobs hysterical Spurs fan",
    "{nn} types of {object} that you can't live without - {person} swears by #7!",
)

OBJECTS = (
    "a cabbage", "a space hopper", "a Ford Pinto",
    "an anteater", "a bottle of beer", "an antique lamp",
    "a spanner", "Mars", "Illuminati secrets",
    "original source code of Windows 1.0",
)

PEOPLE = (
    "Donald Trump", "Vladimir Putin", "Dr Seuss",
    "Jeremy Cronyn", "Karl Marx", "Mikhail Bakunin",
    "Beyoncé Knowles", "Lady Gaga",
    "Isenbard Kingdom Brunel",
)

def sentence():
    return re.sub(
        r"{([a-z]+)}",
        wordgen,
        random.choice(TEMPLATES))

def wordgen(m):
    k = m.group(1)
    if k == "person":
        return random.choice(PEOPLE)
    if k == "object":
        return random.choice(OBJECTS)
    if k == "nn":
        return str(random.randint(11, 19))
    return "balderdash"

if __name__ == "__main__":
    print(sentence())
