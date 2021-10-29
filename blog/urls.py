from django.conf.urls import url 

from .views import index, add_blog, delete_blog, update_blog, view_blog
urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'add_blog$', add_blog, name='add-blog'), 
    url(r'^delete_blog/(?P<blog_id>\d+)$', delete_blog, name='delete-blog'),
    url(r'^update_blog/(?P<blog_id>\d+)$', update_blog, name='update-blog'),
    url(r'^view_blog/(?P<blog_id>\d+)$', view_blog, name='view-blog'),
]