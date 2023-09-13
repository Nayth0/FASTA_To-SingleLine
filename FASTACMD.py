import argparse

def fasta_to_single_line(input_file, output_file=None):
    try:
        if not output_file:
            # If output_file is not provided, generate a default name based on the input file
            output_file = f"{input_file}.single_line.fasta"

        with open(input_file, 'r') as input_fasta, open(output_file, 'w') as output_fasta:
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
    parser = argparse.ArgumentParser(description='Convert a FASTA file to single-line format.')
    parser.add_argument('-i', '--input', required=True, help='Input FASTA file')
    parser.add_argument('-o', '--output', help='Output FASTA file (default: input.single_line.fasta)')

    args = parser.parse_args()
    input_file = args.input
    output_file = args.output

    fasta_to_single_line(input_file, output_file)

if __name__ == '__main__':
    main()
