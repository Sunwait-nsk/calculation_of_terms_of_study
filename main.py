import raschet_pr
import transformations
import translate_excel


if __name__ == "__main__":
    date1 = '30.03.2022'  # input("дата начала!!! в виде: 04.04.2022: ")
    total_t = 449  # int(input("Общее количество часов: "))
    t_pr = 144  # int(input("Теория в часах: "))
    t_k = 8
    t_e = 8
    profession = "Тракторист"
    number_group = 22
    group = ' Группа № {}'.format(number_group)
    type_preparation = "подготовка"
    forma = "очная"
    economy = 2
    economy_teacher = "Корнилова"
    teacher = "Барейко В. К."
    people = 10
    group_data = {
        "date_start": date1,
        "total_hour": total_t,
        'profession': profession,
        'group': group,
        'type_preparation': type_preparation,
        'forma': forma,
        'economy': economy,
        'teacher': teacher,
        'economy_teacher': economy_teacher,
        'people': people
    }
    date_start, date_end_theory, date_start_practice, date_end_practice, consultation, exam, date_out, total, time\
        = raschet_pr.dates(date1, total_t, t_pr, t_k, t_e)
    name_file, months = transformations.table_xls(date_start, date_end_theory, date_start_practice, date_end_practice,
                                                  consultation, exam, date_out, total_t, t_pr, group_data, t_k, t_e,
                                                  economy_teacher, economy)
    translate_excel.translate_file(name_file, group_data, months)
