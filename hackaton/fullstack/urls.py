from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    
    path("profile/", views.user_profile, name="profile"),
    
    path("login/", views.login_p, name="login"),
    path("register/", views.register, name="register"),
    
    path("search_inn/", views.search_inn, name="search_inn"),
    
    # path("questions/", views.questions, name="questions"),
    # path("question/<int:question_id>/", views.edit_question, name="question_edit"),
    
    # path("dialogs/", views.dialogs, name="dialogs"),
    # path("dialog/<str:chat_id>/", views.dialog, name="dialog_view"),
    
    # path("scenario/", views.scenario, name="scenario"),
    # path("scenario/answer/", views.scenario_answer, name="scenario_answer"),
    # path("scenario/save/", views.scenario_save, name="scenario_save"),
    # path("scenario/editAnswer/", views.scenario_answer_edit, name="scenario_answer_edit"),
    
    # path("main-menu/", views.main_menu, name="main-menu"),
    # path("main-menu/button/<int:button_id>/", views.edit_main_menu_button, name="edit-main-menu-button"),
]