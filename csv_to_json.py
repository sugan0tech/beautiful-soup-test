import csv
import json

data_dict = {}


def to_int(s):
    if s == "":
        return 0
    return int(s)


with open("/home/sugan/Documents/SIH/datas in csv/college_basic_details.csv", encoding='utf-8') as csv_file_handler:
    csv_reader = csv.DictReader(csv_file_handler)
    sett = {"College Name", "Website", "Area", "Year of Establishment", "Total Teachers", "Number of Study Centers", "Number of pg and off Campus Centers",
            "Speciality", "Number of Departments"}
    for rows in csv_reader:
        print(rows)
        tmp = {}
        for input_factor in rows:
            tmp["Hostel Facility"] = to_int(
                rows["Boys Hostel Intake Capacity"])*0.5 + to_int(rows["Girls Hostel Intake Capacity"])*0.5
            tmp["Student Count"] = to_int(
                rows["No of Boys in Regular Course"]) + to_int(rows["No of Girls in Regular Course"])
            if input_factor in sett:
                tmp[input_factor] = rows[input_factor]

        key = rows['AISHE Code']
        data_dict[key] = tmp

    with open("/home/sugan/Documents/GitHub/beautiful-soup-test/college_basic_data.json", 'w', encoding='utf-8') as json_file_handler:
        json_file_handler.write(json.dumps(data_dict, indent=4))
