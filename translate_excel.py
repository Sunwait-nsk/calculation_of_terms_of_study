from pandas import DataFrame
import openpyxl
from openpyxl.utils.cell import get_column_letter
from openpyxl.styles import (
                        PatternFill, Border, Side,
                        Alignment, Font, GradientFill
                        )

def translate_file(name_file: str, group_data: dict, months: list) -> None:
    wb = openpyxl.load_workbook(filename=name_file)
    sheet = wb["Sheet1"]
    font = Font(
        name='Times New Roman',
        size=12,
        bold=False,
        italic=False,
        vertAlign=None,
        underline='none',
        strike=False,
        color='FF000000'
    )
    alignment = Alignment(
        horizontal='general',
        vertical='bottom',
        text_rotation=0,
        wrap_text=False,
        shrink_to_fit=False,
        indent=0
    )
    border = Border(
        left=Side(border_style=None, color='FF000000'),
        right=Side(border_style=None, color='FF000000'),
        top=Side(border_style=None, color='FF000000'),
        bottom=Side(border_style=None, color='FF000000'),
        diagonal=Side(border_style=None, color='FF000000'),
        diagonal_direction=0,
        outline=Side(border_style=None, color='FF000000'),
        vertical=Side(border_style=None, color='FF000000'),
        horizontal=Side(border_style=None, color='FF000000')
    )

    for i in range(1, 32):
        letter = get_column_letter(i)
        sheet.column_dimensions[letter].width = 3
    letter1 = "{}1".format(get_column_letter(1))
    letter2 = "{}2".format(get_column_letter(1))
    letter3 = "{}3".format(get_column_letter(1))
    sheet[letter1].font = Font(bold=True)
    sheet[letter1].alignment = Alignment(horizontal='center')
    sheet[letter2].alignment = Alignment(horizontal='center')
    sheet[letter3].font = Font(bold=True)
    sheet[letter3].alignment = Alignment(horizontal='center')
    for i in range(1, 32):
        letter = "{}7".format(get_column_letter(i))
        sheet[letter].value = ""
    sheet.merge_cells('a7:ae7')
    thins = Side(border_style="thin", color="000000")
    for i in range(1, 32):
        letter = "{}7".format(get_column_letter(i))
        sheet[letter].border = Border(top=thins, bottom=thins, left=thins, right=thins)
    for j in range(len(months)):

        for i in range(1, 34):
            letter = "{}{}".format(get_column_letter(i), j * 4 + 1 + 7)
            sheet[letter].border = Border(top=thins, bottom=thins, left=thins, right=thins)

            letter = "{}{}".format(get_column_letter(i), j * 4 + 1 + 8)
            sheet[letter].border = Border(top=thins, bottom=thins, left=thins, right=thins)
            letter = "{}{}".format(get_column_letter(i), j * 4 + 1 + 9)
            sheet[letter].border = Border(top=thins, bottom=thins, left=thins, right=thins)
            letter = "{}{}".format(get_column_letter(i), j * 4 + 1 + 10)
            sheet[letter].border = Border(top=thins, bottom=thins, left=thins, right=thins)
        letter = "E{}".format(j * 4 + 1 + 7)
        month = sheet[letter].value
        letters = "A{}:AE{}".format((j * 4 + 1 + 7), (j * 4 + 1 + 7))
        sheet.merge_cells(letters)
        letter = "A{}".format(j * 4 + 1 + 7)
        sheet[letter].value = month
        sheet[letter].alignment = Alignment(horizontal='center')
        letter = "AG{}".format(j * 4 + 1 + 9)
        sheet[letter] = "=SUM(A{}:AE{})".format((j * 4 + 1 + 9), (j * 4 + 1 + 9))
        last_row = j * 4 + 1 + 10
    letter = "AF8:AF{}".format(last_row)
    sheet["AF{}".format(last_row + 1)] = "=SUM({})".format(letter)
    letter = "AG8:AG{}".format(last_row)
    sheet["AG{}".format(last_row + 1)] = "=SUM({})".format(letter)


    name_file_out = "{}-{}-{}.xlsx".format(group_data['profession'], group_data["date_start"], group_data["total_hour"])

    wb.save(name_file_out)
