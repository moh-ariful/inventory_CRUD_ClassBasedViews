from django.contrib import admin
from django.urls import path
from stock.views import *
from django.conf.urls.static import static
from django.conf import settings
from stock import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    # Registration
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # CRUD
    path('createstock/', views.CreateStock.as_view(), name='createstock'),
    path('detail/<int:pk>', views.DetailStock.as_view(), name='detailstock'),
    path('detail/<int:pk>/update', views.UpdateStock.as_view(), name='updatestock'),
    path('detail/<int:pk>/delete', views.DeleteStock.as_view(), name='deletestock'),

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
