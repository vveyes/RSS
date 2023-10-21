from . import models, views, routers
from django.urls import path, include

urlpatterns = [
    path('api/v1/', include(routers.album_router.urls))
]
