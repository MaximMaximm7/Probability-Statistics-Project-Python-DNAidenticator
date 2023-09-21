
import csv
import sys


def main():

    # TODO: Check for command-line usage

    if len(sys.argv) != 3:
        sys.exit("Usage: python dna.py databases/_____.csv sequences/____.txt")

    # TODO: Read database file into a variable
    # first command-line argument the name of a CSV file containing the STR counts for a list of individuals

    database = []
    first_command_line_argument = sys.argv[1]
    with open(first_command_line_argument, "r") as file:
        reader = csv.DictReader(file)
        for name in reader:
            database.append(name)

    # TODO: Read DNA sequence file into a variable
    # second command-line argument the name of a text file containing the DNA sequence to identify

    sequence = []
    second_command_line_argument = sys.argv[2]
    with open(second_command_line_argument, "r") as file:
        sequence = file.read()

    # TODO: Find longest match of each STR in DNA sequence
    # list() - creating a list
    # [1:] - Loop through, starting from first indexed element
    # .keys() - returns a list of all the available keys in the dictionary.
    # subsequences - all STRs
    subsequences = list(database[0].keys())[1:]

    # creating a dictionary for results
    results = {}
    for subsequence in subsequences:
        results[subsequence] = longest_match(sequence, subsequence)

    # TODO: Check database for matching profiles
    for name in database:
        count = 0
        for j in subsequences:
            # If there is one STR match add 1 to count
            if int(name[j]) == results[j]:
                count += 1

        # If the STR counts match exactly all STR
        # (AGATC,AATG,TATC) for 1 to 4: if count == 3:
        # for 5 to 20 (5-9 and 10-20): if count == int(sys.argv[2])[0:1] and [0:2]
        if count == len(subsequences):
            print(name['name'])

            sys.exit(0)

    # If there is no match
    print("No match")

    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
