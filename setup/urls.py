from django.contrib import admin
from django.urls import path, include
from main.views import HomeView
from tasks.views import TaskListView, TaskUpdateView, TaskDeleteView, TaskCreateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='main-home'),
    path('Tasks/', include('tasks.urls')),
    path('account/', include('account.urls')),
    path('upload/', include('filemanager.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
