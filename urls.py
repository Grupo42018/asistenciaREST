from django.conf.urls import url
from REST import views

urlpatterns = [
    url(r'^$', views.check, name='HEAD'),
    url(r'^students', views.getStudents.as_view(), name='get_students'),
    url(r'^preceptors', views.getPreceptors.as_view(), name='get_preceptors'),
    url(r'^parents', views.getParents.as_view(), name='get_parents'),
    url(r'^years', views.getYears.as_view(), name='get_years'),
    url(r'^registros', views.getRegistros.as_view(), name='get_registros'),
    url(r'^absence/$', views.getAbsences.as_view(), name='get_absences'),
    url(r'^absence/(?P<pk>[0-9]+)', views.Absence.as_view(), name='absence'),
]