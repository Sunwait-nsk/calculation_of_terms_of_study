import raschet_pr
import transformations
import translate_excel
import in_date

if __name__ == "__main__":
    date1, tot_t, t_pr, t_k, t_e, prof, number, preparat, forma, economy, ec_teach, teacher, people = in_date.in_date()
    group = ' Группа № {}'.format(number)

    group_data = {
        "date_start": date1,
        "total_hour": tot_t,
        'profession': prof,
        'group': group,
        'type_preparation': preparat,
        'forma': forma,
        'economy': economy,
        'teacher': teacher,
        'economy_teacher': ec_teach,
        'people': people
    }
    date_start, date_end_theory, date_start_practice, date_end_practice, consultation, exam, date_out, total, time\
        = raschet_pr.dates(date1, tot_t, t_pr, t_k, t_e)
    print(raschet_pr.dates(date1, tot_t, t_pr, t_k, t_e))
    name_file, months = transformations.table_xls(date_start, date_end_theory, date_start_practice, date_end_practice,
                                                  consultation, exam, date_out, tot_t, t_pr, group_data, t_k, t_e,
                                                  ec_teach, economy)
    translate_excel.translate_file(name_file, group_data, months)
