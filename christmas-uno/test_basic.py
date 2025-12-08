"""
Basic Tests for Uno Environment

IMPORTANT: These tests have TODOs!

Before running:

1. Implement your Uno game (any structure you want)
2. Update the imports at the top to match your code
3. Fill in the test logic (marked with TODO)
4. Run: python test_basic.py

Example import:
    from my_uno_game import UnoEnvironment, RandomAgent, QLearningAgent

These are MINIMAL tests to verify your implementation works.
You should add more tests of your own!
"""

import unittest

# TODO: Import your implementation here
# from your_uno_file import UnoEnvironment, or however you structure it


class TestBasicFunctionality(unittest.TestCase):
    """Minimal tests - add more of your own!"""
    
    def setUp(self):
        """Setup before each test"""
        # TODO: Create your environment
        # self.env = YourEnvironment(seed=42)
        pass
    
    def test_game_initializes(self):
        """Test 1: Game starts correctly"""
        # TODO: Test that game initializes with 2 players, 7 cards each
        pass
    
    def test_can_play_valid_card(self):
        """Test 2: Can play a valid matching card"""
        # TODO: 
        # - Start game
        # - Get valid actions
        # - Play one
        # - Verify game state changes
        pass
    
    def test_skip_card_skips_opponent(self):
        """Test 3: Skip card makes same player go again"""
        # TODO:
        # - Force a Skip card to be played (you might need to manipulate deck)
        # - Verify current player doesn't change
        pass
    
    def test_draw_two_works(self):
        """Test 4: Draw Two gives opponent 2 cards and skips turn"""
        # TODO:
        # - Play Draw Two card
        # - Verify opponent gets 2 cards
        # - Verify opponent's turn is skipped
        pass
    
    def test_game_ends_when_hand_empty(self):
        """Test 5: Game ends when player empties hand"""
        # TODO:
        # - Get a player to empty their hand (might need to manipulate state)
        # - Verify game returns done=True
        # - Verify winner gets +100 reward, loser gets -100
        pass
    
    def test_reproducible_with_seed(self):
        """Test 6: Same seed = same game"""
        # TODO:
        # - Create two games with same seed
        # - Verify initial states are identical
        pass


class TestAgents(unittest.TestCase):
    """Test your agents work"""
    
    def test_random_agent_picks_valid_actions(self):
        """Test 7: Random agent only picks legal moves"""
        # TODO:
        # - Create environment and random agent
        # - Play 100 random moves
        # - Verify all moves are legal
        pass
    
    def test_q_agent_can_select_action(self):
        """Test 8: Q-learning agent can pick actions"""
        # TODO:
        # - Create Q-learning agent
        # - Verify it can select actions (even with empty Q-table)
        pass


def run_basic_tests():
    """Run all basic tests"""
    print("=" * 60)
    print("Running Basic Uno Tests")
    print("=" * 60)
    print("\nThese are MINIMAL tests.")
    print("You should implement more comprehensive tests yourself!")
    print("=" * 60)
    
    unittest.main(argv=[''], exit=False, verbosity=2)


if __name__ == '__main__':
    run_basic_tests()
