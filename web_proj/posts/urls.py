from django.urls import path
from .views import new, create, show, edit, update, delete, search, like, unlike, comment, comment_delete

app_name = "posts"
urlpatterns = [
    path('new/', new, name="new"),
    path('create/', create, name="create"),
    path('<int:post_id>/', show, name="show"),
    path('edit/<int:post_id>/', edit, name="edit"),
    path('update/<int:post_id>/', update, name="update"),
    path('delete/<int:post_id>/', delete, name="delete"),
    path('search/', search, name="search"),
    path('like/', like, name="like"),
    path('unlike/', unlike, name="unlike"),
    path('comment/<int:post_id>/', comment, name="comment"),
    path('comment_delete/<int:post_id>/<int:comment_id>/',
         comment_delete, name="comment_delete")
]
