from django.conf.urls import url
from django.urls import path
from Buy import views

app_name = 'Buy'

urlpatterns = [
	path(r'',views.index,name='index'),
	path(r'match/',views.match,name='match'),
	path(r'signup/',views.SignupFormView, name='signup'),
	path(r'login/',views.LoginFormView, name='login'),
	path(r'final/',views.finalPage, name='final_page')
]
