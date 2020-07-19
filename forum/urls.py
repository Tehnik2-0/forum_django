from django.urls import path

from forum import views
 
urlpatterns = [
    path('', views.HomeListView.as_view(), name='home'),
    path('detail/<int:pk>', views.DetailPageListView.as_view(), name='detail_page')
]