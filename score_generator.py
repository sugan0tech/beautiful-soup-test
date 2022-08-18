import csv
import json
from re import T


def to_int(s):
    if s == "":
        return 0
    return int(s)


"""
    Getting data from Infrastructure.csv
"""
infrastructure_data = {}
with open("/home/sugan/Documents/SIH/datas in csv/infrastructure.csv", encoding='utf-8') as csv_file_handler:
    csv_reader = csv.DictReader(csv_file_handler)
    infra_set = {
        "library",
        "laboratory",
        "conference_hall",
        "computer_center",
        "no_of_books",
        "no_of_journals",
        "no_of_laboratories",
        "no_of_computer_centers",
        "no_of_libraries"
    }
    tmp = {}
    for rows in csv_reader:
        key = rows['id']
        for infra_key in infra_set:
            tmp[infra_key] = rows[infra_key]
        infrastructure_data[key] = tmp
        tmp = {}

"""
    Getting data from CollegeInstitution.csv
"""
college_institution_data = {}
with open("/home/sugan/Documents/SIH/datas in csv/college_institution.csv", encoding='utf-8') as csv_file_handler:
    csv_reader = csv.DictReader(csv_file_handler)
    college_set = {
        "aishe_code",
        "city",
        "state_code",
        "location",
        "infrastructure_id",
        "latitude",
        "longitude",
        "offers_scholarship"
    }
    tmp = {}
    for rows in csv_reader:
        key = rows['aishe_code']
        infra_key = rows['infrastructure_id']
        for college_key in college_set:
            tmp[college_key] = rows[college_key]

        college_institution_data[key] = tmp
        tmp = {}

"""
    generating max value for each fields 
"""
stu_count_max = 0
teacher_count_max = 0
hostel_max = 0
dept_max = 0
data_dict = {}
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
        tmp = {}


"""
    Finally generating score based on generated Normalized data to finalScoring.json
"""

with open("/home/sugan/Documents/SIH/datas in csv/college_basic_details.csv", encoding='utf-8') as csv_file_handler:
    csv_reader = csv.DictReader(csv_file_handler)
    sett = {"AISHE Code", "College Name", "Website", "Area", "Year of Establishment", "Total Teachers", "Number of Study Centers", "Number of pg and off Campus Centers",
            "Speciality", "Number of Departments"}
    m = 0

    for rows in csv_reader:
        tmp = {}
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
        # print(stu_countf, teacher_countf, hostelf)

        tmp["Score"] = stu_countf*35 + \
            teacher_countf*35 + hostelf*10 + deptf*20
        key = rows['AISHE Code']

        try:
            for college_keys in college_institution_data[key]:
                tmp[college_keys] = college_institution_data[key][college_keys]
            data_dict[key] = tmp

            infra_id = college_institution_data[key]["infrastructure_id"]
            for infra_keys in infrastructure_data[infra_id]:
                tmp[infra_keys] = infrastructure_data[infra_id][infra_keys]
        except:
            pass

        tmp = {}

    with open("/home/sugan/Documents/GitHub/beautiful-soup-test/finalScoring.json", 'w', encoding='utf-8') as json_file_handler:
        json_file_handler.write(json.dumps(data_dict, indent=4))
