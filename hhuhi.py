import random
subject={
    "sharukh khan"
    "kajol"
    "virat koli"
    "zoro"
    "luffy"
    "ace"

}
paragraph={
    "dies from"
    "eats meat"
    "has accident"
    "sleeps"
    "lack sleep"
    "eats banana"
}
object={
    "cancer"
    "throughout the day"
    "while playing football"
    "during morning"
    "due to watching phone"
    "like a monkey"
}
while True:
    subject=random.choice(subject)
    paragraph=random.choice(paragraph)
    object=random.choice(object)
    headline=f"BREKING NEWS:{subject}{paragraph}{object}"
    print ("\n"+headline)
