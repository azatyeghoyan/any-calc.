from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('calculator/', views.calculator, name='calculator'),
    path('factorial/', views.factorial, name='factorial'),
    path('fibonacci/', views.fibonacci, name='fibonacci'),
    path('calculator/calc_res/', views.calc_res, name='res'),
    path('factorial/fact_res/', views.fact_res, name='res'),
    path('fibonacci/fib_res/', views.fib_res, name='res')
]
