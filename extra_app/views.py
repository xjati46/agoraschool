from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import UserPassesTestMixin
from extra_app.models import Pengumuman, NilaiMurid, LaporanMurid, TagihanMurid
from django.urls import reverse_lazy
from extra_app.forms import (
                            PengumumanForm, NilaiMuridForm, LaporanMuridForm,
                            TagihanMuridForm,)


# ############################## ADMIN VIEWS ##############################
# PENGUMUMAN APPS -------------------------------------------------------------
class PengumumanAdminView(UserPassesTestMixin, ListView):
    model = Pengumuman
    template_name = 'extra_app/admin/pengumuman/pengumuman_list.html'

    def test_func(self):
        return self.request.user.groups.filter(name="admin").exists()

    def handle_no_permission(self):
        return redirect('denied-access')


class PengumumanAdminDetailView(UserPassesTestMixin, DetailView):
    model = Pengumuman
    template_name = 'extra_app/admin/pengumuman/pengumuman_detail.html'

    def test_func(self):
        return self.request.user.groups.filter(name="admin").exists()

    def handle_no_permission(self):
        return redirect('denied-access')


class PengumumanAdminCreateView(UserPassesTestMixin, CreateView):
    form_class = PengumumanForm
    success_url = reverse_lazy('extra-app:pengumuman-admin')
    template_name = 'extra_app/admin/pengumuman/pengumuman_form.html'

    def test_func(self):
        return self.request.user.groups.filter(name="admin").exists()

    def handle_no_permission(self):
        return redirect('denied-access')


# NILAI APPS ------------------------------------------------------------------
class NilaiMuridAdminView(UserPassesTestMixin, ListView):
    model = NilaiMurid
    template_name = 'extra_app/admin/nilai_murid/nilaimurid_list.html'

    def test_func(self):
        return self.request.user.groups.filter(name="admin").exists()

    def handle_no_permission(self):
        return redirect('denied-access')


class NilaiMuridAdminCreateView(UserPassesTestMixin, CreateView):
    form_class = NilaiMuridForm
    success_url = reverse_lazy('extra-app:nilaimurid-admin')
    template_name = 'extra_app/admin/nilai_murid/nilaimurid_form.html'

    def test_func(self):
        return self.request.user.groups.filter(name="admin").exists()

    def handle_no_permission(self):
        return redirect('denied-access')


# LAPORAN APPS ----------------------------------------------------------------
class LaporanMuridAdminView(UserPassesTestMixin, ListView):
    model = LaporanMurid
    template_name = 'extra_app/admin/laporan_murid/laporanmurid_list.html'

    def test_func(self):
        return self.request.user.groups.filter(name="admin").exists()

    def handle_no_permission(self):
        return redirect('denied-access')


class LaporanMuridAdminDetailView(UserPassesTestMixin, DetailView):
    model = LaporanMurid
    template_name = 'extra_app/admin/laporan_murid/laporanmurid_detail.html'

    def test_func(self):
        return self.request.user.groups.filter(name="admin").exists()

    def handle_no_permission(self):
        return redirect('denied-access')


class LaporanMuridAdminCreateView(UserPassesTestMixin, CreateView):
    form_class = LaporanMuridForm
    success_url = reverse_lazy('extra-app:laporanmurid-admin')
    template_name = 'extra_app/admin/laporan_murid/laporanmurid_form.html'

    def test_func(self):
        return self.request.user.groups.filter(name="admin").exists()

    def handle_no_permission(self):
        return redirect('denied-access')


# TAGIHAN APPS ----------------------------------------------------------------
class TagihanMuridAdminView(UserPassesTestMixin, ListView):
    model = TagihanMurid
    template_name = 'extra_app/admin/tagihan_murid/tagihanmurid_list.html'

    def test_func(self):
        return self.request.user.groups.filter(name="admin").exists()

    def handle_no_permission(self):
        return redirect('denied-access')


class TagihanMuridAdminCreateView(UserPassesTestMixin, CreateView):
    form_class = TagihanMuridForm
    success_url = reverse_lazy('extra-app:tagihanmurid-admin')
    template_name = 'extra_app/admin/tagihan_murid/tagihanmurid_form.html'

    def test_func(self):
        return self.request.user.groups.filter(name="admin").exists()

    def handle_no_permission(self):
        return redirect('denied-access')


# ############################## END-ADMIN VIEWS ##############################


# ############################## GURU VIEWS ##############################
# NILAI APPS ------------------------------------------------------------------
class NilaiMuridGuruView(UserPassesTestMixin, ListView):
    template_name = 'extra_app/guru/nilai_murid/nilaimurid_list.html'

    def get_queryset(self):
        return NilaiMurid.objects.filter(pembuat_tes=self.request.user.id)

    def test_func(self):
        return self.request.user.groups.filter(name="guru").exists()

    def handle_no_permission(self):
        return redirect('denied-access')


