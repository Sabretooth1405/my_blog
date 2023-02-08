from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path, include
from users import views as users_views
from django.conf import settings
from django.conf.urls.static import static
from api import views as api_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("blog/", include("blog.urls")),
    path("register/", users_views.register, name="register"),
    path("login/", users_views.login, name="login"),
    path("logout/", users_views.logout, name="logout"),
    path("profile/", users_views.profile, name="profile"),
    path("user/update/<int:pk>",
         users_views.UpdateUserProfile.as_view(), name="update-user"),
    path("user/update-image/<int:pk>",
         users_views.UpdateProfileImg.as_view(), name="update-user-image"),
    path('users/delete/<int:pk>', users_views.UserDeleteView.as_view(), name='user-delete'),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='users/password_reset.html'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='users/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='users/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='users/password_reset_complete.html'
         ),
         name='password_reset_complete'),
    path('', include('blog.urls')),
    path('api/views/<int:pk>',api_views.view_counterDetail,name='api-views'),
   

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
