import sys
import os
import configparser

def load_signatures(config_file):
    config = configparser.ConfigParser()
    config.read(config_file)

    signatures = {}
    for section in config.sections():
        for file_type, value in config.items(section):
            header, footer = value.split(':')
            header = bytes.fromhex(header.strip())
            footer = bytes.fromhex(footer.strip()) if footer.strip() else b''
            signatures[file_type] = {'header': header, 'footer': footer}
    
    return signatures

def carve_files(input_file, output_dir, signatures):
    with open(input_file, 'rb') as f:
        data = f.read()

    os.makedirs(output_dir, exist_ok=True)

    for file_type, sig in signatures.items():
        header = sig['header']
        footer = sig['footer']
        start = 0

        while True:
            start = data.find(header, start)
            if start == -1:
                break

            if footer:
                end = data.find(footer, start + len(header))
                if end == -1:
                    break
                end += len(footer)
            else:
                end = start + 1024  # Adjust this as needed

            file_data = data[start:end]
            output_file = os.path.join(output_dir, f'{file_type}_{start:08X}.{file_type}')
            with open(output_file, 'wb') as out_f:
                out_f.write(file_data)
            
            print(f"Extracted {file_type} file from offset {start} to {end}, saved as {output_file}")

            start = end

    print(f"Files carved to {output_dir}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python file_carver.py <inputfile> <outputdirectory> <configfile>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_dir = sys.argv[2]
    config_file = sys.argv[3]

    signatures = load_signatures(config_file)
    carve_files(input_file, output_dir, signatures)

# Note about usage:
# To run this script for file carving, use the following command:
# python file_carver.py <inputfile> <outputdirectory> signatures.conf
# Replace <inputfile> with the path to your binary file.
# Replace <outputdirectory> with the path to the directory where carved files should be saved.
# Replace signatures.conf with the path to your configuration file.
