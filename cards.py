from enum import Enum
import random

class Card(Enum):
	ONE_ELEVEN_OUT = "1/11"
	TWO = "2"
	THREE = "3"
	FOUR_PLUS_MINUS = "4±"
	FIVE = "5"
	SIX = "6"
	SEVEN_SPECIAL = "7"
	EIGHT = "8"
	NINE = "9"
	TEN = "10"
	SWAP = "^"
	TWELVE = "12"
	THIRTEEN_OUT = "13"
	JOKER = "?"

STANDARD_CARDS = set((Card.TWO, Card.THREE, Card.FIVE, Card.SIX, Card.EIGHT, Card.NINE, Card.TEN, Card.TWELVE))
STANDARD_CARDS_COPIES = 8
SPECIAL_CARDS = set((Card.ONE_ELEVEN_OUT, Card.FOUR_PLUS_MINUS, Card.SEVEN_SPECIAL, Card.THIRTEEN_OUT, Card.SWAP))
SPECIAL_CARDS_COPIES = 8
JOKERS_COPIES = 6

def build_initial_deck():
	deck = []
	for card in STANDARD_CARDS:
		deck.extend([card] * STANDARD_CARDS_COPIES)
	for card in SPECIAL_CARDS:
		deck.extend([card] * SPECIAL_CARDS_COPIES)
	deck.extend([Card.JOKER] * JOKERS_COPIES)
	random.shuffle(deck)
	return deck

def print_hand(player_number, hand):
	print("Player {}: {}".format(player_number, " ".join([card.value for card in hand])))

deck = build_initial_deck()
played = []
NUM_HANDS = 6
ROUNDS_TO_DEAL = 20
for r in range(ROUNDS_TO_DEAL):
	hand_size = 6-(r%5)
	hands = []
	for i in range(NUM_HANDS):
		hands.append([])
	for i in range(hand_size):
		for hand in hands:
			hand.append(deck.pop())
	print("Round {}: Dealt {} cards to each of {} players:".format(r+1, hand_size, NUM_HANDS))
	for i, hand in enumerate(hands):
		print_hand(i+1, hand)
	print("Before Round: Cards in deck: {} Cards in discard to shuffle in: {}".format(len(deck), len(played)))
	deck.extend(played)
	random.shuffle(deck)
	played = []
	for hand in hands:
		played.extend(hand)



