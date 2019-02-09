from django.conf.urls import url
from . import views
from django.urls import path
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import PostSitemap

sitemaps = {
    'posts' : PostSitemap
}

urlpatterns =[
    path('', views.post_list_view, name='post_list_view'),
    path('<int:year>)/<int:month>/<int:day>/<slug:post>/', views.post_detail_view, name='post_detail_view'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap')

]