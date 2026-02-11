from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name = 'home'),
    path('addbook', views.add_Book, name = 'addbook'),
    path('addschool', views.add_school, name = 'addschool'),
    path('editbook/<int:id>/', views.edit_book, name = 'editbook'),
    path('editschool/<int:id>/', views.edit_school, name = 'editschool'),
    path('deletebook/<int:id>/', views.delete_book, name = 'deletebook'),
    path('deleteschool/<int:id>/', views.delete_school, name = 'deleteschool'),
    path('login', views.login_view, name = 'login'),
    path('logout', views.logout_view, name = 'logout'),
    path('register', views.register, name = 'register'),
    path('activate/<uidb64>/<token>/', views.activate_account, name='activate'),



]