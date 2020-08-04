from django.urls import path

from forum import views
 
urlpatterns = [
    path('', views.HomeListView.as_view(), name='home'),
    path('detail/<int:pk>', views.DetailPageListView.as_view(), name='detail_page'),
    path('edit-page', views.ArticleCreateView.as_view(), name='edit_page'),
    path('update-page/<int:pk>', views.ArticleUpdateView.as_view(), name='update_page'),
    path('delete-page/<int:pk>', views.ArticleDeleteView.as_view(), name='delete_page'),
    path('login', views.ForumLoginView.as_view(), name='login_page'),
    path('register', views.RegisterUserView.as_view(), name='register_page'),
    path('logout', views.ForumLogoutView.as_view(), name='logout_page'),
    
    #ajax
    path('update_comment_status/<int:pk>/<slug:type>', views.update_comment_status, name='update_comment_status'),
]