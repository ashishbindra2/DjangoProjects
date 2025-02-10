from django.urls import path
from . import views
urlpatterns = [
    path('',views.index_view),
    path('check/', views.check_view),
    path('count/', views.count_view),
    path('home/',views.home_view),
    path('second/',views.date_time_view),
    path('result/',views.result_view),
    # path('name/', views.name_view),
    # path('age/', views.age_view),
    # path('gf/', views.gf_view),
    # path('results/', views.results_view),
    # shopping
    path('index/',views.index),
    path('additem/',views.add_item),
    path('display',views.display_item_view),
    # session
    path('pageCount/',views.page_count_view),
    path('age/',views.age_session_view),
    path('gf/',views.gf_session_view),
    path('name/',views.name_session_view),
    path('results/',views.results_session_view),
    path('add_item',views.add_item_view),
    path('displayitem', views.display_items_view),
]