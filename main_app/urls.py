from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('bugs/', views.bugs_index, name='index'),
    path('bugs/<int:bug_id>/', views.bugs_detail, name='detail'),
    path('bugs/create/', views.BugCreate.as_view(), name='bugs_create'),
    path('bugs/<int:pk>/update/', views.BugUpdate.as_view(), name='bugs_update'),
    path('bugs/<int:pk>/delete/', views.BugDelete.as_view(), name='bugs_delete'),
]