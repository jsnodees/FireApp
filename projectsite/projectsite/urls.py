from django.contrib import admin
from django.urls import path

from fire.views import HomePageView, ChartView, PieCountbySeverity, LineCountbyMonth, MultilineIncidentTop3Country, multipleBarbySeverity, IncidentList, IncidentCreateView, IncidentUpdateView, IncidentDeleteView, LocationsList, LocationsCreateView, LocationsUpdateView, LocationsDeleteView, FireStationList, FireStationCreateView, FireStationUpdateView, FireStationDeleteView
from fire import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
    path('stations', views.map_station, name='map-station'),
    path('incidents', views.map_incident, name='map-incident'),
    path('dashboard_chart', ChartView.as_view(), name='dashboard-chart'),
    path('chart/', PieCountbySeverity, name='chart'),
    path('lineChart/', LineCountbyMonth, name='chart'),
    path('multilineChart/', MultilineIncidentTop3Country, name='chart'),
    path('multiBarChart/', multipleBarbySeverity, name='chart'),
    path('incident_list', IncidentList.as_view(), name='incident-list'),
    path('incident_list/add', IncidentCreateView.as_view(), name='incident-add'),
    path('incident_list/<pk>',IncidentUpdateView.as_view(), name='incident-update'),
    path('incident_list/<pk>/delete', IncidentDeleteView.as_view(), name='incident-delete'),
    path('location_list', LocationsList.as_view(), name='location-list'),
    path('location_list/add', LocationsCreateView.as_view(), name='location-add'),
    path('location_list/<pk>',LocationsUpdateView.as_view(), name='location-update'),
    path('location_list/<pk>/delete', LocationsDeleteView.as_view(), name='location-delete'),
    path('firestation_list', FireStationList.as_view(), name='firestation-list'),
    path('firestation_list/add', FireStationCreateView.as_view(), name='firestation-add'),
    path('firestation_list/<pk>',FireStationUpdateView.as_view(), name='firestation-update'),
    path('firestation_list/<pk>/delete', FireStationDeleteView.as_view(), name='firestation-delete'),
]