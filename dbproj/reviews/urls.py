from django.urls import path
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
urlpatterns = [
    
    path('movie_detail/<pk>',views.moviedetail,name='moviedet'),
    
    ]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)