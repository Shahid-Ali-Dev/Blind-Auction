# 🕶️ Blind Auction Game (Python)

This is a simple command-line game built in Python that simulates a **blind auction**. Multiple users can place bids without knowing what others have bid, and at the end, the program announces the highest bidder as the winner.

---

## 🎯 Features

- Accepts multiple users with their name and bid
- Clears the screen after each bidder (simulated by printing 100 new lines)
- Finds and displays the highest bidder at the end
- Uses recursion to repeat bidding until all participants have submitted bids
- Uses a dictionary to store bids for each participant

---

## 🚀 How It Works

1. Each user is prompted to enter their **name** and **bid amount**.
2. The program asks if there are more bidders:
   - If `yes`, it clears the screen and continues
   - If `no`, it evaluates all bids
3. The highest bidder is determined and announced

---

## 🧪 Example Output

(Logo)
What's your name?: Alice
What's your bid?: $150
Are there any other biders? Type 'yes' or 'no'.
yes

[screen clears]

What's your name?: Bob
What's your bid?: $175
Are there any other biders? Type 'yes' or 'no'.
no

The winner is Bob with $175 bid.

