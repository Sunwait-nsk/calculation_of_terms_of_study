import requests


day_list = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18",
            "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"]
month_list = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]

year = '2022'
date2 = []
date_str = ''
for mon in month_list:
    for d in day_list:
        day_now = year + mon + d
        req = "https://isdayoff.ru/" + day_now
        my_req = requests.get(req)
        if int(my_req.text) < 100:
            if int(my_req.text) == 0:
                pr = (".".join([year, mon, d]))
                if pr in date2:
                    pass
                else:
                    date2.append(pr)
                    date_str += pr + ", "

with open("cal.txt", 'w') as f:
    f.write(date_str)