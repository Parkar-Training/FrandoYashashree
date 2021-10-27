from django.contrib import admin
from django.urls import path
from django.conf.urls import url

from user import views, viewsintegrationsignup
from user.views import UserD, User, emailOtp, OTP2, verifyOtp

from advanceProfile import views
from advanceProfile.views import Adv

from Posts.deletePost import dPost
from Posts.postPost import pPost
from Posts.putPost import putpost
from Posts.getPost import getpost
from frndlst.views import frnd







#from user.views import LogIn#User
#UserList, UserDetail, User
#from user.views import showData

urlpatterns = [
    path('admin/', admin.site.urls),
   # url(r'^api/show/(?P<userId>\d+)/$', UserDetail.as_view(),name='user_list'),


  #  path('view/', showData(),name='show data')


   # url(r'^api/show/$', UserList.as_view(), name='user_list'),

    url(r'^api/sign_up$',viewsintegrationsignup.users_new,name = "signup integration"), #Signup
    url(r'^api/put$',view=User), #forgetPassword

    url(r'^api/emailOtp2$',view=emailOtp), #OTP Email
    url(r'^api/otp/(?P<userId>\d+)/$',emailOtp.as_view(),name = 'otp store'),
   # url(r'^api/otp$',view=OTP2.as_view()),
    url(r'^api/emailOtp$',emailOtp.as_view()),

    url(r'^api/delete/(?P<userId>\d+)/$',UserD.as_view(),name='delete user'),

    url(r'^api/deletePost/(?P<id>\d+)/$',dPost.as_view(),name='delete Post'),
    url(r'^api/postPost$', pPost.as_view()),
    url(r'^api/getpost$', getpost.as_view()),
    url(r'^api/post/put/(?P<id>\d+)/$', putpost.as_view(),name='put POST'),




    url(r'^api/login$', UserD.as_view()),
    url(r'^api/verify$', verifyOtp.as_view()),

    url(r'^api/advprof$', Adv.as_view()),
    url(r'^api/advprof/put/(?P<id>\d+)/$', Adv.as_view()),
    url(r'^api/frndlst$', frnd.as_view()),
    url(r'^api/delete/frndlst/(?P<id>\d+)/$',frnd.as_view(),name='delete frndlst'),

    url(r'^api/frndlst/put/(?P<id>\d+)/$', frnd.as_view(),name='put frndlst')






]
