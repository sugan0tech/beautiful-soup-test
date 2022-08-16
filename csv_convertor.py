import xlrd
import csv
import json

def csv_from_excel():
    wb = xlrd.open_workbook('/home/sugan/Documents/GitHub/beautiful-soup-test/test.xlsx')
    sh = wb.sheet_by_name('Report 15 Complete')
    your_csv_file = open('/home/sugan/Documents/GitHub/beautiful-soup-test/output.csv', 'w', encoding='utf8')
    wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)

    for rownum in range(sh.nrows):
        wr.writerow(sh.row_values(rownum))

    your_csv_file.close()


data_dict = {}
with open("/home/sugan/Documents/GitHub/beautiful-soup-test/output.csv", encoding = 'utf-8') as csv_file_handler:
    csv_reader = csv.DictReader(csv_file_handler)
    sett = {"university Name","Website", "Area", "Year of Establishment", "Total Teachers", "Number of Study Centers", "Number of pg and off Campus Centers" , "Speciality", "Number of Departments", "No of Boys Hostel", "No of Girls Hostel", "Boys Hostel Intake Capacity", "Girls Hostel Intake Capacity"}
    for rows in csv_reader:
        print(rows)
        tmp = {}
        for input_factor in rows:
            if input_factor in sett:
                tmp[input_factor] = rows[input_factor]

        key = rows['AISHE Code']
        data_dict[key] = tmp

    with open("/home/sugan/Documents/GitHub/beautiful-soup-test/simpleData.json", 'w', encoding = 'utf-8') as json_file_handler:
        json_file_handler.write(json.dumps(data_dict, indent = 4))
