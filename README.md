# DataGenerator


purpose of creating this was because I wanted to be able to create test data whenever I wanted to. I picked up a python course and wanted to solve this issue of never having test data whenever I'm working. I know python is really powerful so figured might as well give it a shot. used https://faker.readthedocs.io/en/master/index.html documentation to figure out what variables I want, can mix and match or filter it in .csv.
Basically this removes the need for me to google and find 100000s of data sets to load into cloud enviornments for testing. 
Can be configured to add more, all you need to do is go to the faker website to verify what variables you need and simply add the fieldnames for the csv row 1 titles so if you have a new field add the "field name":, and then scroll down to the fake_data part and add the "field name": fake.insert_field_name_from_faker(), copy paste and repeat

no one shares this stuff for free on the web, why do i have to pay $39.99 for fake data that you made bro, I just want something for testing. and now I have it, feel free to download and make changes if you want. 

You must have python installed to run this app, run main.py and it shoould work



literally all you need to do is modify two lines of code.

# Specify the output folder and the number of rows you want in the CSV
output_folder = os.path.expanduser(r"C:\Users\username\Desktop\outputs")  # Use a raw string (r) or escape backslashes
num_rows = 10  # Change this to the desired number of rows

# Generate and write fake data to the CSV with a timestamp
generate_and_write_fake_data(output_folder, num_rows)
