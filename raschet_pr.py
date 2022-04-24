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


def result_dates(day: str, month: str, dates: list) -> list:
    flag = 0
    result = []

    for symbol in dates:

        month_dates = symbol.split('.')[1]
        day_dates = symbol.split('.')[2]
        if int(month_dates) == int(month) and int(day_dates) == int(day):
            flag = 1
            result.append(symbol)
        elif flag == 1:
            result.append(symbol)
    return result


def result_dates_out(time_t: int, result_1: list) -> list:
    hours = 0
    if time_t % 8 != 0:
        time_total = (time_t // 8) * 8 + 8
    else:
        time_total = time_t
    result = []
    for symbol in result_1:
        hours += 8
        if hours <= time_total:
            result.append(symbol)
    return result


def theory_day(result_2: list, time_pr: int) -> tuple:
    if time_pr % 8 != 0:
        count = time_pr // 8 + 1
    else:
        count = time_pr // 8
    result = result_2[0:count]
    date_end = result[len(result) - 1]
    return date_end, 8 - time_pr % 8


def practice_day(total: int, result_2, hour_exz, hour_consul, hour_day) -> str:
    if total % 8 != 0:
        count = total // 8 + 1
    else:
        count = total // 8
    return result_2[count - 1]


day_list = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18",
            "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"]
month_list = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]


def dates(start_date: str, time_t: int, time_pr: int, hour_consul: int, hour_exz: int) -> tuple:
    with open("cal.txt", 'r') as name:
        text = name.read()
    result = text.split(", ")
    result_1 = result_dates(start_date.split('.')[0], start_date.split('.')[1], result)
    result_2 = result_dates_out(time_t, result_1)
    date_start = result_2[0]
    consultation = result_2[len(result_2)-2]
    exam = result_2[len(result_2)-1]
    date_end_theory, hour_day = theory_day(result_2, time_pr)
    if time_pr % 8 != 0:
        date_start_practice = date_end_theory
    else:
        date_start_practice = result_2[result_2.index(date_end_theory) + 1]
    practice = time_t - time_pr - hour_exz - hour_consul
    date_end_practice = practice_day(practice, result_2[result_2.index(date_start_practice):], hour_exz, hour_consul, hour_day)
    return date_start, date_end_theory, date_start_practice, date_end_practice, consultation, exam, result_2, time_t, time_pr

