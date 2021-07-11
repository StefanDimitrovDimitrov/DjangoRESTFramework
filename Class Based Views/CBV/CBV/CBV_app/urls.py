from django.urls import path

from CBV.CBV_app.views import CBVList, Details

urlpatterns = [
    path('', CBVList.as_view(), name='CBVList'),
    path('details/<int:pk>', Details.as_view(), name='details')
]