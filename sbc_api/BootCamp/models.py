from django.db import models

class BootCamp(models.Model):
    company_id = models.CharField(max_length=12, null=True, blank=True) # 사업자등록번호
    brand_name = models.CharField(max_length=100, null=True, blank=True) # 브랜드명
    program = models.CharField(max_length=100, null=True, blank=True) # 프로그램 종류
    bootcamp_name = models.CharField(max_length=100, null=True, blank=True) # 부트캠프 이름
    tech_stack = models.CharField(max_length=100, null=True, blank=True)# 기술 스택
    price = models.CharField(max_length=100, null=True, blank=True) # 수강료
    training_period = models.IntegerField(null=True, blank=True) # 교육 기간
    accept = models.IntegerField(null=True, blank=True) # 모집 현황
    apply_start = models.CharField(max_length=100, null=True, blank=True) # 모집 시작일
    apply_end = models.CharField(max_length=100, null=True, blank=True) # 모집 마감일
    on_offline = models.IntegerField(null=True, blank=True) # 온/오프라인
    place = models.IntegerField(null=True, blank=True) # 장소
    apply_condition = models.IntegerField(null=True, blank=True) # 지원자격
    apply_course = models.IntegerField(null=True, blank=True) # 지원 과정
    k_digital = models.IntegerField( null=True, blank=True) # 국민내일배움카드 여부
    link = models.CharField(max_length=1000, null=True, blank=True) # 링크
    note = models.CharField(max_length=100, null=True, blank=True) # 비고
    count = models.IntegerField(default=0) # 조회수

    def __str__(self):
        return self.bootcamp_name
