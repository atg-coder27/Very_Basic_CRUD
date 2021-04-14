from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home_view, name = 'home'),
    path('login/',views.login_view,name = 'login'),
    path('display/',views.display_view,name = 'display'),
    path('edit/<int:pk>/',views.edit_view, name = 'edit'),
    path('delete/<int:pk>/',views.delete_view,name = 'delete')
]
