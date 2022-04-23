# calculation_of_terms_of_study
Python libraries used: openpyxl, pandas, requests
Input data: training time, start date, profession, consultation and exam hours, full name of the teacher
Output data: a ready-made Excel file with the name of the profession.
Intermediate data: Temp preview file.xlxs
First, a list of the dates of the desired year is generated in the script calenda1r.py . The result in the file - cal.txt . It starts independently, if necessary
The main script is main.py
The template of the data array collected in the dictionary using Dataframe is transferred to an Excel file, then formatting and calculations are performed
