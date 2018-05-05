import random

article = ("the", "a", "an")
noun = ("dog", "Ferrari", "mountains", "river", "intelligence")
verb = ("work", "play", "listen", "walk", "talk")

sentence = random.choice(article) + ' ' + random.choice(noun) + ' ' + random.choice(verb)

print(sentence);
