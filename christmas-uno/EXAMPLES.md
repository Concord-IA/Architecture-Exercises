# State Representation Examples

The **biggest challenge** in Q-learning for Uno is representing the game state. You can't use the full hand (too many combinations!), so you need to extract **features** that matter.

## ❌ Too Complex (Don't Do This!)

```python
# Using full hand - TOO MANY STATES!
state = str(sorted(my_hand))  # "BLUE3,RED5,RED7,..."

# With 48 cards, this creates billions of possible states!
# Your agent will never see the same state twice, so it can't learn!
```

**Why this fails:**
- With 7 cards from a deck of 48, there are millions of possible hands
- Q-table becomes huge and sparse
- Agent never learns because it rarely (or never) sees the same state twice

## ✅ Simple (Start Here!)

```python
# Just hand sizes and top card color
state = f"{len(my_hand)}_{len(opp_hand)}_{top_card.color}"

# Example: "5_7_RED"
# Only ~100 possible states, learns FAST
```

**Why this works:**
- Very few states (~100 combinations)
- Agent sees same states repeatedly
- Learns basic strategy: "when I have few cards and opponent has many, play aggressively"

**Limitations:**
- Can't distinguish between different cards of same color
- Might miss color-specific strategies

## ✅✅ Medium (Better Strategy)

```python
# Add color counts in hand
red_count = sum(1 for c in my_hand if c.color == Color.RED)
blue_count = sum(1 for c in my_hand if c.color == Color.BLUE)
green_count = sum(1 for c in my_hand if c.color == Color.GREEN)
yellow_count = sum(1 for c in my_hand if c.color == Color.YELLOW)

state = f"{len(my_hand)}_{len(opp_hand)}_{top_card.color}_{red_count}_{blue_count}_{green_count}_{yellow_count}"

# Example: "5_7_RED_2_1_1_1"
# ~10,000 states, still manageable
```

**Why this works:**
- More informative than simple version
- Can learn color-specific strategies
- Still manageable number of states (~10,000)

**Trade-off:**
- Takes longer to learn than simple version
- But learns better strategies

## ✅✅✅ Advanced

```python
# Add whether you have matching cards
has_color_match = any(c.color == top_card.color for c in my_hand)
has_number_match = any(c.value == top_card.value for c in my_hand if c.card_type == CardType.NUMBER)
has_special = any(c.card_type in [CardType.SKIP, CardType.DRAW_TWO] for c in my_hand)

state = f"{len(my_hand)}_{len(opp_hand)}_{top_card.color}_{top_card.value}_{has_color_match}_{has_number_match}_{has_special}"

# Example: "5_7_RED_7_True_True_False"
```

**Why this works:**
- Captures strategic information (can I match? do I have special cards?)
- Still reasonable number of states
- Can learn more nuanced strategies

## 🎯 Recommendations

**For beginners:**
- Start with the **Simple** version
- Get it working and learning
- Then try **Medium** to see if it improves

**For advanced:**
- Try **Advanced** or create your own features
- Experiment with different combinations
- Track Q-table size - if it grows beyond 100,000 states, simplify!

## 💡 Feature Ideas

Think about what matters in Uno:

- **Hand size** - fewer cards = closer to winning
- **Opponent hand size** - more cards = they're struggling
- **Top card color** - determines what you can play
- **Color distribution** - do you have many cards of the top color?
- **Can you match?** - boolean: do you have any playable cards?
- **Special cards** - do you have Skip/Draw Two available?
- **Number of valid actions** - more options = more flexibility

**Experiment!** Try different representations and see what works best for your implementation.
