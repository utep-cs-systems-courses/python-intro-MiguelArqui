import re
import sys

def count_words(input_file, output_file):
    word_counts = {}
    
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            text = file.read()
    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")
        return

    # Remove punctuation and split the text into words
    words = re.findall(r'\b\w+\b', text.lower())

    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    # Sort the word counts in descending order
    sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

    try:
        with open(output_file, 'w', encoding='utf-8') as file:
            for word, count in sorted_word_counts:
                file.write(f"{word} {count}\n")
    except IOError:
        print(f"Error: Unable to write to output file '{output_file}'.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python wordCount.py input.txt output.txt")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        count_words(input_file, output_file)
        print(f"Word count completed. Results saved to '{output_file}'.")
