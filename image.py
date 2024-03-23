import image
import numpy as np

img = Image.open('cabbage.jpg')

arr = np.asarray(img)
print(arr.shape)

numbers = []
for row in arr:
    temp = []
    for col in row:
        temp.append(str(col))
    numbers.append(temp)

with open('testImage.txt', 'w') as f:
    for row in numbers:
        f.write(','.join(row) + '\n')