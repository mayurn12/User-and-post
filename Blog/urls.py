from django.urls import path
# from .import views
from. views import PostView,PostUpdate, PostCreate, PostDelete
urlpatterns = [
    path('',PostView.as_view()),
    path('post_update/<pk>',PostUpdate.as_view()),
    path('post_create/',PostCreate.as_view()),
    path('/<pk>/post_delete',PostDelete.as_view())
]