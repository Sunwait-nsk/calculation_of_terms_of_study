import openpyxl
import datetime
from openpyxl.utils.cell import get_column_letter


def in_date() -> tuple:
    wb = openpyxl.load_workbook(filename="сроки шаблон.xlsx")
    sheet = wb["данные"]
    date1 = sheet["B1"].value
    if date1.day < 10:
        day = "0{}".format(date1.day)
    else:
        day = "{}".format(date1.day)
    if date1.month < 10:
        month = "0{}".format(date1.month)
    else:
        month = "{}".format(date1.month)
    date1 = "{}.{}.{}".format(day, month, date1.year)
    total_t = sheet["B2"].value
    t_pr = sheet["B3"].value
    t_k = sheet["B4"].value
    t_e = sheet["B5"].value
    prof = sheet["B6"].value
    number = sheet["B7"].value
    preparat = sheet["B8"].value
    forma = sheet["B9"].value
    economy = sheet["B10"].value
    economy_teacher = sheet["B11"].value
    teacher = sheet["B12"].value
    people = sheet["B13"].value
    return date1, total_t, t_pr, t_k, t_e, prof, number, preparat, forma, economy, economy_teacher, teacher, people
