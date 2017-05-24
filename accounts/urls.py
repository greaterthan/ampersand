from django.conf.urls import include, url
from accounts.views import *

from accounts.views import *

urlpatterns = [
    url(r'^(?P<account_id>\d+)/$', AccountDetail.as_view(), name='account_detail'),
    url(r'^list/$', AccountList.as_view(), name='account_list'),
]



