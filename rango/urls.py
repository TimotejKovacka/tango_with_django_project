from django.urls import path
from rango import views

app_name = 'rango'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('about/', views.about, name = 'about'),
    path('darth_vader/', views.vader, name='vader'),
    path('category/<slug:category_name_slug>/', views.show_category, name='show_category' ),
    path('add_category/', views.add_category, name='add_category'),
    path('category/<slug:category_name_slug>/add_page/',
         views.add_page, name='add_page'),
]