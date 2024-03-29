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
    temp = bootcamp_sheet.cell(idx, 6).value
    if temp == 1:
        training_period = '1개월 미만'
    elif temp == 2:
        training_period = '1개월~3개월 미만'
    elif temp == 3:
        training_period = '3개월~6개월 미만'
    elif temp == 4:
        training_period = '6개월 이상'
    else:
        training_period = None

    temp = bootcamp_sheet.cell(idx, 7).value
    if temp == 1:
        accept = '모집중'
    elif temp == 2:
        accept = '모집예정'
    elif temp == 3:
        accept = '모집완료'
    else:
        accept = None

    apply_start = bootcamp_sheet.cell(idx, 8).value if bootcamp_sheet.cell(idx, 8).value else None
    apply_end = bootcamp_sheet.cell(idx, 8).value if bootcamp_sheet.cell(idx, 8).value else None

    temp = bootcamp_sheet.cell(idx, 10).value
    if temp == 1:
        on_offline = '온라인'
    elif temp == 2:
        on_offline = '오프라인'
    elif temp == 3:
        on_offline = '온/오프라인 병행'
    else:
        on_offline = None

    temp = bootcamp_sheet.cell(idx, 11).value
    if temp == 1:
        place = '없음'
    elif temp == 2:
        place = '서울'
    elif temp == 3:
        place = '경기'
    elif temp == 4:
        place = '대구'
    elif temp == 5:
        place = '부산'
    elif temp == 6:
        place = '울산'
    elif temp == 7:
        place = '광주'
    elif temp == 8:
        place = '대전'
    elif temp == 9:
        place = '경북'
    elif temp == 10:
        place = '경남'
    elif temp == 11:
        place = '전북'
    elif temp == 12:
        place = '전남'
    elif temp == 13:
        place = '강원'
    elif temp == 14:
        place = '충남'
    else:
        place = None

    apply_condition = list(map(int, map(float, str(bootcamp_sheet.cell(idx, 12).value).split(","))))
    apply_conditions = []
    for x in apply_condition:
        apply_conditions += APPLYCONDITION[x - 1][1] + ","
    apply_condition = "".join(apply_conditions)[:-1]

    temp = bootcamp_sheet.cell(idx, 13).value
    if temp == 1:
        apply_course = '없음'
    elif temp == 2:
        apply_course = '코테'
    elif temp == 3:
        apply_course = '지원서'
    elif temp == 4:
        apply_course = '인터뷰'
    elif temp == 5:
        apply_course = '코테 + 지원서'
    elif temp == 6:
        apply_course = '코테 + 인터뷰'
    elif temp == 7:
        apply_course = '지원서 + 인터뷰'
    elif temp == 8:
        apply_course = '코테 + 지원서 + 인터뷰'
    elif temp == 9:
        apply_course = '적성검사'
    else:
        apply_course = None

    temp = bootcamp_sheet.cell(idx, 14).value
    if temp == 1:
        k_digital = '국민내일배움카드 X'
    elif temp == 2:
        k_digital = '국민내일배움카드 필수'
    elif temp == 3:
        k_digital = '국민내일배움카드 선택사항'
    else:
        apply_course = None

    link = bootcamp_sheet.cell(idx, 15).value if bootcamp_sheet.cell(idx, 15).value else None
    note = bootcamp_sheet.cell(idx, 16).value if bootcamp_sheet.cell(idx, 16).value else None
    image_id = bootcamp_sheet.cell(idx, 17).value if bootcamp_sheet.cell(idx, 17).value else None
    values = (id, company_id, brand_name, program, bootcamp_name, tech_stack, price, training_period, accept,
              apply_start, apply_end, on_offline, place, apply_condition, apply_course, k_digital, link, note, image_id)
    curs.execute(bootcamp_insert, values)
conn.commit()
print("BootCamp 정보가 DB에 등록되었습니다!")
