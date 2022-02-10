from django.db import models

TRAININGPERIOD = (
    (1, '1개월 미만'),
    (2, '1개월~3개월 미만'),
    (3, '3개월~6개월 미만'),
    (4, '6개월 이상'),
)


ACCEPT = (
    (1, '모집중'),
    (2, '모집예정'),
    (3, '모집완료'),
)

ONOFFLINE = (
    (1, 'Online'),
    (2, 'Offline'),
    (3, 'Both'),
)

PLACE = (
    (1, '없음'),
    (2, '서울'),
    (3, '경기'),
    (4, '대구'),
    (5, '부산'),
    (6, '울산'),
    (7, '광주'),
    (8, '대전'),
    (9, '경북'),
    (10, '경남'),
    (11, '전북'),
    (12, '전남'),
    (13, '강원'),
    (14, '충남'),
)

APPLYCONDITION = (
    ('1', '졸업예정자'),
    ('2', '전공자'),
    ('3', '누구나'),
    ('4', '직장인'),
    ('5', '예비창업자'),
    ('6', '졸업자'),
)

APPLYCOURSE = (
    (1, '없음'),
    (2, '코테'),
    (3, '지원서'),
    (4, '인터뷰'),
    (5, '코테 + 지원서'),
    (6, '코테 + 인터뷰'),
    (7, '지원서 + 인터뷰'),
    (8, '코테 + 지원서 + 인터뷰'),
    (9, '적성검사'),
)

KDIGITAL = (
    (1, '국민내일배움카드 X'),
    (2, '국민내일배움카드 필수'),
    (3, '국민내일배움카드 선택사항'),
)

class BootCamp(models.Model):
    company_id = models.CharField(max_length=15, null=True, blank=True) # 사업자등록번호
    brand_name = models.CharField(max_length=100, null=True, blank=True) # 브랜드명
    program = models.CharField(max_length=500, null=True, blank=True) # 프로그램 종류
    bootcamp_name = models.CharField(max_length=100, null=True, blank=True) # 부트캠프 이름
    tech_stack = models.CharField(max_length=100, null=True, blank=True) # 기술 스택
    price = models.CharField(max_length=100, null=True, blank=True) # 수강료
    training_period = models.IntegerField(choices=TRAININGPERIOD, null=True, blank=True) # 교육 기간
    accept = models.IntegerField(choices=ACCEPT, null=True, blank=True) # 모집 현황
    apply_start = models.CharField(max_length=100, null=True, blank=True) # 모집 시작일
    apply_end = models.CharField(max_length=100, null=True, blank=True) # 모집 마감일
    on_offline = models.IntegerField(choices=ONOFFLINE, null=True, blank=True) # 온/오프라인
    place = models.IntegerField(choices=PLACE, null=True, blank=True) # 장소
    apply_condition = models.CharField(max_length=100, null=True, blank=True) # 지원자격
    apply_course = models.IntegerField(choices=APPLYCOURSE, null=True, blank=True) # 지원 과정
    k_digital = models.IntegerField(choices=KDIGITAL, null=True, blank=True) # 국민내일배움카드 여부
    link = models.CharField(max_length=1000, null=True, blank=True) # 링크
    note = models.CharField(max_length=1000, null=True, blank=True) # 비고
    count = models.IntegerField(default=0) # 조회수

    def __str__(self):
        return self.bootcamp_name