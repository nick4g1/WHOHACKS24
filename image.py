from PIL import Image
import numpy as np

img = Image.open('cabbage.jpg')

arr = np.array(img)



scale_factor = 0.05
new_width = int(arr.shape[1] * scale_factor)
new_height = int(arr.shape[0] * scale_factor)
arr = np.array(Image.fromarray(arr).resize((new_width, new_height)))

print(new_width)
print(new_height)


def rgb_to_hex(rgb):
    return '0x{0:02x}{1:02x}{2:02x}'.format(int(rgb[0]), int(rgb[1]), int(rgb[2]))

reshaped_array = arr.reshape(-1, arr.shape[-1])
with open('testImage.txt', 'w') as f:
    for i in range(len(reshaped_array)):
        right = np.dot(reshaped_array[i], [0.2989, 0.5870, 0.1140])
        f.write(str(round(right)))
        f.write(", ")
        f.write(str(rgb_to_hex(reshaped_array[i])))
        f.write('\n')


#with open('testImage.txt', 'w') as f:
#    for row in reshaped_array:
#        f.write(str(row[0]))
#        f.write('\n')
