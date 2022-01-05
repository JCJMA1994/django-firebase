from login import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),

    # url
    path('', views.home, name='home'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signUp, name='signup'),
    path('postsign/', views.postsign),
    path('logout/', views.logout, name="logout"),
    path('postsignup/', views.postsignup, name="postsignup"),

]
