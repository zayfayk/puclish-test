from django.urls import path
from .views import HomeView, PostDetalisView, AddPostView, Updatepost, DeletPost, UserPostsListView, AddCategoryView, CategoryView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('post/<int:pk>', PostDetalisView.as_view(), name='Post-Detalis'),
    path('Add_customer/', AddPostView.as_view(), name='Add_customer'),
    path('Update_customer/customer/<int:pk>', Updatepost.as_view(), name='updatepost'),
    path('delete_customer/<int:pk>/Remove', DeletPost.as_view(), name='DeletePost'),
    path('user_posts/', UserPostsListView.as_view(), name='user-posts'),
    path('category/<str:cats>/', CategoryView, name='Category'),
    path('Add_category/', AddCategoryView.as_view(), name='add_Category'),
]
