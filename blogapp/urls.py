from django.urls import path
from .views import homepage,ajaxsave
app_name = 'blogapp'

urlpatterns = [
    path('homepage/',homepage),
    path('ajaxsaved/',ajaxsave,name="ajaxsaved"),
]
