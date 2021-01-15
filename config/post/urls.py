from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
    path('', view=views.post_list, name='Ulist'),
    path('<int:pk>/', views.post_detail, name='Udetail'),
    path('create/', views.post_create, name='Ucreate'),
    path('<int:dpk>/delete/', views.post_delete, name='Udelete'),
    path('<int:pk>/create_comment/', views.comment_create, name='Ucocreate')
]