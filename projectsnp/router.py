from snpapp.api.viewsets import userviewsets
from rest_framework import routers

router = routers.DefaultRouter()
router.register('snpapp', userviewsets, base_name='snpapp_api')
