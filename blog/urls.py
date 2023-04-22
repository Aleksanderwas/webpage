from . import views
from django.urls import path

app_name = "blog"
urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
    path('opis_projektu/', views.UsedTech.as_view(), name='used_tech')
]