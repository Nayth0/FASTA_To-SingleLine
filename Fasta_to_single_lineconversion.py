

def fasta_to_single_line(input_file, output_file):
    try:
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

# Replace these filenames with your input and output file names as desired
input_file = 'input-file-name-here'
output_file = 'output-file-name-here'

fasta_to_single_line(input_file, output_file)

