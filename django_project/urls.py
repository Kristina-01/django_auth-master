# django_project/urls.py
from django import forms
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

from django.views.static import serve

from django.conf.urls import handler404

from django.conf import settings
from django.conf.urls.static import static

from . import views, settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),

    path('view/<str:name>/<int:id>/', views.add_task_to_list, name='add_task'),
    path('view/<int:idlesson>/<int:iduser>/<str:namep>/<int:isres>', views.next_lesson, name='new_lessons'),
    path('view/<int:idlesson>/<int:iduser>/<str:namep>', views.old_lessons, name='old_lessons'),
    path('view/', views.user_param, name="user_param"),

    path('media/', serve,{'document_root': settings.MEDIA_ROOT}),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = views.error_404
