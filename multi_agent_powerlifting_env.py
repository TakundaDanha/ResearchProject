import gym
import numpy as np
import random

class MultiAgentPowerliftingEnv(gym.Env):
    def __init__(self, num_agents=9):
        super(MultiAgentPowerliftingEnv, self).__init__()
        self.num_agents = num_agents
        self.agents = [
            {"MaxSquat": random.randint(180, 300), 
             "MaxBench": random.randint(120, 200), 
             "MaxDeadlift": random.randint(200, 350), 
             "AttemptsLeft": 9, "TotalKg": 0}
            for _ in range(self.num_agents)
        ]
        self.current_agent = 0  # Index of the agent taking their turn
        self.current_lift = "Squat"  # Current lift type: Squat -> Bench -> Deadlift
        self.action_space = gym.spaces.Discrete(100)  # Action: Attempt weight (0-100kg for simplicity)
        self.observation_space = gym.spaces.Box(
            low=0, high=np.inf, shape=(self.num_agents * 5,)  # Max lifts, attempts left, total
        )

    def reset(self):
        """Reset the environment."""
        self.agents = [
            {"MaxSquat": random.randint(180, 300), 
             "MaxBench": random.randint(120, 200), 
             "MaxDeadlift": random.randint(200, 350), 
             "AttemptsLeft": 9, "TotalKg": 0}
            for _ in range(self.num_agents)
        ]
        self.current_agent = 0
        self.current_lift = "Squat"
        return self._get_observation()

    def step(self, action):
        """Perform a step for the current agent."""
        agent = self.agents[self.current_agent]
        max_lift = agent[f"Max{self.current_lift}"]

        # Constrain action to the agent's max lift
        if action > max_lift:
            action = max_lift  # Cap action to max lift

        success = random.choice([0, 1])  # Random success/failure
        if success:
            agent["TotalKg"] += action  # Update total for successful lift
        agent["AttemptsLeft"] -= 1

        # Cycle through lifts: Squat -> Bench -> Deadlift
        if agent["AttemptsLeft"] % 3 == 0:
            self.current_lift = {
                "Squat": "Bench", "Bench": "Deadlift", "Deadlift": "Squat"
            }[self.current_lift]

        # Update to the next agent
        self.current_agent = (self.current_agent + 1) % self.num_agents
        done = all(a["AttemptsLeft"] == 0 for a in self.agents)  # Check if all agents are done

        reward = action if success else -action * 0.5  # Reward for success, penalty for failure
        return self._get_observation(), reward, done, {}

    def _get_observation(self):
        """Return observation: [MaxSquat, MaxBench, MaxDeadlift, AttemptsLeft, TotalKg] for all agents."""
        return np.array([
            [a["MaxSquat"], a["MaxBench"], a["MaxDeadlift"], a["AttemptsLeft"], a["TotalKg"]]
            for a in self.agents
        ]).flatten()

    def render(self, mode='human'):
        for i, agent in enumerate(self.agents):
            print(f"Agent {i+1}: {agent}")
