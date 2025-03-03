import os
import csv


def csv_appender(name, data):
    path = r"C:\Users\Abdallah Mohamed\Desktop\Jobs"
    csv_path = os.path.join(path, 'page' + name + '.csv')

    # Check if the file exists
    file_exists = os.path.exists(csv_path)

    with open(csv_path, 'a', newline='') as csvfile:
        fieldnames = ['Company Names', 'Years of experience', 'Skills', 'Locations', 'Salaries', 'Links']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Write header only if the file does not exist
        if not file_exists:
            writer.writeheader()

        writer.writerow(data)
    print(f"Data has been appended to {csv_path} successfully✅")