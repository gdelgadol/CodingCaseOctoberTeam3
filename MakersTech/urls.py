"""
URL configuration for MakersTech project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from MakersTech.MakersTechApp import views
from MakersTech.chat.views import ChatBotAPIView

router = DefaultRouter()
router.register(r"brand", views.BrandViewSet)
router.register(r"feature", views.FeatureViewSet)
router.register(r"product",views.ProductViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include(router.urls)),
    path("api/chat/", ChatBotAPIView.as_view(), name="chat_api"),
]
