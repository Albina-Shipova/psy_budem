from django.urls import path
from budemapp.views import Main, SeminarDetail


urlpatterns = [
    path('', Main.as_view(), name='main'),
    path('psy', Main.as_view(template_name="budemapp/psy_seminars.html"), name='psy',),
    path('business', Main.as_view(template_name="budemapp/business_seminars.html"), name='business'),
    path('health', Main.as_view(template_name="budemapp/health_seminars.html"), name='health'),
    path("detail/<int:pk>/", SeminarDetail.as_view(), name='detail'),
]
