from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = "tatilturapp"

urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('case/',views.case,name='case'),
    path('favori/',views.favourites,name='favourites'),
    path('signup/',views.SignUpView.as_view(),name='signup'),
    path('çanakkale/',views.çanakkale,name='çanakkale'),
    path('case/çanakkale/',views.caseçanakkale,name='caseçanakkale'),
    path('bursa/',views.bursa,name='bursa'),
    path('case/bursa/',views.casebursa,name='casebursa'),
    path('izmir/',views.izmir,name='izmir'),
    path('case/izmir/',views.caseizmir,name='caseizmir'),
    path('antalya',views.antalya,name='antalya'),
    path('case/antalya/',views.caseantalya,name='caseantalya'),
    path('istanbul/',views.istanbul,name='istanbul'),
    path('case/istanbul/',views.caseistanbul,name='caseistanbul'),
    path('muğla/',views.muğla,name='muğla'),
    path('case/muğla/',views.casemuğla,name='casemuğla'),
    path('trabzon/',views.trabzon,name='trabzon'),
    path('case/trabzon/',views.casetrabzon,name='casetrabzon'),
    path('adana/',views.adana,name='adana'),
    path('case/adana/',views.caseadana,name='caseadana'),
]
