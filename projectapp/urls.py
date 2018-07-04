from django.conf.urls import url
from projectapp import views
urlpatterns=[
url(r'^pullrequest/metadata',views.Pull_request_metadata.as_view(),name='Pull_request_metadata'),

]

