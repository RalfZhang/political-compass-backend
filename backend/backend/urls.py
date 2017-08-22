from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
import sys
sys.path.append("..")
from qaa import views

router = routers.DefaultRouter()
router.register(r'questions', views.QuestionViewSet)
router.register(r'answers', views.AnswerViewSet)

urlpatterns = [
    # Examples:
    # url(r'^$', 'backend.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^qaa/', include('qaa.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
