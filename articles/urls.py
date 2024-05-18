from django.urls import path, re_path
from . import views

app_name = 'articles'

# no need to write '/article', already included in path('articles/', include('articles.urls')),
urlpatterns = [
    path('', views.article_list, name='list'),
    path('create/', views.article_create, name='create'),
    re_path(r'^(?P<slug>[\w-]+)/$', views.article_details, name = 'detail'),
    # path('<slug:slug>/', views.article_details),
]