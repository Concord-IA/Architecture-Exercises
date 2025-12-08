# 🎮 Uno RL Challenge

Build a 2-player Uno game and teach an AI to play it using Reinforcement Learning!

## 🎯 The Challenge

**Build:**

1. A working Uno game environment
2. A random agent (baseline)
3. A Q-learning agent that learns to play strategically

**Learn:**

- Sequential decision making
- State representation (the hard part!)
- Q-learning algorithm
- Training RL agents

## 📋 Game Rules

**Deck:** 48 cards total
- 40 number cards: 4 colors × (0-9)
- 8 special cards: 4 Skip + 4 Draw Two

**Setup:**
- Each player starts with 7 cards
- 1 card face-up to start

**Matching:**
- Play a card matching top card by: color OR number OR type
- If no match: draw 1 card

**Special Cards:**
- **Skip**: Opponent loses turn (you go again)
- **Draw Two**: Opponent draws 2 cards AND loses turn (you go again)

**Win:** First to empty hand wins!

## 🎴 Visual Example

Starting hand example:

- Player 1: [RED 5, BLUE 3, GREEN 7, YELLOW 2, RED SKIP, BLUE 9, GREEN 0]
- Player 2: [7 cards hidden]
- Top card: RED 7

Valid plays: RED 5, RED SKIP (match color) or GREEN 7, BLUE 7, YELLOW 7 (match number)

If you play RED SKIP → opponent loses turn, you go again!

## 🚀 Quick Start

```bash
# Install dependencies (using uv - recommended)
uv venv
uv pip install -e .

# Or using pip
pip install -e .

# Run basic tests to verify your implementation works
python test_basic.py

# Play a game
python play.py

# Train your agent
python train.py --episodes 10000
```

## 📁 What to Implement

### 1. **Game Environment** (Core)

Create your Uno game however you like! As long as it works and follows the rules.

**Suggested structure:**

```python
class UnoEnvironment:
    def reset() -> state
    def step(action) -> (next_state, reward, done)
    def get_valid_actions() -> List[actions]
```

### 2. **Random Agent** (Baseline)

An agent that picks random valid moves.

### 3. **Q-Learning Agent** (Advanced)

Implement Q-learning to train an agent that learns strategy!

**Key challenge:** How do you represent state? You can't track every card combination (too many states!). Think about what features matter:
- Hand sizes?
- Top card color/number?
- Color counts in hand?

Be creative!

## ✅ Verification

Run `test_basic.py` to check your implementation handles:
- Game initialization
- Playing valid cards
- Special card effects (Skip, Draw Two)
- Win conditions
- Random reproducibility with seeds

**These are minimal tests** - you should add your own!

## ⚠️ Common Mistakes to Avoid

1. **State representation too complex** - Using full hand = millions of states, won't learn
2. **Forgetting Skip/Draw Two logic** - Both make SAME player go again (not alternating)
3. **Not testing incrementally** - Build number cards first, THEN add special cards
4. **Epsilon not decaying** - Agent never stops exploring, won't converge
5. **Reward only at end** - Consider small rewards during game too (optional)

## 📊 Deliverables

**Code:**
- Your implementation (structure it however you want!)
- Training script
- Play script

**Report (1-2 pages):**
- How did you design your environment?
- What state representation did you choose for Q-learning? Why?
- Results: win rates, training curves, Q-table size
- What strategies did your agent learn?

## 💡 Tips

**Getting Started:**
- Start with number cards only, add special cards later
- Test with small hands (2-3 cards) first
- Print state after every step while debugging
- Use `seed=42` for reproducible testing

**State Representation Ideas:**
- Simple: `f"{my_hand_size}_{opp_hand_size}_{top_color}"`
- Medium: Add top card number, color counts
- Complex: Include card type patterns

Simpler representations learn faster but might miss strategies!

**Q-Learning:**
- Start epsilon high (0.5) for exploration
- Decay over time: `epsilon *= 0.995` each game
- Min epsilon around 0.01
- Save Q-table periodically!

## 🎓 Connection to LLMs

This teaches concepts directly applicable to language modeling:
- **Sequential decisions** → Next token prediction
- **State representation** → Token embeddings  
- **Reward shaping** → RLHF objectives
- **Exploration vs exploitation** → Temperature sampling

Think: How is playing Uno like generating text?

## 🏆 Grading Rubric

| Component | Points |
|-----------|--------|
| Working environment | 40 |
| Tests pass | 20 |
| Random agent + analysis | 10 |
| Q-Learning implementation | 20 |
| Report | 10 |

**Bonus:** +5 pts for most creative state representation that works well!

## 📚 Resources

- Lecture slides on RL fundamentals
- Sutton & Barto Chapter 6 (Temporal Difference Learning)
- OpenAI Spinning Up: Q-Learning tutorial

## 🎁 Have Fun!

The goal is to **learn by building**. Be creative with your implementation! As long as it follows the rules and your agent learns something, you're doing great.

Questions? Ask in #sotonlm-architecture

**Merry Christmas and happy coding! 🎄**
