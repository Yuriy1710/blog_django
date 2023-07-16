from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('article/<int:pk>', views.ArticleDetailView.as_view(), name='article_detail'),
    path('add-post/', views.AddPostView.as_view(), name='add_post'),
    path('article/edit/<int:pk>', views.UpdatePostView.as_view(), name='update_post'),
    # path('article/delete/<int:pk>', views.DeletePostView.as_view(), name='delete_post'),
    path('article/delete/<int:pk>', views.delete_post, name='delete_post'),
]
