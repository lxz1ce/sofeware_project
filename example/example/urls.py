"""example URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url
from demo1 import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('specific_info/', views.specific_info),
    path('admin/', admin.site.urls),
    path('', views.search_house),
    path('login/', views.login),
    path('register/', views.register),
    path('logout/', views.logout),
    path('show_info/', views.show_info),
    path('main/', views.main),
    path('add_house/', views.add_house),
    path('search_house/', views.search_house),
    path('add_technician/', views.add_technician),
    path('check_app/', views.check_app),
    path('my_app/', views.my_app),
    path('user_info/', views.user_info),
    path('repairing/', views.repairing),
    path('manage_repairing/', views.manage_repairing),
    path('cancel_repairing/', views.cancel_repairing),
    path('arrange_repairing/', views.arrange_repairing),
    path('pay/', views.pay),
    path('confirm_payment/', views.confirm_payment),
    path('cancel_apply/', views.cancel_apply),
    path('send_message/', views.send_message),
    path('my_message/', views.my_message),
    path('delete_house/', views.delete_house),
    path('create_apply/', views.create_apply),
    # path('export_app/', views.export_app),
    path('my_repairing/', views.my_repairing),
    path('comment/', views.comment),
    path('fix/', views.fix),
    path('check_user/', views.check_user),
    path('CS_change_info/', views.CS_change_info),
    path('remind/', views.remind),
    path('change_title/', views.change_title),
    path('reporting/', views.reporting),
    path('manage_reporting/', views.manage_reporting),
    path('handle_reporting/', views.handle_reporting),
    path('my_reporting/', views.my_reporting),
    url(r'^active/(?P<active_code>.*)/$', views.active, name="user_active"),
    url(r'^download_app/', views.download_app, name='crm_download'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)