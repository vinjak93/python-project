import random

# List of symbols for the slot machine
symbols = ['🍒', '🍋', '🔔', '💎', '🍀']

# Starting balance
balance = 100

print("Welcome to the Slot Machine Game!")
print("You start with $100.")

# Main game loop
while True:
    print("\nYour current balance: $", balance)
    bet = int(input("Enter your bet amount (or 0 to quit): "))

    if bet == 0:
        print("Thanks for playing! Your final balance is $", balance)
        break

    if bet > balance:
        print("You don't have enough balance for this bet.")
        continue

    # Spin the reels
    reel1 = random.choice(symbols)
    reel2 = random.choice(symbols)
    reel3 = random.choice(symbols)

    print("Spinning...")
    print(f"Reels: {reel1} | {reel2} | {reel3}")

    # Check the outcome
    if reel1 == reel2 == reel3:
        print("Jackpot! You won $", bet * 10)
        balance += bet * 10
    elif reel1 == reel2 or reel1 == reel3 or reel2 == reel3:
        print("You won $", bet * 2)
        balance += bet * 2
    else:
        print("You lost your bet.")
        balance -= bet

    if balance <= 0:
        print("You ran out of money! Game over.")
        break
