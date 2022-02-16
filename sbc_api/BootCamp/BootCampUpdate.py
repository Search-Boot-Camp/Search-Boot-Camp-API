#-*- coding: utf-8 -*-

import pandas as pd
import pymysql
import xlrd
import datetime

PROGRAMS = (
    ('1', 'Back-end(백엔드)'),
    ('2', 'Bootcamp Prep(부트캠프 프랩)'),
    ('3', 'Data analysis(데이터 분석, 빅데이터)'),
    ('4', 'Software Development(소프트웨어 개발)'),
    ('5', 'Algorithm(알고리즘)'),
    ('6', 'Cloud(클라우드)'),
    ('7', 'Portfolio(포트폴리오)'),
    ('8', 'Full Stack(풀스택)'),
    ('9', 'Front-end(프론트엔드)'),
    ('10', 'AI(인공지능)'),
    ('11', 'Android'),
    ('12', 'iOS'),
    ('13', 'Web'),
    ('14', '3D Graphics'),
    ('15', '이론'),
    ('16', 'Intelligent Robots(지능로봇)'),
    ('17', 'IOT(사물인터넷)'),
    ('18', 'Block Chain(블록체인)'),
    ('19', 'Virtual Reality(가상현실)'),
    ('20', 'DevOps'),
    ('21', 'Embedded(임베디드)'),
    ('22', 'Security(보안)'),
    ('23', '3D printing'),
    ('24', 'PM(프로덕트매니지먼트)'),
    ('25', '기타'),
)

APPLYCONDITION = (
    ('1', '졸업예정자'),
    ('2', '전공자'),
    ('3', '누구나'),
    ('4', '직장인'),
    ('5', '예비창업자'),
    ('6', '졸업자'),
)

conn = pymysql.connect(host='127.0.0.1', user='root', db='sbc')
curs = conn.cursor(pymysql.cursors.DictCursor)

bootcamp_book = xlrd.open_workbook('Search Boot Camp.xls')
bootcamp_sheet = bootcamp_book.sheet_by_name('취합본')

bootcamp_truncate = 'truncate table BootCamp_bootcamp'

curs.execute(bootcamp_truncate)
conn.commit()

bootcamp_insert = 'insert into BootCamp_bootcamp values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'

for idx in range(1, bootcamp_sheet.nrows):
    id = idx;
    company_id = bootcamp_sheet.cell(idx, 0).value if bootcamp_sheet.cell(idx, 0).value else None
    brand_name = bootcamp_sheet.cell(idx, 1).value

    program = list(map(int, map(float, str(bootcamp_sheet.cell(idx, 2).value).split(","))))
    programs = []
    for x in program:
        programs += PROGRAMS[x-1][1] + ","
    program = "".join(programs)[:-1]

    bootcamp_name = bootcamp_sheet.cell(idx, 3).value
    tech_stack = bootcamp_sheet.cell(idx, 4).value if bootcamp_sheet.cell(idx, 4).value else None
    price = bootcamp_sheet.cell(idx, 5).value if bootcamp_sheet.cell(idx, 5).value else None
    training_period = bootcamp_sheet.cell(idx, 6).value
    accept = bootcamp_sheet.cell(idx, 7).value
    apply_start = datetime.datetime(
        *xlrd.xldate_as_tuple(bootcamp_sheet.cell(idx, 9).value, bootcamp_book.datemode)).strftime(
        "%x") if bootcamp_sheet.cell(idx, 8).value else None
    apply_end = datetime.datetime(
        *xlrd.xldate_as_tuple(bootcamp_sheet.cell(idx, 9).value, bootcamp_book.datemode)).strftime(
        "%x") if bootcamp_sheet.cell(idx, 9).value else None
    on_offline = bootcamp_sheet.cell(idx, 10).value
    place = bootcamp_sheet.cell(idx, 11).value

    apply_condition = list(map(int, map(float, str(bootcamp_sheet.cell(idx, 12).value).split(","))))
    apply_conditions = []
    for x in apply_condition:
        apply_conditions += APPLYCONDITION[x-1][1] + ","
    apply_condition = "".join(apply_conditions)[:-1]

    apply_course = bootcamp_sheet.cell(idx, 13).value
    k_digital = bootcamp_sheet.cell(idx, 14).value
    link = bootcamp_sheet.cell(idx, 15).value if bootcamp_sheet.cell(idx, 15).value else None
    note = bootcamp_sheet.cell(idx, 16).value if bootcamp_sheet.cell(idx, 16).value else None
    image_id = bootcamp_sheet.cell(idx, 17).value if bootcamp_sheet.cell(idx, 17).value else None
    values = (id, company_id, brand_name, program, bootcamp_name, tech_stack, price, training_period, accept,
              apply_start, apply_end, on_offline, place, apply_condition, apply_course, k_digital, link, note, image_id)
    curs.execute(bootcamp_insert, values)
conn.commit()
print("BootCamp 정보가 DB에 등록되었습니다!")
