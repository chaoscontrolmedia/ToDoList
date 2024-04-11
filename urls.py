from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="list"),
    path('update_task/<str:pk>/', views.updateTask, name="update_task"),
    path('delete/<str:pk>/', views.deleteTask, name="delete"),
]


'''

#path('<slug:project_slug>', views.project_detail, name='detail'),
#path('add', views.BudgetCreateView.as_view(), name='add')
'''  