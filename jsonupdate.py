import json
with open("/home/sugan/Documents/GitHub/beautiful-soup-test/output.json") as json_file:
    data = json.load(json_file)
    lst = sorted(data.items(), key = lambda x : int(float(x[1]["Total Teachers"])), reverse=True)
    for i in lst:
        tmp = i[1]
        print(tmp["AISHE Code"], tmp['university Name'], tmp["Type"], tmp['Total Teachers'])