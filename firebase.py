import firebase_admin
from firebase_admin import credentials, firestore
import csv
from datetime import datetime, timedelta

# Initialize Firebase
cred = credentials.Certificate("/Users/namayjindal/Desktop/developer/fin-bytes/finbyte-8455a-firebase-adminsdk-nsdnj-2f479c6d45.json")
firebase_admin.initialize_app(cred)

# Reference to Firestore
db = firestore.client()

def calculate_week_number(signup_date):
    # Assuming your newsletters are sent every Sunday
    # Convert signup_date to a datetime object
    signup_date = datetime.strptime(signup_date, '%m/%d/%Y')

    # Calculate the difference in days from the signup date to the current date
    delta_days = (datetime.now() - signup_date).days

    # Calculate the week number
    week_number = delta_days // 7 + 1

    return week_number

# Add data to Firestore
def add_user(user_data):
    users_ref = db.collection('users')
    users_ref.add(user_data)

# Read CSV file and add user data to Firestore
csv_file_path = 'user_info.csv'  # Replace with the actual path
with open(csv_file_path, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Convert 'Submitted At' to a formatted date string (if needed)
        formatted_date = datetime.strptime(row['Submitted At'], '%m/%d/%Y %H:%M:%S').strftime('%m/%d/%Y')

        # Calculate week number
        week_number = calculate_week_number(formatted_date)

        # Example data (replace with actual CSV columns)
        user_data = {
            'name': f"{row['First name']} {row['Last name']}",
            'email': row['Email'],
            'experience_level': row['Experience Level'].lower(),
            'interest': row['Topics of Interest'],
            'form_date': formatted_date,
            'Week': week_number
        }

        # Add user data to Firestore
        add_user(user_data)

print('Users data added to Firestore successfully.')
