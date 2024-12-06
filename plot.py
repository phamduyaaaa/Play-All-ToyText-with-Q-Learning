import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Tham số rolling length
rolling_length = 1000

# Đọc dữ liệu từ CSV
data = pd.read_csv("reward_data.csv")

# Lấy giá trị rewards
rewards = data["Total Reward"].to_numpy()

# Tính rolling average
reward_moving_average = np.convolve(
    rewards, np.ones(rolling_length) / rolling_length, mode="valid"
)

# Vẽ biểu đồ
fig, ax = plt.subplots(figsize=(12, 5))
ax.set_title("Rolling Average of Rewards")
ax.plot(reward_moving_average, label="Rolling Average", color="orange")
ax.set_xlabel("Episode")
ax.set_ylabel("Reward")
ax.legend()

plt.tight_layout()
plt.show()
