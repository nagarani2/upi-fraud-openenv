from upi_env import UPIFraudEnv
env = UPIFraudEnv()
for i in range(5):
    state = env.reset()
    print("\nTransaction:", state)

    action = input("Enter action (fraud/safe): ")

    _, reward, _, info = env.step(action)

    print("Correct:", info["correct"])
    print("Reward:", reward)