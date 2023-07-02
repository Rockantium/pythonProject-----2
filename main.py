import csv

def word_frequencies(file_name):
    frequencies = {}
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            for word in row:
                word = word.strip()
                if word not in frequencies:
                    frequencies[word] = 1
                else:
                    frequencies[word] += 1

    for word, frequency in frequencies.items():
        print(word, frequency)

# Read the input file name from the user
file_name = input()

# Call the function to calculate and display word frequencies
word_frequencies(file_name)
