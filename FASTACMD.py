import argparse
import os

def ensure_extension(filename, extension):
    # Ensure that the filename ends with the specified extension
    if not filename.endswith(extension):
        filename += extension
    return filename

def combine_filenames(input_files):
    # Combine the base names of input files
    base_names = [os.path.splitext(os.path.basename(file))[0] for file in input_files]
    return "_".join(base_names) + "_single_line.fasta"

def fasta_to_single_line(input_files, output_file=None):
    try:
        if not output_file:
            # If output_file is not provided, generate a default name based on input file names
            output_file = combine_filenames(input_files)
        else:
            # Ensure that the output file has the .fasta extension
            output_file = ensure_extension(output_file, '.fasta')

        with open(output_file, 'w') as output_fasta:
            for input_file in input_files:
                with open(input_file, 'r') as input_fasta:
                    sequence = ""
                    for line in input_fasta:
                        line = line.strip()
                        if line.startswith('>'):
                            # If it's a header line, write the previous sequence (if any)
                            if sequence:
                                output_fasta.write(sequence + '\n')
                            output_fasta.write(line + '\n')  # Write the header line
                            sequence = ""  # Reset the sequence
                        else:
                            sequence += line  # Concatenate sequence lines

                    # Write the last sequence (if any)
                    if sequence:
                        output_fasta.write(sequence + '\n')
        
        print(f"Conversion complete. Output written to '{output_file}'")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def main():
    parser = argparse.ArgumentParser(description='Convert FASTA files to single-line format and combine them into a single output file.')
    parser.add_argument('-i', '--input', nargs='+', required=True, help='Input FASTA file(s)')
    parser.add_argument('-o', '--output', help='Output FASTA file (default: combined input file names)')

    args = parser.parse_args()
    input_files = args.input
    output_file = args.output

    if not output_file:
        # Use the default output file name based on input file names
        output_file = combine_filenames(input_files)
    else:
        # Ensure that the output file has the .fasta extension
        output_file = ensure_extension(output_file, '.fasta')

    fasta_to_single_line(input_files, output_file)

if __name__ == '__main__':
    main()
