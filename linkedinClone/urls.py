"""linkedinClone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from linkedin_app import views
from django.conf import settings
from django.conf.urls.static import static

from django.views.static import serve

handler400 = 'linkedin_app.views.my_400'
handler404 = 'linkedin_app.views.my_404'
handler500 = 'linkedin_app.views.my_500'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('following/', views.follow_view),
    path('signup/', views.SignUpView.as_view()),
    path('login/', views.login_view),
    path('logout/', views.logout_view),
    path('create_post/', views.CreatePostView.as_view()),
    path('profile/<int:user_id>/', views.ProfilePageView.as_view()),
    path('follow/<int:user_id>/', views.handle_follow),
    path('like/<int:post_id>/', views.handle_like),
    path('messages/', views.direct_message_view),
    path('messagefeed/<int:author_id>/', views.message_feed_view),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += [
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
    re_path(r'^uploads/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), 
    ]
