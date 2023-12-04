import csv
from faker import Faker
from datetime import datetime

# Function to generate and write fake data to a CSV file with a timestamp
def generate_and_write_fake_data(num_rows):
    fake = Faker()

    # Specify the fieldnames for the CSV, rewrite the names to match your primary/f-keys, filenames impact your csv cell row A so this makes it easier to export into a db.
    fieldnames = [
        "Name",
        "Building Number",
        "Street Address",
        "Street Name",
        "Street Suffix",
        "City",
        "Postcode",
        "Country",
        "Country Code",
        "Job",
        "Social Security Number",
        "Currency",
        "Bank",
        "Bank IBAN",
        "Bank SWIFT-Branch/Office",
        "Bank SWIFT-11 digit",
        "Credit Card Provider",
        "Credit Card Number",
        "CC Security Code",
        "CC Expire",
        "CC Full",
        "IPv4 Public",
        "IPv4 Private",  # Corrected field name
    ]

    # Get the current timestamp
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

    # Define the CSV filename with the timestamp
    csv_filename = f"fake_data_{timestamp}.csv"

    with open(csv_filename, mode="w", newline="", encoding="utf-8") as csv_file:  # Specify UTF-8 encoding
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        # Write the header row
        writer.writeheader()

        # Generate and write fake data for the specified number of rows
        for _ in range(num_rows):
            fake_data = {
                "Name": fake.name(),
                "Building Number": fake.building_number(),
                "Street Address": fake.street_address(),
                "Street Name": fake.street_name(),
                "Street Suffix": fake.street_suffix(),
                "City": fake.city(),
                "Postcode": fake.postcode(),
                "Country": fake.country(),
                "Country Code": fake.country_code(),
                "Job": fake.job(),
                "Social Security Number": fake.ssn(),
                "Currency": fake.currency(),
                "Bank": fake.bank_country(),
                "Bank IBAN": fake.iban(),
                "Bank SWIFT-Branch/Office": fake.swift(length=8, use_dataset=True),
                "Bank SWIFT-11 digit": fake.swift(length=11, use_dataset=True),
                "Credit Card Provider": fake.credit_card_provider(),
                "Credit Card Number": fake.credit_card_number(card_type="discover"),
                "CC Security Code": fake.credit_card_security_code(card_type="discover"),
                "CC Expire": fake.credit_card_expire(),
                "CC Full": fake.credit_card_full(card_type="discover"),
                "IPv4 Public": fake.ipv4_public(),
                "IPv4 Private": fake.ipv4_private(),  # Corrected field name
            }

            # Write the data row
            writer.writerow(fake_data)

    print(f"Fake data written to {csv_filename}")

# Specify the number of rows you want in the CSV
num_rows = 10  # Change this to the desired number of rows

# Generate and write fake data to the CSV with a timestamp
generate_and_write_fake_data(num_rows)
