from django.urls import path
from . import views

app_name = 'certificates'

urlpatterns = [
    path('', views.all_certificates, name='all_certificates'),
    path('<int:certificate_id>/', views.detail, name='detail')
]