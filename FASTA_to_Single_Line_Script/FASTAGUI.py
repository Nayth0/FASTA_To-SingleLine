#This script can be ran to open a GUI for easier access to directories and file. (intended for 1 file at a time) 
import tkinter as tk
from tkinter import filedialog

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

def select_fasta_file():
    root = tk.Tk()
    root.withdraw()  

    input_file_path = filedialog.askopenfilename(
        title="Select FASTA File",
        filetypes=[("FASTA Files", "*.fasta"), ("All Files", "*.*")]
    )

    if input_file_path:
        output_file_path = filedialog.asksaveasfilename(
            defaultextension=".fasta",
            filetypes=[("FASTA Files", "*.fasta"), ("All Files", "*.*")],
            title="Save Converted FASTA File"
        )

        if output_file_path:
            fasta_to_single_line(input_file_path, output_file_path)

if __name__ == "__main__":
    select_fasta_file()
