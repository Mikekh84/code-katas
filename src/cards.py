

def sort_cards(cards):
    """Sort a deck of cards."""
    deck = []
    new_deck = []
    for card in cards:
        if card.upper() == 'A':
            deck.append((0, 'A'))

        elif card.upper() == 'T':
            deck.append((10, 'T'))

        elif card.upper() == 'J':
            deck.append((11, 'J'))

        elif card.upper() == 'Q':
            deck.append((12, 'Q'))

        elif card.upper() == 'K':
            deck.append((13, 'K'))

        else:
            deck.append((int(card), card))
    deck.sort()
    for card in deck:
        card = card[1]
        new_deck.append(card)
    return new_deck
