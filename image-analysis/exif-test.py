import exifread

def check_metadata(image_path):
    try:
        print(f"Opening image file: {image_path}")
        # Open image file for reading (binary mode)
        with open(image_path, 'rb') as f:
            print("File opened successfully.")
            # Return Exif tags
            tags = exifread.process_file(f)
            if not tags:
                print("No EXIF metadata found.")
                return
            print("EXIF Metadata:")
            for tag in tags.keys():
                print(f"{tag}: {tags[tag]}")
    except FileNotFoundError:
        print(f"File not found: {image_path}")
    except Exception as e:
        print(f"An error occurred while checking metadata: {e}")

def main():
    # Path to the image file to analyze
    image_path = 'example.jpg'  # Replace with your image file path

    # Check metadata
    check_metadata(image_path)

if __name__ == "__main__":
    main()
