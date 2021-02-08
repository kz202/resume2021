from django.urls import path
from . import views

app_name = 'resume'

urlpatterns = [
    path('cv/', views.home, name='home'),
    path('', views.home, name='home'),
    path('cv/about_me/', views.about_me, name='about_me'),
    path('cv/website/', views.website, name='website'),
    path('cv/contact/', views.mail, name='contact'),
    path('cv/skills/', views.skills, name = 'skills'),
    path('cv/back-end/', views.back, name = 'back'),
    path('cv/skills/<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name = 'blog_detail'),
    path('cv/skills/tag/<slug:tag_slug>/', views.skills, name='post_list_by_tag'),

            ]
