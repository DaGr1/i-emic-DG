import matplotlib.pyplot as plt

data = {}
current_header = None
current_block = []

with open("data.txt", "r") as file:
    for line in file:
        line = line.strip()
        if line.endswith(".xml"):
            current_header = line
            data[current_header] = []
        elif line.startswith("--O="):
            if current_block:
                # Compute average of the last block and store
                avg = sum(current_block) / len(current_block)
                data[current_header].append(avg)
                current_block = []
        elif line:
            # Data line: add values to current block
            values = [float(x) for x in line.split()]
            current_block.extend(values)

    # Don't forget the last block
    if current_block:
        avg = sum(current_block) / len(current_block)
        data[current_header].append(avg)

# Optional: print result
for header, averages in data.items():
    print(averages)
