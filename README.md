# File-Analysis
# Image Analysis Script

## Overview

The Image Analysis Program is a versatile Python application designed to process and analyze images by generating various transformations and visualizations. This tool is particularly useful for educational purposes, image processing enthusiasts, and professionals needing detailed insights into image data. The program performs the following key functions:

1. **Grayscale Conversion**: Converts the input image to grayscale.
2. **Color Inversion**: Inverts the colors of the input image.
3. **Bitwise RGB Channel Analysis**: Extracts and visualizes each bit plane of the RGB channels, providing a detailed breakdown of the image's color information.

## Features

1. **Grayscale Conversion**
   - Converts the original image to a grayscale version, reducing the image to shades of gray. This is useful for simplifying the image and focusing on intensity variations.

2. **Color Inversion**
   - Inverts the colors of the original image. Each pixel's color value is reversed, providing a complementary color representation.

3. **Bitwise RGB Channel Analysis**
   - Splits the image into its Red, Green, and Blue channels.
   - Extracts each bit plane from the RGB channels, creating a series of binary images that represent the presence of each bit.
   - Provides a detailed view of the image's color information, broken down bit by bit.

## Usage

To run the Image Analysis Program, use the following command:

```sh
python image-analysis.py <inputfile> <outputdirectory>

