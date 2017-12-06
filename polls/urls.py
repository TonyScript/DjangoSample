# -*- coding: UTF-8 -*-
'''
There’s no need to add URL cruft such as .html – unless you want to, in which case you can do something like this:

	path('polls/latest.html', views.index),

But, don’t do that. It’s silly.
'''
from django.urls import path

from . import views

# Namespacing 用来区分不同的 app
# 因为当前工程中只有 polls 一个 app， 如果以后多了区分 url 等便会产生麻烦
# 加了命名空间之后，在 html 中的 url 前面加上相应的 app_name 即可
app_name = 'polls'

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
