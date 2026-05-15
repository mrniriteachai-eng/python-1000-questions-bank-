import matplotlib.pyplot as plt

x = [1, 2, 3, 4]

y1 = [2, 4, 6, 8]   # Line 1
y2 = [1, 3, 5, 7]   # Line 2

plt.plot(x, y1, label="Line 1")
plt.plot(x, y2, label="Line 2")

plt.legend()

plt.title("Multiple Lines Graph")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

plt.show()