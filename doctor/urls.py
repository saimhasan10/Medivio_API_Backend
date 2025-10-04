from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

router = DefaultRouter()  # router

router.register("list", views.DoctorViewset)  # antena
router.register("specialization", views.SpecializationViewset)
router.register("designation", views.DesignationViewset)
router.register("available_time", views.AvailableTimeViewset)
router.register("reviews", views.ReviewViewset)

urlpatterns = [
    path("", include(router.urls)),
]
