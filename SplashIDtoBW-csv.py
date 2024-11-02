#  SplashIDtoBW-csv.py
#  Format conversion tool to read SplashId CSV and generate a Bitwarden CSV import file.
# This will convert all fields, but does not include any attached files for a SplashId record.
# The field column names are lost when the CSV is created.
# The fields will be recreated as Field1, Field2,Field3,Field4, and Field5
# The Date when that SplashId record was updated will have the field name "Last_Updated"
#
'''
 Glenn Seaton 2024
 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
 WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
 CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

 '''
import csv
import tkinter as tk
from tkinter import filedialog

# Function to get input file from the user
def get_input_file():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    file_path = filedialog.askopenfilename(
        title="Select the SplashId CSV file to convert:",
        filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
    )
    return file_path

print("Convert SplashId csv to Bitwarden csv format.")
print('To import into Bitwarden select file format "Bitwarden (csv)".')

# Define input and output CSV file paths
# Ask the user to select an input file
input_file = get_input_file()
output_file = 'output.csv'

# Column names based on user requirements
column_names = [
    'type', 'name', 'login_username', 'login_password', 'login_uri',
    'field1', 'field2', 'field3', 'field4', 'field5',
    'Last_Updated', 'notes', 'folder'
]

# Define new column names and map fields
new_columns = [
    'folder', 'favorite', 'type', 'name', 'notes', 'fields',
    'reprompt', 'login_uri', 'login_username', 'login_password', 'login_totp'
]

# Read and process the CSV
with open(input_file, mode='r', newline='') as infile:
    #reader = csv.DictReader(infile)
    reader = csv.DictReader(infile, fieldnames=column_names)
    # Skip the header row
    next(reader)

    # Prepare data for output
    output_data = []
    for row in reader:
        # Create a dictionary for each 'fields' entry as key-value pairs
        fields = {
            'field1': row['field1'],
            'field2': row['field2'],
            'field3': row['field3'],
            'field4': row['field4'],
            'field5': row['field5'],
            'Last_Updated': row['Last_Updated']
        }
        # Filter out any fields with blank values
        filtered_fields = {k: v for k, v in fields.items() if v.strip()}
        #
        # Filter brackets and  single quotes from array
        # replace comma separator with newline character
        fieldsout = str(filtered_fields)
        fieldsout = fieldsout.replace("{",'')
        fieldsout = fieldsout.replace("}",'')
        fieldsout = fieldsout.replace("'","")
        fieldsout = fieldsout.replace(",","\n")

        # SplashId export Vertical Tab as new line in Notes Field
        # Replace Vertical Tab character with  NewLine character
        notesfield = row['notes']
        notesfield = notesfield.replace("\x0B","\n" )

        # Map new columns to row values, with fields as JSON-like text
        output_row = {
            'folder': row['folder'],
            'favorite': '',  # Placeholder for undefined column
            'type': row['type'],
            'name': row['name'],
            'notes': notesfield,
            'fields': fieldsout,  # Convert fields dictionary to string
            'reprompt': '',  # Placeholder for undefined column
            'login_uri': row['login_uri'],
            'login_username': row['login_username'],
            'login_password': row['login_password'],
            'login_totp': ''  # Placeholder for undefined column
        }
        output_data.append(output_row)

# Write to the new CSV file
with open(output_file, mode='w', newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=new_columns)
    writer.writeheader()
    writer.writerows(output_data)

print(f"Data written to {output_file}")
