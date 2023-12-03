import time

start = time.time()

f = open("input", "r")

finalSum = 0
lines = f.readlines()

for line in lines:

    line = line.strip()

    lineChars = []
    lineNum = 0

    for c in line:
        if c.isdigit():
            lineChars.append(str(c))

    if len(lineChars) > 0:
        print(line)
        print(f"{lineChars[0]} | {lineChars[-1]}")
        lineNum += int(lineChars[0] + lineChars[-1])
        print(lineNum)

        finalSum += int(lineNum)

        print(finalSum)

print(finalSum)

finish = time.time()

print(f"\nCompute time: {str(finish - start)} seconds")
