from netbox.api.routers import NetBoxRouter
from . import views


app_name = 'k8s'

router = NetBoxRouter()
router.register('k8s-teams', views.TeamViewSet)
router.register('k8s-namespaces', views.NamespaceViewSet)

urlpatterns = router.urls