import pandas as pd
import pymysql
import xlrd
import datetime

conn = pymysql.connect(host='127.0.0.1', user='root', password='qwer1234', db='sbc')
curs = conn.cursor(pymysql.cursors.DictCursor)

bootcamp_book = xlrd.open_workbook('Search Boot Camp.xls')
bootcamp_sheet = bootcamp_book.sheet_by_name('김현빈')

bootcamp_truncate = 'truncate table BootCamp_bootcamp'

curs.execute(bootcamp_truncate)
conn.commit()

bootcamp_insert = 'insert into BootCamp_bootcamp values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'

for idx in range(1, bootcamp_sheet.nrows):
    id = idx;
    company_id = bootcamp_sheet.cell(idx, 0).value if bootcamp_sheet.cell(idx, 0).value else None
    brand_name = bootcamp_sheet.cell(idx, 1).value
    program = bootcamp_sheet.cell(idx, 2).value
    bootcamp_name = bootcamp_sheet.cell(idx, 3).value
    tech_stack = bootcamp_sheet.cell(idx, 4).value if bootcamp_sheet.cell(idx, 4).value else None
    price = bootcamp_sheet.cell(idx, 5).value if bootcamp_sheet.cell(idx, 5).value else None
    training_period = bootcamp_sheet.cell(idx, 6).value
    accept = bootcamp_sheet.cell(idx, 7).value
    apply_start = datetime.datetime(*xlrd.xldate_as_tuple(bootcamp_sheet.cell(idx, 9).value, bootcamp_book.datemode)).strftime("%x") if bootcamp_sheet.cell(idx, 8).value else None
    apply_end = datetime.datetime(*xlrd.xldate_as_tuple(bootcamp_sheet.cell(idx, 9).value, bootcamp_book.datemode)).strftime("%x") if bootcamp_sheet.cell(idx, 9).value else None
    on_offline = bootcamp_sheet.cell(idx, 10).value
    place = bootcamp_sheet.cell(idx, 11).value
    apply_condition = bootcamp_sheet.cell(idx, 12).value
    apply_course = bootcamp_sheet.cell(idx, 13).value
    k_digital = bootcamp_sheet.cell(idx, 14).value
    link = bootcamp_sheet.cell(idx, 15).value if bootcamp_sheet.cell(idx, 15).value else None
    note = bootcamp_sheet.cell(idx, 16).value if bootcamp_sheet.cell(idx, 16).value else None
    count = 0
    values = (id, company_id, brand_name, program, bootcamp_name, tech_stack, price, training_period, accept,
              apply_start, apply_end, on_offline, place, apply_condition, apply_course, k_digital, link, note, count)
    curs.execute(bootcamp_insert, values)
conn.commit()
print("BootCamp 정보가 DB에 등록되었습니다!")


