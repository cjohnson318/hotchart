from django.urls import path, include

from chart import views

urlpatterns = [
    path('', views.home, name='home'),
    path('line/', views.draw_line_chart, name='line-chart'),
    path('hist/', views.draw_histogram, name='histogram'),
    path('inline/line/', views.draw_inline_line_chart, name='inline-line-chart'),
]