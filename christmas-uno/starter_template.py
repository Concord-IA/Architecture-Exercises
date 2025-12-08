"""
Uno Game - Starter Template

This is just a SKELETON to help you get started.
Feel free to structure your code however you want!
"""

import random
from typing import List, Tuple, Optional
from enum import Enum
from dataclasses import dataclass


# Example enums - use if you want!
class Color(Enum):
    RED = 0
    BLUE = 1
    GREEN = 2
    YELLOW = 3


class CardType(Enum):
    NUMBER = 0
    SKIP = 1
    DRAW_TWO = 2


@dataclass
class Card:
    """Example card representation"""
    color: Color
    card_type: CardType
    value: Optional[int] = None  # 0-9 for NUMBER, None for special
    
    def __repr__(self):
        if self.card_type == CardType.NUMBER:
            return f"{self.color.name} {self.value}"
        return f"{self.color.name} {self.card_type.name}"


# TODO: Implement your game however you like!
# This is just a suggested structure.

class UnoEnvironment:
    """Your Uno game environment"""
    
    def __init__(self, seed: Optional[int] = None):
        """Initialize game"""
        if seed is not None:
            random.seed(seed)
        # TODO: Your initialization
    
    def reset(self):
        """Start new game"""
        # TODO: Create deck, shuffle, deal cards
        pass
    
    def step(self, action):
        """Play a card"""
        # TODO: Apply action, update state, check win
        pass
    
    def get_valid_actions(self):
        """Get legal moves"""
        # TODO: Return list of playable cards
        pass


class RandomAgent:
    """Random agent baseline"""
    
    def select_action(self, state, valid_actions):
        """Pick random valid action"""
        # TODO: Return random choice from valid_actions
        pass


class QLearningAgent:
    """Q-learning agent"""
    
    def __init__(self, learning_rate=0.1, discount=0.9, epsilon=0.1):
        self.lr = learning_rate
        self.gamma = discount
        self.epsilon = epsilon
        self.q_table = {}
    
    def state_to_key(self, state):
        """Convert state to hashable key"""
        # TODO: Design your state representation!
        # This is the KEY challenge - what features matter?
        pass
    
    def select_action(self, state, valid_actions, training=True):
        """Epsilon-greedy action selection"""
        # TODO: Explore vs exploit
        pass
    
    def update(self, state, action, reward, next_state, done):
        """Q-learning update"""
        # TODO: Q(s,a) ← Q(s,a) + α[r + γ max Q(s',a') - Q(s,a)]
        pass


if __name__ == '__main__':
    # Quick test
    env = UnoEnvironment(seed=42)
    print("Environment created!")
    print("Now implement the methods :)")
