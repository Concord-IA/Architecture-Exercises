"""
Training Script - Example

Modify this to train your Q-learning agent!
"""

# TODO: Import your environment and agents
# from your_uno import UnoEnvironment, RandomAgent, QLearningAgent


def train_agent(episodes=10000):
    """Train Q-learning agent"""
    print(f"TODO: Train Q-learning agent for {episodes} episodes")
    print("\nYour training loop should:")
    print("1. Create environment and agents (Q-learner vs Random)")
    print("2. For each episode:")
    print("   - Reset game")
    print("   - Play until done")
    print("   - Update Q-values after each step")
    print("   - Track wins")
    print("3. Decay epsilon over time")
    print("4. Print progress every 1000 games")
    print("5. Save trained Q-table")
    
    # Example structure:
    # env = UnoEnvironment(seed=42)
    # q_agent = QLearningAgent(learning_rate=0.1, discount=0.9, epsilon=0.5)
    # random_agent = RandomAgent()
    # 
    # wins = 0
    # for episode in range(episodes):
    #     state = env.reset()
    #     
    #     while True:
    #         valid_actions = env.get_valid_actions()
    #         
    #         # Current player picks action
    #         if current_player == 0:  # Q-learner
    #             action = q_agent.select_action(state, valid_actions)
    #         else:  # Random
    #             action = random_agent.select_action(state, valid_actions)
    #         
    #         next_state, reward, done = env.step(action)
    #         
    #         # Update Q-learner
    #         if current_player == 0:
    #             q_agent.update(state, action, reward, next_state, done)
    #         
    #         if done:
    #             if reward > 0:  # Q-learner won
    #                 wins += 1
    #             break
    #         
    #         state = next_state
    #     
    #     # Decay epsilon
    #     q_agent.epsilon = max(0.01, q_agent.epsilon * 0.995)
    #     
    #     if (episode + 1) % 1000 == 0:
    #         print(f"Episode {episode+1}: Win rate = {wins/1000:.2%}, Epsilon = {q_agent.epsilon:.3f}")
    #         wins = 0


if __name__ == '__main__':
    print("Uno Q-Learning Training")
    print("=" * 40)
    train_agent(episodes=10000)
