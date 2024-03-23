import PIL.Image
import numpy as np

img = PIL.Image.open('cabbage.jpg')

arr = np.array(img)
scale_factor = 0.02
new_width = int(arr.shape[1] * scale_factor)
new_height = int(arr.shape[0] * scale_factor)
arr = np.array(PIL.Image.fromarray(arr).resize((new_width, new_height)))
reshaped_array = arr.reshape(-1, arr.shape[-1])

with open('testImage.txt', 'w') as f:
    for row in reshaped_array:
        f.write(str(row[0]))
        f.write('\n')
