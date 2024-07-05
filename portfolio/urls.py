
from django.urls import  path
from .views import index
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', index, name='home' ),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
