
# Reinforcement Learning for Powerlifting Strategy Optimization

## 🏋️ Overview

This project explores the application of Reinforcement Learning (RL) to model and optimize decision-making in the sport of **powerlifting**. The RL agent is trained to select lift attempts (e.g., squat, bench press, deadlift) in a simulated competition environment, with the goal of maximizing performance under standard competition constraints.

We evaluate the RL agent’s strategies by **comparing its selected actions and performance to real-world powerlifting data** from actual competitions. This allows us to assess whether RL can replicate or surpass the strategies employed by elite lifters.

---

## 📊 Key Objectives

- Train an RL agent to simulate attempt selections in powerlifting meets.
- Evaluate the learned policy by comparing against historical lifter data.
- Analyze whether RL suggests riskier, safer, or more optimal strategies.
- Explore how varying the rules or success rates affects optimal decision-making.

---

## 🧠 Methodology

### 1. **Environment**
- Custom OpenAI Gym-style environment simulating a powerlifting meet.
- State includes current attempt number, previous success/failure, and total lifted weight.
- Actions represent attempt selections (i.e., how much weight to lift next).

### 2. **RL Agent**
- Algorithm: Proximal Policy Optimization (PPO) / DQN / A2C (choose one based on your project).
- Trained via simulations with reward shaping to reflect:
  - Total meet score (sum of best successful lifts)
  - Successful attempts
  - Miss penalties

### 3. **Real-World Dataset**
- Historical data from actual competitions (e.g., OpenPowerlifting.org).
- Includes:
  - Lifter bodyweight, weight class, meet attempts, final totals
  - Attempt outcomes (success/failure)
  - Placing in the competition

### 4. **Evaluation**
- Compare RL agent's decision paths against real lifters.
- Metrics:
  - Match rate between agent and real attempt selections
  - Total weight lifted vs actual lifters
  - Success rate of attempts
  - Placement simulation (if competing virtually against real lifters)


---

## 🧪 Example Analysis

- Does the RL agent suggest more aggressive third attempts than real lifters?
- How does success rate compare between RL agent and top 10 finishers?
- What would happen if real lifters followed the RL policy?

---
## 📚 Citation and Dataset Source

If you're using publicly available data (e.g., OpenPowerlifting), include a citation here:

> Data sourced from [OpenPowerlifting.org](https://www.openpowerlifting.org)

---

## 🙋‍♂️ About

Developed by **Takunda Danha** as part of a research project exploring decision-making and optimization in strength sports using AI.

Supervised by Dr Johnathan Kariv, University of the Witwatersrand.


