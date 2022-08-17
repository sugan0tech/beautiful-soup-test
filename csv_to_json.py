import csv
import json

data_dict = {}


def to_int(s):
    if s == "":
        return 0
    return int(s)


stu_count_max = 0
teacher_count_max = 0
hostel_max = 0
dept_max = 0

with open("/home/sugan/Documents/SIH/datas in csv/college_basic_details.csv", encoding='utf-8') as csv_file_handler:
    csv_reader = csv.DictReader(csv_file_handler)
    for rows in csv_reader:
        tmp = {}
        for input_factor in rows:
            tmp["Hostel Facility"] = to_int(
                rows["Boys Hostel Intake Capacity"])*0.5 + to_int(rows["Girls Hostel Intake Capacity"])*0.5
            tmp["Student Count"] = to_int(
                rows["No of Boys in Regular Course"]) + to_int(rows["No of Girls in Regular Course"])
        stu_count_max = max(stu_count_max, to_int(tmp["Student Count"]))
        teacher_count_max = max(stu_count_max, to_int(rows["Total Teachers"]))
        hostel_max = max(hostel_max, to_int(tmp["Hostel Facility"]))
        dept_max = max(dept_max, to_int(rows["Number of Departments"]))

print(stu_count_max, teacher_count_max, hostel_max)

with open("/home/sugan/Documents/SIH/datas in csv/college_basic_details.csv", encoding='utf-8') as csv_file_handler:
    csv_reader = csv.DictReader(csv_file_handler)
    sett = {"AISHE Code", "College Name", "Website", "Area", "Year of Establishment", "Total Teachers", "Number of Study Centers", "Number of pg and off Campus Centers",
            "Speciality", "Number of Departments"}
    m = 0

    for rows in csv_reader:
        tmp = {}
        print(rows)
        for input_factor in rows:
            tmp["Hostel Facility"] = to_int(
                rows["Boys Hostel Intake Capacity"])*0.5 + to_int(rows["Girls Hostel Intake Capacity"])*0.5
            tmp["Student Count"] = to_int(
                rows["No of Boys in Regular Course"]) + to_int(rows["No of Girls in Regular Course"])
            if input_factor in sett:
                tmp[input_factor] = rows[input_factor]

        stu_countf = to_int(tmp["Student Count"])/stu_count_max
        teacher_countf = to_int(tmp["Total Teachers"])/teacher_count_max
        hostelf = to_int(tmp["Hostel Facility"])/hostel_max
        deptf = to_int(tmp["Number of Departments"])/dept_max
        print(stu_countf, teacher_countf, hostelf)

        tmp["Score"] = stu_countf*35 + \
            teacher_countf*35 + hostelf*10 + deptf*20
        key = rows['AISHE Code']
        data_dict[key] = tmp

    with open("/home/sugan/Documents/GitHub/beautiful-soup-test/college_basic_data.json", 'w', encoding='utf-8') as json_file_handler:
        json_file_handler.write(json.dumps(data_dict, indent=4))
