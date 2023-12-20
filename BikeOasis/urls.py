from django.urls import path
from . import views
# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login, name="login"),
    path('logout/', views.logout_view, name='logout'),
    path('register/',views.registration,name="register"), 
    path("edit/<int:id>/",views.EditDetails,name="edit"), 
    path('sports/', views.bike_list, name='bike_list'),
    path('bike/<int:pk>/', views.bike_detail, name='bike_detail'),
    path('bike/new/', views.bike_new, name='bike_new'),
    path('bike/<int:bike_id>/edit/', views.bike_edit, name='bike_edit'),
    path('bikes/delete/<int:bike_id>/', views.delete_bike, name='delete_bike'),
    path('message/', views.send_message, name='send_message'),
]

# for media uploading
# Your other URL patterns

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
