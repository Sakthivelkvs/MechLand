"""
URL configuration for MechLand project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from myapp import views
from django.conf.urls.static import static



urlpatterns = [

    path('unitcard/',views.unitcard),
    path('dashboard/',views.dashboard),

    path('admin/', admin.site.urls),

    path('',views.public_home2),
    path('login/',views.login1),
    path('login1_post/',views.login1_post),

    path('logout/',views.logout),

    path('admin_hm/',views.admin),
    path('admin2/',views.admin2),
    path('admin3/',views.admin3),
   

    path('admin_add_mould/',views.admin_add_mould),
    path('admin_add_mould_post/',views.admin_add_mould_post),
    path('admin_view_mould/',views.admin_view_mould),
    path('admin_edit_mould/<int:s1>/',views.admin_edit_mould),
    path('admin_edit_mould_post/',views.admin_edit_mould_post),
    path('admin_delete_mould/<int:s2>/',views.admin_delete_mould),

    path('admin_add_predict_mould/',views.admin_add_predict_mould),
    path('admin_add_predict_mould_post/',views.admin_add_predict_mould_post),
    path('admin_view_predict_mould/',views.admin_view_predict_mould),
    path('admin_edit_predict_mould/<int:s3>/',views.admin_edit_predict_mould),
    path('admin_edit_predict_mould_post/',views.admin_edit_predict_mould_post),
    path('admin_delete_predict_mould/<int:s4>/',views.delete_predict_mouold),
    path('admin_view_public_ratting/',views.admin_view_public_ratting),
    path('admin_view_public_ratting2/<int:s1>/',views.admin_view_public_ratting2),

    path('admin_add_job/',views.admin_add_job),
    path('admin_add_job_post/',views.admin_add_job_post),
    path('admin_view_job/',views.admin_view_job),
    path('admin_edit_job/<int:s5>/',views.admin_edit_job),
    path('admin_edit_job_post/',views.admin_edit_job_post),
    path('admin_delete_job/<int:s6>/',views.admin_delete_job),

    
    path('admin_add_staff_post/<int:id>',views.admin_add_staff_post),
    path('admin_view_staff/',views.admin_view_staff),
    path('admin_view_staff_post/',views.admin_view_staff_post),
    path('admin_edit_staff/<int:s7>/',views.admin_edit_staff),
    path('admin_edit_staff_post/',views.admin_edit_staff_post),
    path('admin_delete_staff/<int:s8>/',views.admin_delete_staff),

    path('admin_allot_manager/',views.admin_allot_manager),
    path('admin_allot_manager_post2/',views.admin_allot_manager_post2),
    path('admin_allot_manager_post/',views.admin_allot_manager_post),
    path('admin_view_manager/',views.admin_view_manager),
    path('admin_view_manager_post/',views.admin_view_manager_post),
    path('admin_delete_manager/<int:s21>/',views.admin_delete_manager),

    path('admin_add_vacancy/<int:s3>',views.admin_add_vacancy),
    path('admin_add_vacancy_post/',views.admin_add_vacancy_post),
    path('admin_view_vacancy/<int:job_id>',views.admin_view_vacancy),
    path('admin_edit_vacancy/<int:s9>/',views.admin_edit_vacancy),
    path('admin_edit_vacancy_post/<int:s1>',views.admin_edit_vacancy_post),
    path('admin_delete_vacancy/<int:s10>/',views.admin_delete_vacancy),

    path('admin_add_shift/',views.admin_add_shift),
    path('admin_add_shift_post/',views.admin_add_shift_post),
    path('admin_view_shift/',views.admin_view_shift),
    path('admin_view_staff_details/<int:s12>',views.admin_view_staff_details),
    path('admin_edit_shift/<int:s11>/',views.admin_edit_shift),
    path('admin_edit_shift_post/',views.admin_edit_shift_post),

    path('admin_view_unit_request/',views.admin_view_unit_request),
    path('admin_view_unit_request_post/',views.admin_view_unit_request_post),
    path('admin_approve_unit_request/<int:s12>',views.admin_approve_unit_request),
    path('admin_reject_unit_request/<int:s13>',views.admin_reject_unit_request),
    path('admin_view_approve_unit_request/',views.admin_view_approve_unit_request),

    path('admin_view_carrier_application/',views.admin_view_carrier_application),
    path('admin_allot_interview/<int:s30>',views.admin_allot_interview),
    path('admin_allot_interview_post/',views.admin_allot_interview_post),
    path('admin_view_carrier_application_post/',views.admin_view_carrier_application_post),
    path('admin_view_carrier_application_labour/',views.admin_view_carrier_application_labour),
    path('admin_view_carrier_application_supervisor/',views.admin_view_carrier_application_supervisor),
    path('admin_view_personal_details/<int:s9>',views.admin_view_personal_details),
    path('admin_delete_carrier_application/<int:s15>',views.admin_delete_carrier_application),
    path('admin_allotstaff/<int:s16>',views.admin_allotstaff),

    path('admin_view_business_request/',views.admin_view_business_request),
    path('admin_approve_business_request/<int:s16>',views.admin_approve_business_request),
    path('admin_approve_business_request_post/',views.admin_approve_business_request_post),
    path('admin_reject_business_request/<int:s17>',views.admin_reject_business_request),
    path('admin_view_approved_business_request/',views.admin_view_approved_business_request),

    # path('admin_add_loan_master/',views.admin_add_loan_master),
    # path('admin_add_loan_master_post/',views.admin_add_loan_master_post),
    # path('admin_view_loan_master/',views.admin_view_loan_master),
    # path('admin_edit_loan_master/<int:s12>/',views.admin_edit_loan_master),
    # path('admin_edit_loan_master_post/',views.admin_edit_loan_master_post),
    # path('admin_delete_loan_master/<int:s19>',views.admin_delete_loan_master),
    path('admin_view_loan_request/',views.admin_view_loan_request),
    path('admin_approve_loan_request/<int:s18>',views.admin_approve_loan_request),
    path('admin_reject_loan_request/<int:s19>',views.admin_reject_loan_request),
    path('admin_view_approved_loan_request/',views.admin_view_approved_loan_request),

    path('admin_set_leave_master/',views.admin_set_leave_master),
    path('admin_set_leave_master_post/',views.admin_set_leave_master_post),
    path('admin_view_leave_master/',views.admin_view_leave_master),
    path('admin_edit_leave_master/<int:s14>/',views.admin_edit_leave_master),
    path('admin_edit_leave_master_post/',views.admin_edit_leave_master_post),
    path('admin_delete_leave_master/<int:s18>/',views.admin_delete_leave_master),
    path('admin_view_leave_request/',views.admin_view_leave_request),
    path('admin_view_leave_request_post/',views.admin_view_leave_request),
    path('admin_approve_leave_request/<int:s22>',views.admin_approve_leave_request),
    path('admin_reject_leave_request/<int:s23>',views.admin_reject_leave_request),
    path('admin_view_approved_leave_request/',views.admin_view_approved_leave_request),

    path('admin_view_staff_advance_for_salary/<int:a1>',views.admin_view_staff_advance_for_salary),
    path('admin_view_staff_advance/',views.admin_view_staff_advance),
    path('admin_approve_advance_request/<int:a2>',views.admin_approve_advance_request),
    path('admin_reject_advance_request/<int:a3>',views.admin_reject_advance_request),
   

    path("admin_view_unit_reviews/", views.admin_view_unit_reviews),
    path('admin_view_unit_complaints/', views.admin_view_unit_complaints),
    path('admin_respond_unit_complaint/<int:s25>', views.admin_respond_unit_complaint),

    path('admin_view_section/', views.admin_view_section),
    path('admin_view_staff_for_attendance/', views.admin_view_staff_for_attendance),
    path('admin_add_attendance/<int:s2>',views.admin_add_attendance),
    path('admin_add_attendance_post/',views.admin_add_attendance_post),
    path('admin_view_attendance/',views.admin_view_attendance),
    path('admin_delete_attendance/<int:s11>', views.admin_delete_attendance),
    path('admin_view_section_for_salary/',views.admin_view_section_for_salary),
    # path('admin_view_staff_for_salary/',views.admin_view_staff_for_salary),
    path('admin_view_staff_leave_for_salary/<int:l1>',views.admin_view_staff_leave_for_salary),
    path('admin_view_staff_loan_for_salary/<int:l2>',views.admin_view_staff_loan_for_salary),
    path('admin_view_staff_adttendance_for_salary/<int:s2>',views.admin_view_staff_adttendance_for_salary),

    path('admin_prepare_salary_slip/<int:p1>',views.admin_prepare_salary_slip),


    path('admin_change_password/',views.admin_change_password),
    path('admin_change_password_post/',views.admin_change_password_post),
    path('admin_salary_post/<int:id>',views.admin_salary_post),

    path('admin_salary_report/',views.admin_salary_report),
    path('admin_salary_report_post/',views.admin_salary_report_post),
    path('admin_salary_report_post2/',views.admin_salary_report_post2),
    path('admin_leave_report/',views.admin_leave_report),
    path('admin_leave_report_post/',views.admin_leave_report_post),
    path('admin_leave_report_post2/',views.admin_leave_report_post2),
    path('admin_loan_report/',views.admin_loan_report),
    path('admin_loan_report_post/',views.admin_loan_report_post),
    path('admin_loan_report_post2/',views.admin_loan_report_post2),

    path('admin_logout/',views.admin_logout),
    path('supervisor_logout/',views.supervisor_logout),
    path('staff_logout/',views.staff_logout),

    ######################## UNIT ####################################
    
    path('unit_login/',views.unit_login),
    path('unit_reg/',views.unit_reg),
    path('unit_reg_post/',views.unit_reg_post),
    path('unitinner/',views.unitinner),
    path('unit_about/',views.unit_about),
    path('unit_service/',views.unit_service),
    path('unit_contact/',views.unit_contact),

    path('unit_view_profile/',views.unit_view_profile),
    path('unit_edit_profile/<int:s6>',views.unit_edit_profile),
    path('unit_edit_profile_post/',views.unit_edit_profile_post),

    path('unit_mould_review/<int:s28>',views.unit_mould_review),
    path('unit_mould_review_post/',views.unit_mould_review_post),

    path('unit_send_complaint/',views.unit_send_complaint),
    path('unit_send_complaint_post/',views.unit_send_complaint_post),
    path('unit_view_complaint/',views.unit_view_complaint),

    path('unit_view_moulds/',views.unit_view_moulds),
    path('unit_view_moulds_post/<int:s7>',views.unit_view_moulds_post),
    path('unit_order_moulds/<int:s1>',views.unit_order_moulds),
    path('unit_order_moulds_post/',views.unit_order_moulds_post),

    path('unit_view_order_status/',views.unit_view_order_status),
    path('unit_view_delivery_status/<int:s8>',views.unit_view_delivery_status),

    path('unit_make_payment/<str:s4>',views.unit_make_payment),
    path('unit_make_payment_post/',views.unit_make_payment_post),

    path('unit_cancel_order/<int:s3>',views.unit_cancel_order),
    path('unit_view_cancel_status/',views.unit_view_cancel_status),

    
    path('unit_change_password/',views.unit_change_password),
    path('unit_change_password_post/',views.unit_change_password_post),

    ######################## STAFF ####################################


    path('staff_login/',views.staff_login),
    path('employee_view_profile/',views.employee_view_profile),
    path('employee_edit_profile/<int:s7>',views.employee_edit_profile),
    path('employee_edit_profile_post/',views.employee_edit_profile_post),
    path('employee_loan_request/',views.employee_loan_request),
    path('employee_loan_request_post/',views.employee_loan_request_post),
    path('employee_view_loan_status/',views.employee_view_loan_status),

    path('employee_apply_advance/',views.employee_apply_advance),
    path('employee_apply_advance_post/',views.employee_apply_advance_post),
    path('employee_view_advance_status/',views.employee_view_advance_status),

    path('employee_view_attendance/',views.employee_view_attendance),



    path('employee_leave_request/',views.employee_leave_request),
    path('employee_leave_request_post/',views.employee_leave_request_post),
    path('employee_view_leave_status/',views.employee_view_leave_status),

    path('employee_view_salary_slip/',views.employee_view_salary_slip),

    path('employee_view_shift_allotment/',views.employee_view_shift_allotment),

    path('employee_change_password/',views.employee_change_password),
    path('employee_change_password_post/',views.employee_change_password_post),


     ########################PUBLIC####################################


    path('public_home/',views.public_home),
    path('public_home2/',views.public_home2),
    path('publicinner/',views.publicinner),
    path('public_about/',views.public_about),
    path('public_view_carrier/',views.public_view_carrier),
    path('public_service/',views.public_service),
    path('contact_service/',views.contact_service),
    path('public_view_vacancy/<int:s13>',views.public_view_vacancy),
    path('public_apply_job/<int:s14>',views.public_apply_job),
    path('public_apply_job_post/',views.public_apply_job_post),
    path('public_business_request/',views.public_business_request),
    path('public_business_request_post/',views.public_business_request_post),

    path('public_view_predict_mould/',views.public_view_predict_mould),
    path('public_rate_mould/<int:s2>',views.public_rate_mould),
    path('public_rate_mould_post/',views.public_rate_mould_post),

    ########################### MANAGER #################################

    path('manager_login/',views.manager_login),
    path('manager_view_profile/',views.manager_view_profile),

    path('manager_delete_order/<int:id>',views.manager_delete_order),

    path('manager_edit_profile/<int:s7>',views.manager_edit_profile),
    path('manager_edit_profile_post/',views.manager_edit_profile_post),

    path('manager_view_staff/',views.manager_view_staff),
    # path('manager_view_staff2/',views.manager_view_staff2),

    path('manager_view_section/',views.manager_view_section),
    path('manager_allot_staff/<int:s11>',views.manager_allot_staff),
    path('manager_allot_staff_post/',views.manager_allot_staff_post),
    path('manager_allot_shift/<int:s27>',views.manager_allot_shift),
    path('manager_allot_shift_post/',views.manager_allot_shift_post),
    path('manager_view_alloted_shift/',views.manager_view_alloted_shift),
    path('manager_view_alloted_shift_post/',views.manager_view_alloted_shift_post),

    path('manager_view_order/',views.manager_view_order),
    path('manager_check_payament/<int:s4>',views.manager_check_payament),
    path('manger_approve_order/<int:s6>',views.manger_approve_order),
    path('manager_approve_order_post/',views.manager_approve_order_post),
    path('manager_reject_order/<int:s7>',views.manager_reject_order),
    path('manager_view_approved_order/',views.manager_view_approved_order),
    path('manager_view_cancel_request/',views.manager_view_cancel_request),
    path('manager_approve_cancel_request/<int:s9>',views.manager_approve_cancel_request),
    path('manager_view_moulds/',views.manager_view_moulds),
    path('manager_add_stock/<int:s2>',views.manager_add_stock),
    path('manager_add_stock1/<int:s2>',views.manager_add_stock1),
    path('manager_change_password/',views.manager_change_password),
    path('manager_change_password_post/',views.manager_change_password_post),



    path('supervisor_login/',views.supervisor_login),
    path('supervisor_view_profile/',views.supervisor_view_profile),
    path('supervisor_edit_profile/<int:s7>',views.supervisor_edit_profile),
    path('supervisor_edit_profile_post/',views.supervisor_edit_profile_post),
    path('supervisor_change_password/',views.supervisor_change_password),
    path('supervisor_change_password_post/',views.supervisor_change_password_post),
    path('supervisor_view_staffs/',views.supervisor_view_staffs),   
    path('supervisor_allot_shift/<int:s2>',views.supervisor_allot_shift),
    path('supervisor_allot_shift_post/',views.supervisor_allot_shift_post),
    path('supervisor_loan_request/',views.supervisor_loan_request),
    path('supervisor_loan_request_post/',views.supervisor_loan_request_post),
    path('supervisor_view_loan_status/',views.supervisor_view_loan_status),
    path('supervisor_apply_advance/',views.supervisor_apply_advance),
    path('supervisor_apply_advance_post/',views.supervisor_apply_advance_post),
    path('supervisor_view_advance_status/',views.supervisor_view_advance_status),
    path('supervisor_leave_request/',views.supervisor_leave_request),
    path('supervisor_leave_request_post/',views.supervisor_leave_request_post),
    path('supervisor_view_leave_status/',views.supervisor_view_leave_status),
    path('supervisor_view_salary_slip/',views.supervisor_view_salary_slip),
    path('supervisor_view_attendance/',views.supervisor_view_attendance),

    path('mnr_idx/',views.mnr_idx),
    
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
