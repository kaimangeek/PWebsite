from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('accounts/', include('django.contrib.auth.urls'))
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]

urlpatterns = format_suffix_patterns(urlpatterns)