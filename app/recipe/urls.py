"""URL mapping for Recipe"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from recipe import views

router=DefaultRouter()

router.register('receipes', views.RecipeViewSets)
app_name = 'recipe'

urlpatterns = [
    path('', include(router.urls)),
]