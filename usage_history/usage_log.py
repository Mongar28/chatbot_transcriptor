import csv
import os


def add_usage_history(data: dict):
    # Folder where the CSV file will be stored
    folder = "usage_logs"
    # Check if the folder exists, if not, create it
    if not os.path.exists(folder):
        os.makedirs(folder)

    # Path to the CSV file
    csv_path = os.path.join(folder, "usage_history.csv")

    # Check if the CSV file exists, if not, create it and write the header
    csv_exists = os.path.exists(csv_path)
    with open(csv_path, 'a', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        if not csv_exists:
            csv_writer.writerow(
                ["Username", "Document Name", "Audio Duration", "Audio Size", "Date"])

        # Write the data to the CSV file
        csv_writer.writerow([data["username"], data["document_name"],
                            data["audio_duration"], data["audio_size"], data["date"]])

    print("---> Se ha agregado al registro del archvio csv.")
