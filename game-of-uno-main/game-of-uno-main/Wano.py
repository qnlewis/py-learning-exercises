import random

# Define card colors and values
COLORS = ['Red', 'Green', 'Blue', 'Yellow']
VALUES = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'Skip', 'Reverse', '+2']

# Create a deck of UNO cards
def create_deck():
    deck = []
    for color in COLORS:
        for value in VALUES:
            deck.append(f"{color} {value}")
            if value != '0':  # Only one '0' per color
                deck.append(f"{color} {value}")
    # Add Wild and Wild Draw Four cards
    for _ in range(4):
        deck.append("Wild")
        deck.append("Wild +4")
    return deck

# Shuffle the deck
def shuffle_deck(deck):
    random.shuffle(deck)
    return deck

# Deal cards to players
def deal_cards(deck, num_players):
    hands = [[] for _ in range(num_players)]
    for _ in range(8):  # Each player gets 8 cards
        for i in range(num_players):
            hands[i].append(deck.pop())
    return hands

# Check if a card is valid to play
def is_valid_card(card, top_card):
    if card.startswith("Wild"):
        return True
    card_color, card_value = card.split()
    top_color, top_value = top_card.split()
    return card_color == top_color or card_value == top_value

# Computer player chooses a card to play
def computer_play(hand, top_card):
    valid_cards = [card for card in hand if is_valid_card(card, top_card)]
    if valid_cards:
        # Prefer playing non-Wild cards first
        non_wild = [card for card in valid_cards if not card.startswith("Wild")]
        if non_wild:
            return random.choice(non_wild)
        else:
            return random.choice(valid_cards)
    else:
        return None  # No valid card to play

# Main game loop
def play_uno():
    print("playne mine gamen")
    num_players = int(input("Enter the number of players (2-4): "))
    while num_players < 2 or num_players > 4:
        print("Invalid input.")
        num_players = int(input("Enter the number of players (2-4): "))

    # Initialize game
    deck = create_deck()
    deck = shuffle_deck(deck)
    hands = deal_cards(deck, num_players)
    discard_pile = [deck.pop()]  # Start the discard pile
    current_player = 0
    direction = 1  # 1 for clockwise, -1 for counterclockwise

    # Determine player types (human or computer)
    player_types = []
    for i in range(num_players):
        player_type = input(f"Is Player {i + 1} a human or computer? (h/c): ").lower()
        while player_type not in ['h', 'c']:
            print("Invalid input. Please enter 'h' for human or 'c' for computer.")
            player_type = input(f"Is Player {i + 1} a human or computer? (h/c): ").lower()
        player_types.append(player_type)

    while True:
        print(f"\nPlayer {current_player + 1}'s turn")
        print(f"Top card: {discard_pile[-1]}")
        if player_types[current_player] == 'h':
            print(f"Your hand: {hands[current_player]}")
        else:
            print("Computer is think...")

        # Check if the player has a valid card to play
        valid_cards = [card for card in hands[current_player] if is_valid_card(card, discard_pile[-1])]
        if valid_cards:
            if player_types[current_player] == 'h':
                print("Valid cards to play:", valid_cards)
                chosen_card = input("Choose a card to play (or type 'draw' to draw a card): ")
                if chosen_card == 'draw' or chosen_card == 'Draw':
                    hands[current_player].append(deck.pop())
                    print("You drew a card.")
                elif chosen_card in valid_cards:
                    hands[current_player].remove(chosen_card)
                    discard_pile.append(chosen_card)
                    print(f"You played: {chosen_card}")
                else:
                    print("Invalid choice. Try again.")
                    continue
            else:
                chosen_card = computer_play(hands[current_player], discard_pile[-1])
                hands[current_player].remove(chosen_card)
                discard_pile.append(chosen_card)
                print(f"Computer played: {chosen_card}")
        else:
            print("No valid cards to play. Drawing a card...")
            hands[current_player].append(deck.pop())

        # Handle special cards
        if "+2" in discard_pile[-1]:
            next_player = (current_player + direction) % num_players
            hands[next_player].extend([deck.pop(), deck.pop()])
            print(f"Player {next_player + 1} draws 2 cards!")
            current_player = next_player # Skip the next player's turn.
        elif "Skip" in discard_pile[-1]:
            current_player = (current_player + direction) % num_players
        elif "Reverse" in discard_pile[-1]:
            direction *= -1
        elif discard_pile[-1].startswith("Wild"):
            if player_types[current_player] == 'h':
                new_color = input("Choose a color (Red, Green, Blue, Yellow): ").capitalize()
                while new_color not in COLORS:
                    print("Invalid color. Try again.")
                    new_color = input("Choose a color (Red, Green, Blue, Yellow): ").capitalize()
                discard_pile[-1] = f"Wild {new_color}"  # Change the top card to the chosen color
            else:
                new_color = random.choice(COLORS)
                print(f"Computer chose {new_color}.")
                discard_pile[-1] = f"Wild {new_color}"


        # Check for a winner
        if not hands[current_player]:
            print(f"\nPlayer {current_player + 1} wins!")
            break

        # Move to the next player
        current_player = (current_player + direction) % num_players

# Start the game
play_uno()