class NilaiMuridGuruCreateView(UserPassesTestMixin, CreateView):
    form_class = NilaiMuridForm
    success_url = reverse_lazy('extra-app:nilaimurid-guru')
    template_name = 'extra_app/guru/nilai_murid/nilaimurid_form.html'

    def test_func(self):
        return self.request.user.groups.filter(name="guru").exists()

    def handle_no_permission(self):
        return redirect('denied-access')


# LAPORAN APPS ----------------------------------------------------------------
class LaporanMuridGuruView(UserPassesTestMixin, ListView):
    template_name = 'extra_app/guru/laporan_murid/laporanmurid_list.html'

    def get_queryset(self):
        return LaporanMurid.objects.filter(pelapor=self.request.user.id)

    def test_func(self):
        return self.request.user.groups.filter(name="guru").exists()

    def handle_no_permission(self):
        return redirect('denied-access')


class LaporanMuridGuruDetailView(UserPassesTestMixin, DetailView):
    model = LaporanMurid
    template_name = 'extra_app/guru/laporan_murid/laporanmurid_detail.html'

    def test_func(self):
        return self.request.user.groups.filter(name="guru").exists()

    def handle_no_permission(self):
        return redirect('denied-access')


class LaporanMuridGuruCreateView(UserPassesTestMixin, CreateView):
    form_class = LaporanMuridForm
    success_url = reverse_lazy('extra-app:laporanmurid-guru')
    template_name = 'extra_app/guru/laporan_murid/laporanmurid_form.html'

    def test_func(self):
        return self.request.user.groups.filter(name="guru").exists()

    def handle_no_permission(self):
        return redirect('denied-access')


# PENGUMUMAN APPS -------------------------------------------------------------
class PengumumanGuruView(UserPassesTestMixin, ListView):
    template_name = 'extra_app/guru/pengumuman/pengumuman_list.html'

    def get_queryset(self):
        return Pengumuman.objects.filter(kategori__exact='Guru')

    def test_func(self):
        return self.request.user.groups.filter(name="guru").exists()

    def handle_no_permission(self):
        return redirect('denied-access')


class PengumumanGuruDetailView(UserPassesTestMixin, DetailView):
    model = Pengumuman
    template_name = 'extra_app/guru/pengumuman/pengumuman_detail.html'

    def test_func(self):
        return self.request.user.groups.filter(name="guru").exists()

    def handle_no_permission(self):
        return redirect('denied-access')


# ############################## END-GURU VIEWS ##############################


# ############################## MURID VIEWS ##############################
# TAGIHAN APPS ----------------------------------------------------------------
class TagihanMuridMuridView(UserPassesTestMixin, ListView):
    template_name = 'extra_app/murid/tagihan_murid/tagihanmurid_list.html'

    def get_queryset(self):
        return TagihanMurid.objects.filter(
            tertagih__murid=self.request.user.id).filter(status_bayar=True)

    def test_func(self):
        return self.request.user.groups.filter(name="murid").exists()

    def handle_no_permission(self):
        return redirect('denied-access')


# PENGUMUMAN APPS -------------------------------------------------------------
class PengumumanMuridView(UserPassesTestMixin, ListView):
    template_name = 'extra_app/murid/pengumuman/pengumuman_list.html'

    def get_queryset(self):
        return Pengumuman.objects.filter(kategori__exact='Murid')

    def test_func(self):
        return self.request.user.groups.filter(name="murid").exists()

    def handle_no_permission(self):
        return redirect('denied-access')


class PengumumanMuridDetailView(UserPassesTestMixin, DetailView):
    model = Pengumuman
    template_name = 'extra_app/murid/pengumuman/pengumuman_detail.html'

    def test_func(self):
        return self.request.user.groups.filter(name="murid").exists()

    def handle_no_permission(self):
        return redirect('denied-access')


# NILAI APPS ------------------------------------------------------------------
class NilaiMuridMuridView(UserPassesTestMixin, ListView):
    template_name = 'extra_app/murid/nilai_murid/nilaimurid_list.html'

    def get_queryset(self):
        return NilaiMurid.objects.filter(
            peserta_tes__murid=self.request.user.id)

    def test_func(self):
        return self.request.user.groups.filter(name="murid").exists()

    def handle_no_permission(self):
        return redirect('denied-access')


# LAPORAN APPS ----------------------------------------------------------------
class LaporanMuridMuridView(UserPassesTestMixin, ListView):
    template_name = 'extra_app/murid/laporan_murid/laporanmurid_list.html'

    def get_queryset(self):
        return LaporanMurid.objects.filter(
            terlapor__murid=self.request.user.id)

    def test_func(self):
        return self.request.user.groups.filter(name="murid").exists()

    def handle_no_permission(self):
        return redirect('denied-access')


class LaporanMuridMuridDetailView(UserPassesTestMixin, DetailView):
    model = LaporanMurid
    template_name = 'extra_app/murid/laporan_murid/laporanmurid_detail.html'

    def test_func(self):
        return self.request.user.groups.filter(name="murid").exists()

    def handle_no_permission(self):
        return redirect('denied-access')


# ############################## END-MURID VIEWS ##############################
