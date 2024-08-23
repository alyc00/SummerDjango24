from django.urls import path, include
from . import views


app_name = 'store'

urlpatterns = [
    path('', views.home_page, name="home/"),
    path('show/<int:id>/', views.shows_detail, name="shows_detail/"),
    path('search.html', views.search_page, name="search/"),
    path('about.html', views.search_page, name="about/"),
]
