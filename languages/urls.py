from django.conf.urls import url, include

# spd : import modules that we need
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register( 'bahasa', views.LanguageViewSet, base_name='bahasaku')
router.register( 'paradigma', views.ParadigmViewSet)
router.register( 'pemrogram', views.ProgrammerViewSet)

app_name = 'languages_app'

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    #url('', include('languages.urls')),
    url('', include(router.urls)),
]
