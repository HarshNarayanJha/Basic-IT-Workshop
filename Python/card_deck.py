from random import shuffle

classes = ["Spade", "Diamond", "Heart", "Clubs"]
faces = [str(x) for x in range(1, 10)] + ["King", "Queen", "Jack", "Ace"]

deck = []

for c in classes:
    for f in faces:
        deck.append(f"{f} of {c}")

shuffle(deck)

print(*deck[:5], sep=', ')
