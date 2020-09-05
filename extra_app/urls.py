from django.urls import path
from extra_app import views


app_name = 'extra-app'

urlpatterns = [
    # ############################## ADMIN VIEWS ##############################
    # PENGUMUMAN APPS --------------------------------------------------
    path(
        'admin_app/pengumuman/',
        views.PengumumanAdminView.as_view(),
        name='pengumuman-admin'),
    path(
        'admin_app/pengumuman/<int:pk>/',
        views.PengumumanAdminDetailView.as_view(),
        name='pengumuman-admin-detail'),
    path(
        'admin_app/pengumuman/tambah/',
        views.PengumumanAdminCreateView.as_view(),
        name='pengumuman-tambah'),
    # NILAI APPS --------------------------------------------------
    path(
        'admin_app/nilai_murid/',
        views.NilaiMuridAdminView.as_view(),
        name='nilaimurid-admin'),
    path(
        'admin_app/nilai_murid/tambah/',
        views.NilaiMuridAdminCreateView.as_view(),
        name='nilaimurid-tambah'),
    # LAPORAN APPS --------------------------------------------------
    path(
        'admin_app/laporan_murid/',
        views.LaporanMuridAdminView.as_view(),
        name='laporanmurid-admin'),
    path(
        'admin_app/laporan_murid/<int:pk>/',
        views.LaporanMuridAdminDetailView.as_view(),
        name='laporanmurid-admin-detail'),
    path(
        'admin_app/laporan_murid/tambah/',
        views.LaporanMuridAdminCreateView.as_view(),
        name='laporanmurid-tambah'),
    # TAGIHAN APPS --------------------------------------------------
    path(
        'admin_app/tagihan_murid/',
        views.TagihanMuridAdminView.as_view(),
        name='tagihanmurid-admin'),
    path(
        'admin_app/tagihan_murid/tambah/',
        views.TagihanMuridAdminCreateView.as_view(),
        name='tagihanmurid-tambah'),
    # ############################## GURU VIEWS ##############################
    # NILAI APPS --------------------------------------------------
    path(
        'guru_app/nilai_murid/',
        views.NilaiMuridGuruView.as_view(),
        name='nilaimurid-guru'),
    path(
        'guru_app/nilai_murid/tambah/',
        views.NilaiMuridGuruCreateView.as_view(),
        name='nilaimurid-guru-tambah'),
    # LAPORAN APPS --------------------------------------------------
    path(
        'guru_app/laporan_murid/',
        views.LaporanMuridGuruView.as_view(),
        name='laporanmurid-guru'),
    path(
        'guru_app/laporan_murid/<int:pk>/',
        views.LaporanMuridGuruDetailView.as_view(),
        name='laporanmurid-guru-detail'),
    path(
        'guru_app/laporan_murid/tambah/',
        views.LaporanMuridGuruCreateView.as_view(),
        name='laporanmurid-guru-tambah'),
    # PENGUMUMAN APPS --------------------------------------------------
    path(
        'guru_app/pengumuman/',
        views.PengumumanGuruView.as_view(),
        name='pengumuman-guru'),
    path(
        'guru_app/pengumuman/<int:pk>/',
        views.PengumumanGuruDetailView.as_view(),
        name='pengumuman-guru-detail'),
    # ############################## MURID VIEWS ##############################
    # TAGIHAN APPS --------------------------------------------------
    path(
        'murid_app/tagihan_murid/',
        views.TagihanMuridMuridView.as_view(),
        name='tagihanmurid-murid'),
    # PENGUMUMAN APPS --------------------------------------------------
    path(
        'murid_app/pengumuman/',
        views.PengumumanMuridView.as_view(),
        name='pengumuman-murid'),
    path(
        'murid_app/pengumuman/<int:pk>/',
        views.PengumumanMuridDetailView.as_view(),
        name='pengumuman-murid-detail'),
    # NILAI APPS --------------------------------------------------
    path(
        'murid_app/nilai_murid/',
        views.NilaiMuridMuridView.as_view(),
        name='nilaimurid-murid'),
    # LAPORAN APPS --------------------------------------------------
    path(
        'murid_app/laporan_murid/',
        views.LaporanMuridMuridView.as_view(),
        name='laporanmurid-murid'),
    path(
        'murid_app/laporan_murid/<int:pk>/',
        views.LaporanMuridMuridDetailView.as_view(),
        name='laporanmurid-murid-detail'),
]
