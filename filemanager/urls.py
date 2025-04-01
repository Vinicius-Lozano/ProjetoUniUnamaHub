from django.urls import path
from .views import FileUploadView, FileListView, FileDeleteView

urlpatterns = [
    path('files/', FileListView.as_view(), name='file-list'),
    path('<int:pk>/upload/', FileUploadView.as_view(), name='file-upload'),
    path('delete/<int:pk>/', FileDeleteView.as_view(), name='file-delete'),
]
