import csv
import os

def write_text_to_csv():
    # Text to be written to the CSV file
    text_lines = [
        "This is the first line of text.",
        "Here is the second line.",
        "And finally, the third line."
    ]

    # Specify the location for the CSV file
    csv_file_path = 'F:\\formatedHar\\sample_text.csv'

    # Ensure the directory exists, create if not
    os.makedirs(os.path.dirname(csv_file_path), exist_ok=True)

    # Delete and recreate the file if it already exists
    if os.path.exists(csv_file_path):
        os.remove(csv_file_path)
        print(f"Existing file '{csv_file_path}' deleted.")

    # Store text in a CSV file
    with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
        # Use the csv.writer to write lines
        csv_writer = csv.writer(csvfile)

        # Write each line to the CSV file
        for line in text_lines:
            csv_writer.writerow([line])

    print(f"Text has been saved to: {os.path.abspath(csv_file_path)}")

# Call the function to write text to CSV
write_text_to_csv()
