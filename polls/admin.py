# -*- coding: UTF-8 -*-
from django.contrib import admin

# Register your models here.
from .models import Question, Choice

class ChoiceInline(admin.TabularInline): # TabularInline 按行内表格展示
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently') # 增加展示选项
    list_filter = ['pub_date'] # 添加筛选控件
    search_fields = ['question_text'] # 添加搜索框

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
