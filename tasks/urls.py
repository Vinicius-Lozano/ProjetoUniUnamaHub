from django.urls import path, include
from .views import TaskDetailView, TaskListView, TaskUpdateView, TaskDeleteView, TaskCreateView

urlpatterns = [
    path('', TaskListView.as_view(), name = 'task-list'),
    path('<int:pk>/edit/', TaskUpdateView.as_view(), name= 'task-edit'),
    path('<int:pk>/delete/', TaskDeleteView.as_view(), name= 'task-delete'),
    path('create/', TaskCreateView.as_view(), name='task-create'),
    path('<int:pk>/Detail/', TaskDetailView.as_view(), name='task-detail'),
    path('Tasks/', include('filemanager.urls'))  
]
