# 🎄 Getting Started with Uno RL Challenge

## What You Have

This is a **minimal starter repo** - it gives you:

- ✅ Clear game rules
- ✅ A few basic tests to verify your implementation works
- ✅ A starter template (optional - use it or not!)
- ✅ Example training/play scripts

**You have CREATIVE FREEDOM on how to implement everything!**

## First Steps

### 1. Setup

**Option A: Using uv (recommended)**
```bash
# Install uv if you don't have it
# Windows: powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
# Mac/Linux: curl -LsSf https://astral.sh/uv/install.sh | sh

# Create virtual environment and install dependencies
uv venv
uv pip install -e .
```

**Option B: Using pip**
```bash
pip install -e .
```

### 2. Understand the Game

Read `README.md` carefully - especially:

- Game rules (48 cards, matching rules, special cards)
- Win condition
- What you need to implement

### 3. Start Building

**Option A: Use the starter template**

```bash
# Copy and modify starter_template.py
cp starter_template.py uno_game.py
# Now implement the TODOs
```

**Option B: Build from scratch**

```bash
# Create your own structure - totally fine!
# As long as it works and follows the rules
```

### 4. Test Your Implementation

```bash
# Run basic tests (you'll need to update imports first!)
python test_basic.py
```

**Important:** The test file has TODOs - you need to:

1. Import your implementation
2. Fill in the test logic
3. Add more tests!

### 5. Build Agents

**Random Agent (easier):**

- Just picks a random valid move
- Good baseline to test environment works

**Q-Learning Agent (harder):**

- **KEY CHALLENGE:** State representation!
- Start simple: just hand sizes + top card color
- Can always add more features later

### 6. Train and Analyze

```bash
# Modify train.py to use your implementation
python train.py

# Play games
python play.py
```

## 🎯 Key Challenges

### Challenge 1: State Representation

You **cannot** use the full hand as state (too many combinations!).

**Think about features:**

- How many cards do I have?
- How many cards does opponent have?
- What's the top card color/number?
- How many of each color do I have?

**Start simple!** `f"{my_cards}_{opp_cards}_{top_color}"` is totally valid.

### Challenge 2: Special Cards

Skip and Draw Two both make the **same player go again**:

- Skip: Opponent just loses turn
- Draw Two: Opponent draws 2 cards **AND** loses turn

### Challenge 3: Q-Learning Update

The formula from lecture:

```
Q(s,a) ← Q(s,a) + α[r + γ max Q(s',a') - Q(s,a)]
```

When game ends (`done=True`), `max Q(s',a') = 0`

## 💡 Implementation Tips

**Environment:**

1. Start with just number cards
2. Get that working first
3. Then add Skip
4. Then add Draw Two
5. Test after each addition!

**Testing:**

- Use `seed=42` for reproducible games
- Print state after every step while debugging
- Start with small hands (2-3 cards) for testing

**Q-Learning:**

- High epsilon initially (0.5) for exploration
- Decay over time: `epsilon *= 0.995`
- Min epsilon around 0.01
- Track win rate every 1000 games

**State Representation:**

- Simpler = learns faster initially
- More complex = might learn better strategies
- Experiment!

## 📋 Deliverables

When you're done:

1. **Code** (your structure, your choice!)

2. **Report** (1-2 pages):

   - How you designed your environment
   - Your state representation choice & why
   - Training results (win rates, plots if you want)
   - What strategies your agent learned
   - Challenges you faced

## 🎁 Have Fun!

This is about **learning by building**. Don't worry about making it perfect - focus on:

- Understanding the concepts
- Getting something working
- Experimenting and learning

Be creative! Try different state representations! See what works!

## 🐛 Troubleshooting

**"Tests don't run"**

- Did you update the imports in test_basic.py?
- Did you implement at least the basic methods?

**"Q-learning not learning"**

- Check your state representation - is it too complex?
- Print Q-table size - should grow to a few thousand, not millions
- Are you decaying epsilon? (should go from 0.5 → 0.01)

**"Game hangs/infinite loop"**

- Check win condition logic
- Make sure game ends after 1000 turns max
- Print turn counter to debug

**"Agent wins 0% of games"**

- Is your reward correct? (+100 for win, -100 for loss)
- Are you updating the Q-table? (check Q-table size increases)
- Try simpler state representation first

**Questions?** Ask in #sotonlm-architecture

**Merry Christmas! 🎄**
