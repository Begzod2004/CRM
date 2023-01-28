from django.db import router
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.routers import SimpleRouter
from rest_framework_swagger.views import get_swagger_view
from django.conf import settings
from django.conf.urls.static import static
from .views import *
router = DefaultRouter()






router = SimpleRouter()
router.register('tranzaksiyaCategory', TranzaksiyaCategoryViewSet)
router.register('moliya_kirim', Moliya_kirimViewSet)
router.register('moliya_chiqim', Moliya_chiqimViewSet)
# router.register('import', ImportViewSet)
# router.register('export', ExportViewSet)
router.register('mijoz', MijozViewSet)
router.register('buyurtma', Buyurtma1ViewSet)
router.register('hodim', HodimViewSet)
router.register('mahsulotlar', MahsulotlarViewSet)
router.register('bonus', BonusViewSet)
router.register('mahsulot_olchov', Mahsulot_olchovViewSet)
router.register('ombor', OmborViewSet)




urlpatterns = [ 
    path("", include(router.urls)),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



