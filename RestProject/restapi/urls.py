from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import OccurrenceList, OccurrenceDetail, UserList, UserDetail
from django.conf.urls import include

urlpatterns = [
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
    path('occurrence/', OccurrenceList.as_view()),
    path('occurrence/<int:pk>/', OccurrenceDetail.as_view()),
    path('api-auth/', include('rest_framework.urls'))
]

urlpatterns = format_suffix_patterns(urlpatterns)

