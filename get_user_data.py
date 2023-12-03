import gspread

sa = gspread.service_account(filename="fin-bytes.json")
sh = sa.open("fin-bytes")

sheet = sh.worksheet("Investing Survey")

sheet_dict = sheet.get_all_records()
sheet_list = sheet.get_all_values()

#print(sheet_dict)
print(sheet_list)