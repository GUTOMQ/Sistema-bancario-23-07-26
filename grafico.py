import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y, color="blue", linestyle="--", marker="o")

plt.title("Meu primeiro gráfico")
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")

plt.show()