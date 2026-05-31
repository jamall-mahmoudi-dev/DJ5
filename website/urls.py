from django.urls import path
from .views import nginx, test, test_do, about, index, contact

app_name = 'website'

urlpatterns = [
    
    path('test/', test, name='test'),
    path('test_do/', test_do, name='test_do'),
    path('nginx/', nginx, name='nginx'),
    path('about/', about , name='about'),
    path('index/', index , name='index'),
    path('contact/', contact , name='contact')
]