from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('search/', views.search, name='search'),
    path('blog/page/<int:blog_pk>', views.infoBlog, name='blog_page_pk'),
    path('type/<str:type_name>', views.TypeBlog, name='blog_type_name'),
]
