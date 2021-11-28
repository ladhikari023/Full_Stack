from django.urls import path
from . import views



urlpatterns = [
    path('',views.PlanListView.as_view(),name='plan_list'),
    path('about/',views.AboutView.as_view(),name='about'),
    path('plans/',views.PlanCreateView.as_view(),name='new_plan'),
    path('drafts/',views.PlanDraftListView.as_view(),name='plan_draft_list'),
    path('plan/<int:pk>/',views.PlanDetailView.as_view(),name='plan_detail'),
    path('plan/<int:pk>/update/',views.PlanUpdateView.as_view(),name='plan_update'),
    path('plan/<int:pk>/remove/',views.PlanDeleteView.as_view(),name='plan_remove'),
    path('plan/<int:pk>/publish/',views.plan_publish,name='plan_publish'),
    path('register/',views.register_user,name='register'),
]
