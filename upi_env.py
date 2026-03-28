import random

class UPIFraudEnv:
    def __init__(self):
        self.transactions = [
            {"amount": 500, "time": 10, "location": "home", "device": "mobile"},
            {"amount": 45000, "time": 2, "location": "new_city", "device": "unknown"},
            {"amount": 1500, "time": 14, "location": "home", "device": "mobile"},
            {"amount": 60000, "time": 1, "location": "new_city", "device": "unknown"},
        ]
        self.current = None

    def reset(self):
        self.current = random.choice(self.transactions)
        return self.current

    def state(self):
        return self.current

    def check_fraud(self, txn):
        score = 0

        if txn["amount"] > 30000:
            score += 1
        if txn["time"] < 5:
            score += 1
        if txn["location"] == "new_city":
            score += 1
        if txn["device"] == "unknown":
            score += 1

        return "fraud" if score >= 2 else "safe"

    def step(self, action):
        correct = self.check_fraud(self.current)

        if action == correct:
            reward = 10
        else:
            reward = -10

        done = True
        return self.current, reward, done, {"correct": correct}