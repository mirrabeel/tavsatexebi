import random
from itertools import permutations

def circular_distance(card1, card2):
    return (card2 - card1) % 13

def encode_permutation(order):
    perms = list(permutations(order))
    for i, perm in enumerate(perms):
        if tuple(order) == perm:
            return i + 1

def generate_deck():
    suits = ['♥', '♦', '♣', '♠']  
    deck = [(rank, suit) for rank in range(1, 14) for suit in suits]
    return deck

def choose_five_cards(deck):
    return random.sample(deck, 5)

def magician_trick():
    deck = generate_deck()
    selected_cards = choose_five_cards(deck)

    suit_groups = {}
    for card in selected_cards:
        rank, suit = card
        if suit not in suit_groups:
            suit_groups[suit] = []
        suit_groups[suit].append(rank)

    hidden_suit = None
    for suit, ranks in suit_groups.items():
        if len(ranks) >= 2:
            hidden_suit = suit
            break

    ranks = sorted(suit_groups[hidden_suit])

    hidden_card_rank = ranks[1]
    first_revealed_rank = ranks[0]

    offset = circular_distance(first_revealed_rank, hidden_card_rank)

    remaining_cards = [card for card in selected_cards if card != (hidden_card_rank, hidden_suit)]

    remaining_cards_sorted = sorted([card[0] for card in remaining_cards])

    permutation_code = encode_permutation(remaining_cards_sorted)

    revealed_cards = [(first_revealed_rank, hidden_suit)] + remaining_cards

    print("Revealed cards:", revealed_cards)
    print("Permutation code (offset):", permutation_code)

    guessed_card = (hidden_card_rank, hidden_suit)
    print("Guessed hidden card:", guessed_card)

magician_trick()
