from django.conf.urls import url
from . import views
from django.views.generic.base import RedirectView


urlpatterns = [
    url(r'^$', views.LoginView.as_view(), name='login_user'),
    url(r'^login/$', views.LoginView.as_view(), name='login_user'),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout_user'),
    url(r'^stud_profile/$', views.stud_profile, name='stud_profile'),
    url(r'^rules/$', views.rules, name='rules'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^no_dues_apply/$', views.no_dues_apply, name='no_dues_apply'),
    url(r'^stud_full_dept/$', views.stud_full_dept, name='stud_full_dept'),
    url(r'^stud_full_lab/$', views.stud_full_lab, name='stud_full_lab'),
    url(r'^faculty_profile/$', views.faculty_profile, name='faculty_profile'),
    # url(r'^library_profile/$', views.library_profile, name='library_profile'),
    # url(r'^caretaker_profile/$', views.caretaker_profile, name='caretaker_profile'),
    # url(r'^gymkhana_profile/$', views.gymkhana_profile, name='gymkhana_profile'),
    # url(r'^assireg_profile/$', views.assireg_profile, name='assireg_profile'),
    url(r'^stud_nodues/$', views.stud_nodues, name='stud_nodues'),
    url(r'^stud_dues/$', views.stud_dues, name='stud_dues'),
    url(r'^stud_search/$', views.stud_search, name='stud_search'),
    url(r'^hostel_update/$', views.hostel_update, name='hostel_update'),
    # url(r'^onlinecc_profile/$', views.onlinecc_profile, name='onlinecc_profile'),
    # url(r'^cc_profile/$', views.cc_profile, name='cc_profile'),
    # url(r'^thesis_manager_profile/$', views.thesis_manager_profile, name='thesis_manager_profile'),
    # url(r'^lab_profile/$', views.lab_profile, name='lab_profile'),
    # url(r'^hod_profile/$', views.hod_profile, name='hod_profile'),
    # url(r'^account_profile/$', views.account_profile, name='account_profile'),
    url(r'^search_faculties/$',views.search_faculties, name='search_faculties'),
    url(r'^add_faculty/$',views.add_faculty, name='add_faculty'),
    # url(r'^update_status/$',views.update_status, name='update_status'),
    # url(r'^update_remarks/$',views.update_remarks, name='update_remarks'),
    # url(r'^update_status/$', views.update_status, name='update_status'),
    # url(r'^update_remarks/$', views.update_remarks, name='update_remarks'),
    # url(r'^update_lab_status/$', views.update_lab_status, name='update_lab_status'),
    # url(r'^update_lab_remarks/$', views.update_lab_remarks, name='update_lab_remarks'),
    url(r'^update_faculty_status/$', views.update_faculty_status, name='update_faculty_status'),
    # url(r'^update_faculty_remarks/$', views.update_faculty_remarks, name='update_faculty_remarks'),
    # url(r'^search_students/$', views.search_students, name='search_students'),
    # url(r'^add_student/$', views.add_student, name='add_student'),
    url(r'^delete_student/$', views.delete_student, name='delete_student'),
    url(r'^faculty_pending/$', views.faculty_pending, name='faculty_pending'),
    url(r'^faculty_approved/$', views.faculty_approved, name='faculty_approved'),
    url(r'^faculty_rejected/$', views.faculty_rejected, name='faculty_rejected'),
    url(r'^dept_admin$', views.dept_admin, name='dept_admin'),
    url(r'^add_lab$', views.add_lab, name='add_lab'),
    url(r'^delete_lab/$', views.delete_lab, name='delete_lab'),

]

    #url(r'^stud_profile/(?P<username>\w+)/', views.stud_profile, name='stud_overall'),
    #url(r'^stud_profile/(.*)/dept$', views.stud_full_dept, name='stud_dept'),
    #url(r'^stud_profile/(.*)/lab$',views.stud_full_lab , name='stud_lab'),


#index is view name
