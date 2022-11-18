
import json
import sys
import matplotlib.pyplot as plt
filename = sys.argv[1]
if __name__ == "__main__":
    with open(filename) as f:
        data = f.read()
        print(data)
    js = json.loads(data)

    keys = []
    values = []
    for element in js:
        keys.append(element["Key"])
        values.append(element["Value"])


    plt.bar(keys, values)
    plt.show()