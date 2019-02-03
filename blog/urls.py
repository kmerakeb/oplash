from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns =[
    path('', views.post_list_view, name='post_list_view'),
    path('<int:year>)/<int:month>/<int:day>/<slug:post>/', views.post_detail_view, name='post_detail_view')

]