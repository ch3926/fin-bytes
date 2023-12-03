import firebase_admin
from firebase_admin import credentials, firestore
from datetime import datetime, timedelta

# Initialize Firebase
cred = credentials.Certificate("/Users/namayjindal/Desktop/developer/fin-bytes/finbyte-8455a-firebase-adminsdk-nsdnj-2f479c6d45.json")
firebase_admin.initialize_app(cred)

# Reference to Firestore
db = firestore.client()

def calculate_week_number(signup_date):
    # Assuming your newsletters are sent every Sunday
    # Calculate the difference in days from the signup date to the current date
    delta_days = (datetime.now() - signup_date).days

    # Calculate the week number
    week_number = delta_days // 7 + 1

    return week_number

# Add data to Firestore
def add_user(user_data):
    users_ref = db.collection('users')
    users_ref.add(user_data)

signup_date = '2023-04-01' # Replace with actual date format
week_number = calculate_week_number(signup_date)

# Example data
user_data = {
    'name': 'John Doe',
    'email': 'john@example.com',
    'experience_level': 'beginner',
    'interest': 'Stocks',
    'form_date': signup_date,  
    'Week': week_number
}

# Add user data to Firestore
add_user(user_data)
