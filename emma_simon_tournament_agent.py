#!/usr/bin/env python3
"""Tournament agent exported from Emma Simon's Unit 5 notebook.

The saved gene values and decision logic are based on the recorded output of
ImprovedEvolvableAgent after 100 generations. Run this in the course project,
where the provided agents.py module is available.
"""

import random
from agents import Agent, INVEST, UNDERCUT


class EmmaSimonAgent(Agent):
    """Ice Queen: cooperates with highly cooperative opponents and retaliates against defection.

    Saved evolved genes:
    [0.9970462326330012, 0.9747697307676272, 0.5775165988663097,
     0.2694337203265058, 0.5915625504553477, 0.7908011628894027]
    """

    def __init__(self):
        self.genes = [
            0.9970462326330012,
            0.9747697307676272,
            0.5775165988663097,
            0.2694337203265058,
            0.5915625504553477,
            0.7908011628894027,
        ]
        super().__init__(
            name="Ice Queen",
            description="Cooperates with highly cooperative opponents but retaliates against defection.",
        )

    def choose_action(self) -> bool:
        # Start cooperatively, using the first evolved gene.
        if self.round_num < 3:
            return random.random() < self.genes[0]

        # Review a recent window of the opponent's actions.
        memory_length = max(1, int(self.genes[4] * 10) + 1)
        recent_history = self.history[-memory_length:]
        if not recent_history:
            return random.random() < self.genes[0]
        cooperation_rate = sum(recent_history) / len(recent_history)

        # Reward highly cooperative opponents.
        if cooperation_rate > 0.8:
            return random.random() < self.genes[1]
        # Be more cautious with mixed behavior.
        elif cooperation_rate > 0.5:
            coop_prob = self.genes[1] * (cooperation_rate - 0.5) * 2
            return random.random() < coop_prob
        # Against mostly-defecting opponents, retaliate but allow occasional forgiveness.
        else:
            if random.random() < self.genes[3] * 0.3:
                return INVEST
            return UNDERCUT


def get_agent():
    """Factory function for tournament loaders that support get_agent()."""
    return EmmaSimonAgent()


if __name__ == "__main__":
    agent = get_agent()
    print(f"Agent loaded: {agent.name}")
    print(f"Genes: {agent.genes}")
    print(f"Description: {agent.description}")
