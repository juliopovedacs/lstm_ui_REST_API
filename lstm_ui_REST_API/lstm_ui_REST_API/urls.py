#------------------------------------------------------------------------------
# LSTM UI REST API
# By japoveda10
# urls.py
# This file configures the app's urls
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# Imports
#------------------------------------------------------------------------------
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from api import views

#------------------------------------------------------------------------------
# Router
#------------------------------------------------------------------------------
router = routers.DefaultRouter()
router.register('event_logs', views.EventLogViewSet)
router.register('trained_models', views.TrainedModelViewSet)
router.register('results', views.ResultViewSet)
router.register('running_cases', views.RunningCaseViewSet)
router.register('activities', views.ActivityViewSet)
router.register('roles', views.RoleViewSet)
router.register('times', views.TimeViewSet)


#------------------------------------------------------------------------------
# Url patterns
#------------------------------------------------------------------------------
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
