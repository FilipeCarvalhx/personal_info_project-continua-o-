"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from info2_app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('welcome/', views.WelcomeView.as_view()),
    path('goodbye/', views.GoodbyeView.as_view()),
    path('about/', views.TemplateView.as_view()),
    path('people/', views.PeopleView.as_view(), name='people'),
    path('current-time/', views.current_time),
    path("greet_Name/", views.greet_Name),
    path('age-category/', views.age_category),
    path('sum/<num1>/<num2>', views.sum_numbers),
]