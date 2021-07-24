from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('dashboard/', views.dashboard, name='dashboard'), 
    path('logout/', views.ulogout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.ulogin, name='login'),
    path('addp/', views.addp, name='addp'),
    path('searchpost/', views.searchpost, name='searchpost'),
    path('likepost/<int:pk>', views.like , name='likepost'),
    path('editp/<int:id>/', views.editp, name='editp'),
    path('delete/<int:id>/', views.deletep, name='deletep'),  
] 
