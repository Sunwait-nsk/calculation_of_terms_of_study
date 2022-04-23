def day_theory_func(theory: int) -> int:
    if theory % 8 == 0:
        result = theory // 8
    else:
        result = theory // 8 + 1
    return result


def pr_date(month: str) -> str:
    month_1 = month.split('.')
    month_2 = [month_1[2], month_1[1], month_1[0]]
    result = '.'.join(month_2)
    return result


day_list = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18",
            "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"]
month_list = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]


def dates(start_date: str, time_t: int, time_pr: int, hour_consul: int, hour_exz: int) -> tuple:
    with open("cal.txt", 'r') as name:
        text = name.read()
    result = text.split(", ")
    start_date = ".".join(start_date.split('.')[::-1])
    flag = 0
    total = 0  # все время. для расчета
    date_out = []
    date_pr = ''
    data_t = ''
    total_time = day_theory_func(time_t)
    day_consultation = day_theory_func(hour_consul)
    day_practice = day_theory_func(time_t - time_pr - hour_exz - hour_consul)
    day_theory = day_theory_func(time_pr)
    days = day_practice + day_theory + day_consultation + 1
    if days != total_time:
        print("не совпадает")
    for sym in result:
        if sym == start_date:
            flag = 1
            total = 8
            date_out.append(sym)
        else:
            if flag == 1:
                total += 8
                if total <= time_t:
                    date_out.append(sym)
                    if total == time_pr:
                        data_t = sym
                elif (time_t - total) <= 8:
                    date_out.append(sym)
                    flag = 0
    if total > time_pr:
        date_pr = date_out[len(date_out) - 3]
    print(" Теория с {} по {}".format(start_date, date_out[day_theory - 1]))
    print(" Практика с {} по {}".format(date_out[day_theory], date_pr))
    print(" Консультация {}".format(date_out[len(date_out) - 2]))
    print(" Экзамен {}".format(date_out[len(date_out) - 1]))
    result = (pr_date(start_date), pr_date(date_out[day_theory - 1]), pr_date(date_out[day_theory]), pr_date(date_pr),
              pr_date(date_out[len(date_out) - 2]), pr_date(date_out[len(date_out) - 1]), date_out, total_time, time_t)
    return result
