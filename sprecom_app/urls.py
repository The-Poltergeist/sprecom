from django.urls import path
from . import views

urlpatterns = [
    # path('',views.index,name='index'),
    # path('form/',views.form,name='form'),
    path('form', views.UserViewSet.as_view()),
]

# path('', views.UserViewSet.as_view()),