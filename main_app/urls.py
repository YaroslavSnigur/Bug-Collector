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
    path('bugs/<int:bug_id>/add_treatment/', views.add_treatment, name='add_treatment'),
    path('bugs/<int:bug_id>/add_photo/', views.add_photo, name='add_photo'),
    path('bugs/<int:bug_id>/assoc_agent/<int:agent_id>/', views.assoc_agent, name='assoc_agent'),
]