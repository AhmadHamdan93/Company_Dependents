from django.urls import path
from . import views

urlpatterns =[
    path('',views.show_all_emps,name="allEmps"),
    path('dependent/<str:id>/',views.show_dependent,name="allDependent"),
    # paths for main operations
    path('deleteDependent/',views.deleteDependent,name="delete"),
    path('insertDependent/',views.insertDependent,name="insert"),
    path('updateDependent/',views.updateDependent,name="update"),
]