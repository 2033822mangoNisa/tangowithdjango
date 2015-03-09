from django.conf.urls import patterns, url
from rango import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^about/$', views.about, name='about'),
        url(r'^add_category/$', views.add_category, name='add_category'),
        url(r'^category/(?P<category_name_slug>[\w\-]+)/add_page/$', views.add_page, name='add_page'),
        url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.category, name='category'),
        #url(r'^register/$', views.register, name='register'),
        #url(r'^login/$', views.user_login, name='login'),
        url(r'^add_profile/$', views.register_profile, name='add_profile'),
        url(r'^edit_profile/$', views.edit_profile, name='edit_profile'),
        url(r'^profile/(?P<username>[\w\-]+)/$', views.profile, name='profile'),
        url(r'^restrict/ed/', views.restricted, name='restricted'),
        url(r'^users_page/$', views.users_page, name='users_page'),
        #url(r'^search/$', views.search, name='search'),
        url(r'^goto/$', views.track_url, name='goto'),
        

)
