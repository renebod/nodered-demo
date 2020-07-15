from django.conf.urls import url
from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from rest_framework_swagger.views import get_swagger_view

app_name = 'validate_vlan'
schema_view = get_swagger_view(title='Example VLAN Inventory API')


urlpatterns = [
    url(r'^api/token/$', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    url(r'^api/token/refresh/$', TokenRefreshView.as_view(), name='token_refresh'),
    url(r'^api/token/verify/$', TokenVerifyView.as_view(), name='token_verify'),
    url('swagger', schema_view, name='docs'),
    path('vlans', views.VLANList.as_view()),
    path('vlans/<int:pk>/', views.VLANDetail.as_view()),
    path('check_vlan', views.CheckVLAN.as_view(), name='CheckVLAN'),
]
