import matplotlib.pyplot as plt


l=[10,8,7,7,7,7,7,7,6,6,6]

plt.plot(l)
plt.xlabel('--O')
plt.ylabel('iterations')
plt.title('Comparison number of iterations')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
