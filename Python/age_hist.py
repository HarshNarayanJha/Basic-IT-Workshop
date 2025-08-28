import matplotlib.pyplot as plt

ages = [21, 54, 66, 44, 32, 42, 54, 62, 93, 45, 32, 70]
average_age = sum(ages) / len(ages)

plt.hist(ages, bins=10)
plt.axvline(
    average_age,
    color="red",
    linestyle="dashed",
    linewidth=2,
    label=f"Average Age: {average_age:.2f}",
)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()
