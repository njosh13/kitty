from django.urls import path
from . import views

app_name = 'user'
urlpatterns =[

    path('', views.index, name='index'),

    path('register', views.register, name='register'),

    path('', views.users, name='users'), #c[R]ud
    path('create', views.users_create, name='users_create'), #[C]rUd
    path('update/<user_id>', views.users_update, name='users_update'), #Cr[U]d
    path('delete/<user_id>', views.users_delete, name='users_delete'), #cru[D]

    path('api/users',
        views.user_list,
        name='user-list'),
    path('api/users/<int:pk>',
        views.user_detail,
        name='user-detail'),
]


from rest_framework.urlpatterns import format_suffix_patterns
# from snippets import views

urlpatterns += [
    
    path('api/users',
        views.user_list,
        name='user-list'),
    path('api/users/<int:pk>',
        views.user_detail,
        name='user-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)

# https://www.django-rest-framework.org/api-guide/authentication/#generating-tokens
from rest_framework.authtoken import views
urlpatterns += [
    path('api-token-auth/', views.obtain_auth_token)
]