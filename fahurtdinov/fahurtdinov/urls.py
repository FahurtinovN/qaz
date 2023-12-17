from django.contrib import admin
from django.urls import path, re_path
from fahurtdinov import views

urlpatterns = [
    re_path(r'full_name/about/contact/', views.contact,kwargs={'github': '213', 'number': 89127018780, 'telegram': 'xvdf'}),
    re_path(r'full_name/about/', views.about, kwargs={'city': 'Kirov', 'up': 3.80, 'love': 'Люблю учиться новому'}),
    path(r'full_name/', views.full_name, kwargs={'name': 'Nurislam', 'age': 16, 'interests': 'Python'}),
    path(r'about/', views.about, kwargs={'city': 'Kirov', 'up': 3.80, 'love': 'Люблю учиться новому'}),
    path(r'contact/', views.contact, kwargs={'github': 'на moodle', 'number': 484665654, 'telegram': '@Nurislam_2007'})
]