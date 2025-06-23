import matplotlib.pyplot as plt
values = []
count=0
with open("data.txt", "r") as file:
    print(count)
    for line in file:
        if "Average:" in line:
            value_str = line.split("Average:")[1].strip()
            values.append(float(value_str))
            count+=1
        if count==11:
            print(values)
            values=[]
            count=0


