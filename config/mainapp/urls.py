from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('contacts/', views.contacts, name='contacts'),
    path('courses/', views.courses, name='courses'),
    path('doc_site/', views.doc_site, name='doc_site'),
    path('login/', views.login, name='login'),
    path('news/', views.news, name='news'),
    path('news/<int:pk>/', views.news_with_pagiinator, name='news_paginator'),
]
