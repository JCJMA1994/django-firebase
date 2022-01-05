from login import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),

    # url
    path('', views.home, name='home'),
    path('signin/', views.signIn, name='signIn'),
    path('signup/', views.signUp, name='signUp'),
    path('postsign/', views.postSignIn, name='postSignIn'),
    path('logout/', views.logout, name="logout"),
    path('postsignup/', views.postSignUp, name="postSignUp"),

]
