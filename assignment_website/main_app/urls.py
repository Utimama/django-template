from django.urls import path
from .views import home_page_view, single_blog_post, about_page_view, contact_page_view

urlpatterns=[
    path('', home_page_view, name="Home"),
    path('', about_page_view, name="About"),
    path('', contact_page_view, name="Contact"),
    path('blog-post/<int:blog_id>/', single_blog_post, name="post")
]


