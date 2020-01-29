# from: http://archive.ics.uci.edu/ml/datasets/EEG+Eye+State#

with open('EEG Eye State.arff.txt', 'r') as input_file:
    all_lines = input_file.readlines()

all_lines = all_lines[19:]

all_lines = list(map(lambda f: f.strip().split(','), all_lines))

all_lines_converted = [[int(float(word) * 100) for word in line] for line in all_lines]

import numpy as np

arr = np.array(all_lines_converted)

arr.tofile("numpy.binary")

# arr.max()
# max: 71589700 = 0x4 44 5F 44

import cv2
import numpy as np



arr_to_bytes = [
    [
        0xff & (value >> p)
        for value in row
        for p in [0, 8, 16, 24]

    ]
    for row in arr]

arr_to_bytes_np = np.array(arr_to_bytes)

cv2.imwrite("filename.png", arr_to_bytes_np)