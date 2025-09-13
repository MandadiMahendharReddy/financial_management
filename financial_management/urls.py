"""
URL configuration for financial_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('debug/template-paths/', views.debug_template_settings, name='debug_template_settings'),
    path('report/excel/', views.export_report_excel, name='export_report_excel'),
    path('report/pdf/', views.export_report_pdf, name='export_report_pdf'),
    path('report/word/', views.export_report_word, name='export_report_word'),
    path('admin/', admin.site.urls),
    path('income/', include('income.urls')),
    path('expenditure/', include('expenditure.urls')),
    path('savings/', include('savings.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', views.register, name='register'),
]
