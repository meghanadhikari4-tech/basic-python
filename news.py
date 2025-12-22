import random
subject=[
    "sharukh khan ",
    "kajol ",
    "virat koli ",
    "zoro ",
    "luffy ",
    "ace ",

]
paragraph=[
    " dies from ",
    " eats meat ",
    " has accident ",
    " sleeps ",
    " lack sleep ",
    " eats banana ",
]
object=[
    " cancer",
    " throughout the day",
    " while playing football",
    " during morning",
    " due to watching phone",
    " like a monkey",
]
s=random.choice(subject)
p=random.choice(paragraph)
o=random.choice(object)
headline=f"BREAKING NEWS:{s}{p}{o}"
print ("\n"+headline)
 