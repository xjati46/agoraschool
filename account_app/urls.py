from django.urls import path
from account_app import views


app_name = 'account-app'

urlpatterns = [
    # ############################## ADMIN VIEWS ##############################
    path('admin_app/', views.HomeAdminView.as_view(), name='home-admin'),
    # ADMIN LIST VIEW --------------------------------------------------
    path(
        'admin_app/kelas/',
        views.KelasAdminView.as_view(),
        name='kelas-admin'),
    path(
        'admin_app/murid/',
        views.MuridAdminView,
        name='murid-admin'),
    path(
        'admin_app/murid/nama/',
        views.SortNamaMuridAdminView,
        name='sortnama-murid-admin'),
    path(
        'admin_app/mapel/',
        views.MapelAdminView.as_view(),
        name='mapel-admin'),
    path(
        'admin_app/guru/',
        views.GuruAdminView,
        name='guru-admin'),
    path(
        'admin_app/guru/nama/',
        views.SortNamaGuruAdminView,
        name='sortnama-guru-admin'),
    # ADMIN DETAIL VIEW --------------------------------------------------
    path(
        'admin_app/guru/<int:pk>/',
        views.GuruAdminDetailView.as_view(),
        name='guru-admin-detail'),
    path(
        'admin_app/murid/<int:pk>/',
        views.MuridAdminDetailView.as_view(),
        name='murid-admin-detail'),
    path(
        'admin_app/kelas/<int:pk>/',
        views.KelasAdminDetailView.as_view(),
        name='kelas-admin-detail'),
    path(
        'admin_app/mapel/<int:pk>/',
        views.MapelAdminDetailView.as_view(),
        name='mapel-admin-detail'),
    path(
        'admin_app/mapel/kurikulum/<int:pk>/',
        views.KurikulumAdminDetailView.as_view(),
        name='kurikulum-admin-detail'),
    path(
        'admin_app/log_mengajar/<int:pk>/',
        views.LogMengajarAdminDetailView.as_view(),
        name='logmengajar-admin-detail'),
    # ############################## GURU VIEWS ##############################
    path('guru_app/', views.HomeGuruView.as_view(), name='home-guru'),
    # GURU LIST VIEW --------------------------------------------------
    path(
        'guru_app/kelas/',
        views.KelasGuruView.as_view(),
        name='kelas-guru'),
    path(
        'guru_app/mapel/',
        views.MapelGuruView.as_view(),
        name='mapel-guru'),
    # GURU DETAIL VIEW --------------------------------------------------
    path(
        'guru_app/kelas/<int:pk>/',
        views.KelasGuruDetailView.as_view(),
        name='kelas-guru-detail'),
    path(
        'guru_app/murid/<int:pk>/',
        views.MuridGuruDetailView.as_view(),
        name='murid-guru-detail'),
    path(
        'guru_app/mapel/<int:pk>/',
        views.MapelGuruDetailView.as_view(),
        name='mapel-guru-detail'),
    path(
        'guru_app/mapel/kurikulum/<int:pk>/',
        views.KurikulumGuruDetailView.as_view(),
        name='kurikulum-guru-detail'),
    path(
        'guru_app/log_mengajar/<int:pk>/',
        views.LogMengajarGuruDetailView.as_view(),
        name='logmengajar-guru-detail'),
    # GURU CREATE VIEW --------------------------------------------------
    path(
        'guru_app/mapel/kurikulum/tambah/',
        views.KurikulumGuruCreateView.as_view(),
        name='kurikulum-guru-tambah'),
    path(
        'guru_app/log_mengajar/tambah/',
        views.LogMengajarGuruCreateView.as_view(),
        name='logmengajar-guru-tambah'),
    # ############################## ADMIN VIEWS ##############################
    path('murid_app/', views.HomeMuridView.as_view(), name='home-murid'),
    # MURID LIST VIEW --------------------------------------------------
    path(
        'murid_app/mapel/',
        views.MapelMuridView.as_view(),
        name='mapel-murid'),
    # MURID DETAIL VIEW --------------------------------------------------
    path(
        'murid_app/mapel/<int:pk>/',
        views.MapelMuridDetailView.as_view(),
        name='mapel-murid-detail'),
    path(
        'murid_app/mapel/kurikulum/<int:pk>/',
        views.KurikulumMuridDetailView.as_view(),
        name='kurikulum-murid-detail'),
]
