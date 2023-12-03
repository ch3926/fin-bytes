import gspread
import json

sa = gspread.service_account(filename="fin-bytes.json") # service account to use for api
sh = sa.open("fin-bytes") # the google sheet containing all the user entered data
sheet = sh.worksheet("Investing Survey") # specific sheet containing the data

# grab user entered records from spreadsheet so we can use them here
sheet_dict = sheet.get_all_records()
sheet_list = sheet.get_all_values()

#print(sheet_dict)
#print(sheet_list)

# convert list of dict values into json
# json_info = json.dumps(sheet_dict)
# print(json_info)
