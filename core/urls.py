from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name= 'login'),
    path('signup/', views.signup, name= 'signup'),
    path('logout/', views.logout_view, name = 'logout'),
    path('dashboard/', views.dashboard, name= 'dashboard'),
    path('contacts/', views.contact_list, name= 'contact_list'),
    path('contacts/view/<int:pk>/', views.view_contact, name='view_contact'),  
    path('contacts/edit/<int:pk>/', views.edit_contact, name='edit_contact'),  
    path('contacts/delete/<int:pk>/', views.delete_contact, name='delete_contact'),  



]