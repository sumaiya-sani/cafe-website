from django.urls import path
from store import views 
from.views import *
from django.contrib.auth import views as auth_views


app_name="cafe"
urlpatterns=[
    path('index/',views.index,name='index'),
    path('cafe_list/',views.CafeList,name='cafe_list'),
    path('cafe/<str:slug>',views.CafeDetail,name='cafe_detail'),
    path('search/',views.search_page,name='search_page'),
    path('addcafe/',views.add_cafe,name="add_cafe", ),
    #user
    path("register", register.as_view(), name="register"),
    path('edit_profile/',UserEditView.as_view(),name="edit_profile"),
    path('password/',auth_views.PasswordChangeView.as_view(template_name='change_password.html')),
    path('login/',views.login_page,name='login'),
    
]