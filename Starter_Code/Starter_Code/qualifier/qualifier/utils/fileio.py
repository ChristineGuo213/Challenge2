# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv


def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data


def save_csv(csvpath,qualifying_loans,header=None):
    """Writes the CSV file to the one named qualifying_loans.

    Args:
        csvpath (Path): The csv file path.

    Prints:
        Confirmation that the date has been saved a CSV file with all the qualifying loans informatin. 

    """
    with open(csvpath, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        if header:

            # Write the header row first
            csvwriter.writerow(header)

        # Write data rows    
        csvwriter.writerows(qualifying_loans)
    
        # If user wants to save CSV file, print the following statement after CSV file is saved.
        print("Thank you for submitting your information. The data has been saved.")
    
