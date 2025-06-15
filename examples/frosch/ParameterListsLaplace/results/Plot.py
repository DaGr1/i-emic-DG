import matplotlib.pyplot as plt
import ast

all_lists = []
with open("List.txt", "r") as file:
    lines = [line.strip() for line in file if line.strip()]


with open("lists.txt", "r") as f:
    for line in f:
        if line.strip():
            try:
                lst = ast.literal_eval(line.strip())
                all_lists.append(lst)
            except Exception as e:
                print(f"Skipping line due to error: {e}")


for idx, data in enumerate(all_lists):
    plt.plot(data, label=lines[idx])

plt.xlabel('--O')
plt.ylabel('time taken(s)')
plt.title('Comparison of time taken')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
