import argparse

def fasta_to_single_line(input_files, output_file):
    try:
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
    parser.add_argument('-o', '--output', required=True, help='Output FASTA file')

    args = parser.parse_args()
    input_files = args.input
    output_file = args.output

    fasta_to_single_line(input_files, output_file)

if __name__ == '__main__':
    main()
