import openpyxl
from pandas import DataFrame


def pr_mon(mon: str) -> str:
    months = {'01': 'январь', '02': 'февраль', '03': 'март', '04': 'апрель', '05': 'май', '06': 'июнь', '07': 'июль',
              '08': 'август', '09': 'сентябрь', '10': 'октябрь', '11': 'ноябрь', '12': 'декабрь'}
    return months[mon]


def count_month(date_in: list) -> list:
    mon_lst = []
    for sym in date_in:
        if not (sym.split('.')[1]) in mon_lst:
            mon_lst.append((sym.split('.')[1]))
    return mon_lst


def date_under(day: int, x: str) -> str:
    month = {'01': 'январь', '02': 'февраль', '03': 'март', '04': 'апрель', '05': 'май', '06': 'июнь', '07': 'июль',
             '08': 'август', '09': 'сентябрь', '10': 'октябрь', '11': 'ноябрь', '12': 'декабрь'}
    for mon in month.keys():
        if mon == x:
            result_month = mon
    if day < 10:
        day_symbol = "0{}".format(day)
    else:
        day_symbol = str(day)
    return '2022.{}.{}'.format(result_month, day_symbol)


def pr_mon(mon: str) -> str:
    month = {'01': 'январь', '02': 'февраль', '03': 'март', '04': 'апрель', '05': 'май', '06': 'июнь', '07': 'июль',
             '08': 'август', '09': 'сентябрь', '10': 'октябрь', '11': 'ноябрь', '12': 'декабрь'}
    return month[mon]


##  Теория с 2022.03.30 по 2022.04.22
## Практика с 2022.04.25 по 2022.06.20
## Консультация 2022.06.21
## Экзамен 2022.06.22
## ('2022.03.30', '2022.04.22', '2022.04.25', '2022.06.20', '2022.06.21', '2022.06.22', ['2022.03.30', '2022.03.31', '2022.04.01', '2022.04.04', '2022.04.05', '2022.04.06', '2022.04.07', '2022.04.08', '2022.04.11', '2022.04.12', '2022.04.13', '2022.04.14', '2022.04.15', '2022.04.18', '2022.04.19', '2022.04.20', '2022.04.21', '2022.04.22', '2022.04.25', '2022.04.26', '2022.04.27', '2022.04.28', '2022.04.29', '2022.05.04', '2022.05.05', '2022.05.06', '2022.05.11', '2022.05.12', '2022.05.13', '2022.05.16', '2022.05.17', '2022.05.18', '2022.05.19', '2022.05.20', '2022.05.23', '2022.05.24', '2022.05.25', '2022.05.26', '2022.05.27', '2022.05.30', '2022.05.31', '2022.06.01', '2022.06.02', '2022.06.03', '2022.06.06', '2022.06.07', '2022.06.08', '2022.06.09', '2022.06.10', '2022.06.13', '2022.06.14', '2022.06.15', '2022.06.16', '2022.06.17', '2022.06.20', '2022.06.21', '2022.06.22'])

days = {'01': 31, '02': 29, '03': 31, '04': 30, '05': 31, '06': 30, '07': 31, '08': 31, '09': 30, '10': 31,
        '11': 30, '12': 31}


def table_xls(date_start: str, date_end_theory: str, date_start_practice: str, date_end_practice: str,
              consultation: int, exam: int, date_out: list, total: int, time_theory: int, group_data: dict,
              t_k: int, t_e: int, economy_teacher: str, economy: int) -> str:
    months = count_month(date_out)
    my_dict = {}
    last_day = date_out[-1]
    for d in range(1, 32):
        my_dict[str(d)] = []
        for y in range(1, len(months) + 1):
            if d == 5:
                my_dict[str(d)].append("Месяц {}".format(pr_mon(months[y - 1])))
            else:
                my_dict[str(d)].append('')
            my_dict[str(d)].append(d)
            if date_start <= date_under(d, months[y - 1]) <= last_day:
                my_dict[str(d)].append(1)
                my_dict[str(d)].append('В')

            else:
                my_dict[str(d)].append('')
                my_dict[str(d)].append("")
    my_dict['часов'] = ["" for _ in range(1, 17)]
    my_dict['дней'] = ["" for _ in range(1, 17)]
    # print(my_dict)
    for day in date_out:
        day_date = str(int(day.split('.')[2]))
        month_date = day.split('.')[1]
        my_dict[day_date][(months.index(month_date) * 4) + 3] = 8
    g = DataFrame(my_dict)
    m = {}
    for i, mon in enumerate(months):
        m[i] = g.loc[((i * 4) + 3)]
    sum_m = []
    for element in m:
        sum_d = sum(sym for sym in m[element] if sym == 8)
        sum_m.append(sum_d)
    for i, mon in enumerate(months):
        my_dict['часов'][(i * 4) + 3] = sum_m[i]
    g = DataFrame(my_dict)
    name = "temp.xlsx"
    g.to_excel(name)
    wb = openpyxl.load_workbook(filename=name)
    sheet = wb["Sheet1"]
    sheet.insert_rows(1, 6)
    sheet.delete_cols(1, 1)
    row = "СРОКИ ОБУЧЕНИЯ С " + date_start + " ПО " + exam
    sheet.merge_cells('A1:AE1')
    sheet.cell(row=1, column=1).value = row
    row = "Учебное заведение ИДПО ФГБОУ ВО Новосибирский ГАУ"
    sheet.merge_cells('A2:AE2')
    sheet.cell(row=2, column=1).value = row
    row = "ПРОФЕССИЯ {} ({}) {} ({})".format(group_data['profession'], group_data['type_preparation'],
                                             group_data['group'], group_data['forma'])
    sheet.merge_cells('A3:AE3')
    sheet.cell(row=3, column=1).value = row
    row = "ТЕОРИЯ = " + str(time_theory) + " час С " + date_start + " ПО " + date_end_theory
    sheet.cell(row=4, column=1).value = row
    sheet.merge_cells('A4:P4')
    row = "консультация = " + str(t_k) + " час " + str(consultation)
    sheet.cell(row=4, column=17).value = row
    sheet.merge_cells('Q4:AE4')
    row = "ПРАКТИКА = {} час С {} ПО {} ".format((total - time_theory - t_k - t_e), date_start_practice,
                                                 date_end_practice)
    sheet.cell(row=5, column=1).value = row
    sheet.merge_cells('A5:P5')
    row = "квалификационный экзамен = " + str(t_e) + " час " + exam
    sheet.cell(row=5, column=17).value = row
    sheet.merge_cells('Q5:AE5')
    row = "ОБЩЕЕ ЧИСЛО ЧАСОВ  = " + str(total) + " час"
    sheet.cell(row=6, column=1).value = row
    sheet.merge_cells('A6:P6')
    row = "экономика = {} час {}".format(economy, economy_teacher)
    sheet.cell(row=6, column=17).value = row
    sheet.merge_cells('q6:ae6')
    wb.save("temp.xlsx")
    return name, months
