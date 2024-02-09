from django.urls import include, path
from rest_framework import routers
from django.contrib import admin
from views import MyModelViewSet, MyModelCreateAPIView

router = routers.DefaultRouter()
router.register(r'mymodels', MyModelViewSet)

urlpatterns = {
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api/', include('audify_backend.urls')),
    path('mymodels/create/', MyModelCreateAPIView.as_view(), name='mymodel_create'),
}
