from django.contrib import admin
from django.urls import path, include
from student_app.student_api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.api_view, name='home'),
    path('student_api/', include('student_app.student_api.urls')),
]
