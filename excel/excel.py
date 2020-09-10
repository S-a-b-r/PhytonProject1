import xlsxwriter
import sys
sys.path[0] = 'd:\\Univer\\Alg\\PythonProject1'
from db.DB import DB

#Создать экземпляр БД
db = DB()
tests = db.getTestResults() #Получили данные тестов

#Создаем документ
workbook = xlsxwriter.Workbook('example.xlsx')#Создаем документ
worksheet = workbook.add_worksheet() #Создаем вкладку внутри документа

#Настроим форматирование
cellPass = workbook.add_format({'font_color': 'green'})
cellFail = workbook.add_format({'bold': True, 'font_color': 'red'})

#Пишем данные
worksheet.write('A1', ' № ' )
worksheet.write('B1', ' Название теста')
worksheet.write('C1', ' Успех')
worksheet.write('D1', 'Фиаско')
worksheet.write('E1', 'Дата проведения')

for i, test in enumerate(tests):
    worksheet.write('A' + str(i+2), i + 1)
    worksheet.write('B' + str(i+2), test['name'])
    if test['result']:
        worksheet.write('C' + str(i+2), 1 , cellPass)
    else:
        worksheet.write('D' + str(i+2), 1 , cellFail)
    worksheet.write('E' + str(i+2), test['date_time'])

#Считаем кол-во успешных и проваленных тестов
worksheet.write('F1', 'Успешные тесты')
worksheet.write('G1', 'Проваленные тесты тесты')
worksheet.write('F2', '=SUM(C:C)')
worksheet.write('G2', '=SUM(D:D)')

#Создаем график
chart = workbook.add_chart({'type': 'column'})
chart.add_series({'values': '=Sheet1!$F2'})
chart.add_series({'values': '=Sheet1!$G2'})
worksheet.insert_chart('H7', chart)

#Закрыть документ, записать данные
workbook.close()