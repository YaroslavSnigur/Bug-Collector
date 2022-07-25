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
    path('bugs/<int:bug_id>/unassoc_agent/<int:agent_id>/', views.unassoc_agent, name='unassoc_agent'),
    path('agents/', views.AgentList.as_view(), name='agents_index'),
    path('agents/<int:pk>/', views.AgentDetail.as_view(), name='agents_detail'),
    path('agents/create/', views.AgentCreate.as_view(), name='agents_create'),
    path('agents/<int:pk>/update/', views.AgentUpdate.as_view(), name='agents_update'),
    path('agents/<int:pk>/delete/', views.AgentDelete.as_view(), name='agents_delete'),
    path('accounts/signup/', views.signup, name='signup'),
]