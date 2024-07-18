import sys
import os
import cv2
import numpy as np
from matplotlib import pyplot as plt

def convert_to_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def invert_image(image):
    return cv2.bitwise_not(image)

def display_rgb_channels_bit_by_bit(image):
    bit_planes = { 'B': [], 'G': [], 'R': [] }
    for channel, color in zip(cv2.split(image), ('B', 'G', 'R')):
        for bit in range(8):
            bit_plane = (channel >> bit) & 1
            bit_planes[color].append(bit_plane * 255)
    return bit_planes

def save_images(output_dir, grayscale, inverted, bit_planes):
    os.makedirs(output_dir, exist_ok=True)

    cv2.imwrite(os.path.join(output_dir, 'grayscale.png'), grayscale)
    cv2.imwrite(os.path.join(output_dir, 'inverted.png'), inverted)

    for color, planes in bit_planes.items():
        for bit, plane in enumerate(planes):
            filename = f'{color}_bit_{bit}.png'
            cv2.imwrite(os.path.join(output_dir, filename), plane)

def main(inputfile, outputdirectory):
    image = cv2.imread(inputfile)
    if image is None:
        print(f"Error: Unable to open image file {inputfile}")
        return

    grayscale = convert_to_grayscale(image)
    inverted = invert_image(image)
    bit_planes = display_rgb_channels_bit_by_bit(image)

    save_images(outputdirectory, grayscale, inverted, bit_planes)

    print(f"Images saved in {outputdirectory}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python image-analysis.py <inputfile> <outputdirectory>")
    else:
        inputfile = sys.argv[1]
        outputdirectory = sys.argv[2]
        main(inputfile, outputdirectory)
