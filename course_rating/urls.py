from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('courses.urls', namespace='courses')),
    path('admin/', admin.site.urls),
]
