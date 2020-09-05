from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.contrib.auth.mixins import UserPassesTestMixin
from account_app.models import (
                                Kelas, AnggotaKelas, Mapel, TimMapel,
                                Kurikulum, LogMengajar
                                )
from account_app.filters import MuridAdminFilter, GuruAdminFilter
from django.contrib.auth.decorators import user_passes_test
from django.urls import reverse_lazy
from account_app.forms import KurikulumForm, LogMengajarForm
from extra_app.models import Pengumuman, TagihanMurid, NilaiMurid


def test_func(self):
    return self.groups.filter(name="admin").exists()


def test_func_2(self):
    return self.groups.filter(name="guru").exists()


def test_func_3(self):
    return self.groups.filter(name="murid").exists()


# ############################## ADMIN VIEWS ##############################
class HomeAdminView(UserPassesTestMixin, TemplateView):
    template_name = 'account_app/admin/home.html'

    def test_func(self):
        return self.request.user.groups.filter(name="admin").exists()

    def handle_no_permission(self):
        return redirect('denied-access')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['jumlah_murid'] = AnggotaKelas.objects.count()
        context['jumlah_guru'] = TimMapel.objects.count()
        context['jumlah_kelas'] = Kelas.objects.count()
        context['jumlah_mapel'] = Mapel.objects.count()
        return context


# ALL KELAS VIEW ------------------------------
class KelasAdminView(UserPassesTestMixin, ListView):
    model = Kelas
    template_name = 'account_app/admin/kelas_list.html'

    def test_func(self):
        return self.request.user.groups.filter(name="admin").exists()

    def handle_no_permission(self):
        return redirect('denied-access')


class KelasAdminDetailView(UserPassesTestMixin, DetailView):
    model = Kelas
    template_name = 'account_app/admin/kelas_detail.html'

    def test_func(self):
        return self.request.user.groups.filter(name="admin").exists()

    def handle_no_permission(self):
        return redirect('denied-access')


# ALL MURID VIEW ------------------------------
@user_passes_test(
    test_func,
    login_url='/denied-access/',
    redirect_field_name=None)
def MuridAdminView(request):
    qs = AnggotaKelas.objects.order_by('kelas', 'murid__nama_lengkap')
    filter_qs = MuridAdminFilter(request.GET, queryset=qs)

    context = {
        'qs': qs,
        'filter_qs': filter_qs,
    }
    return render(
        request,
        'account_app/admin/murid_list.html',
        context)


@user_passes_test(
    test_func,
    login_url='/denied-access/',
    redirect_field_name=None)
def SortNamaMuridAdminView(request):
    qs = AnggotaKelas.objects.order_by('murid__nama_lengkap')
    filter_qs = MuridAdminFilter(request.GET, queryset=qs)

    context = {
        'qs': qs,
        'filter_qs': filter_qs,
    }
    return render(
        request,
        'account_app/admin/sort/sortnama_murid_list.html',
        context)


class MuridAdminDetailView(UserPassesTestMixin, DetailView):
    model = AnggotaKelas
    template_name = 'account_app/admin/murid_detail.html'

    def test_func(self):
        return self.request.user.groups.filter(name="admin").exists()

    def handle_no_permission(self):
        return redirect('denied-access')


# ALL MAPEL VIEW ------------------------------
class MapelAdminView(UserPassesTestMixin, ListView):
    model = Mapel
    template_name = 'account_app/admin/mapel_list.html'

    def test_func(self):
        return self.request.user.groups.filter(name="admin").exists()

    def handle_no_permission(self):
        return redirect('denied-access')


class MapelAdminDetailView(UserPassesTestMixin, DetailView):
    model = Mapel
    template_name = 'account_app/admin/mapel_detail.html'

    def test_func(self):
        return self.request.user.groups.filter(name="admin").exists()

    def handle_no_permission(self):
        return redirect('denied-access')


# ALL GURU VIEW ------------------------------
@user_passes_test(
    test_func,
    login_url='/denied-access/',
    redirect_field_name=None)
def GuruAdminView(request):
    qs = TimMapel.objects.order_by('mapel', 'guru__nama_lengkap')
    filter_qs = GuruAdminFilter(request.GET, queryset=qs)

    context = {
        'qs': qs,
        'filter_qs': filter_qs,
    }
    return render(
        request,
        'account_app/admin/guru_list.html',
        context)


@user_passes_test(
    test_func,
    login_url='/denied-access/',
    redirect_field_name=None)
def SortNamaGuruAdminView(request):
    qs = TimMapel.objects.order_by('guru__nama_lengkap')
    filter_qs = GuruAdminFilter(request.GET, queryset=qs)

    context = {
        'qs': qs,
        'filter_qs': filter_qs,
    }
    return render(
        request,
        'account_app/admin/sort/sortnama_guru_list.html',
        context)


class GuruAdminDetailView(UserPassesTestMixin, DetailView):
    model = TimMapel
    template_name = 'account_app/admin/guru_detail.html'

    def test_func(self):
        return self.request.user.groups.filter(name="admin").exists()

    def handle_no_permission(self):
        return redirect('denied-access')


# ALL KURIKULUM VIEW ------------------------------
class KurikulumAdminDetailView(UserPassesTestMixin, DetailView):
    template_name = 'account_app/admin/kurikulum.html'
    model = Kurikulum

    def test_func(self):
        return self.request.user.groups.filter(name="admin").exists()

    def handle_no_permission(self):
        return redirect('denied-access')


# ALL LOG MENGAJAR VIEW ------------------------------
class LogMengajarAdminDetailView(UserPassesTestMixin, DetailView):
    template_name = 'account_app/admin/logmengajar.html'
    model = LogMengajar

    def test_func(self):
        return self.request.user.groups.filter(name="admin").exists()

    def handle_no_permission(self):
        return redirect('denied-access')


# ############################## END-ADMIN VIEWS ##############################


# ############################## GURU VIEWS ##############################
class HomeGuruView(UserPassesTestMixin, TemplateView):
    template_name = 'account_app/guru/home.html'

    def test_func(self):
        return self.request.user.groups.filter(name="guru").exists()

    def handle_no_permission(self):
        return redirect('denied-access')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['log_list'] = LogMengajar.objects.filter(
            guru=self.request.user.id)[:5]
        context['pengumuman_list'] = Pengumuman.objects.filter(
            kategori__exact='Guru')[:5]
        return context


# ALL KELAS VIEW ------------------------------
class KelasGuruView(UserPassesTestMixin, ListView):
    model = Kelas
    template_name = 'account_app/guru/kelas_list.html'

    def test_func(self):
        return self.request.user.groups.filter(name="guru").exists()

    def handle_no_permission(self):
        return redirect('denied-access')


class KelasGuruDetailView(UserPassesTestMixin, DetailView):
    model = Kelas
    template_name = 'account_app/guru/kelas_detail.html'

    def test_func(self):
        return self.request.user.groups.filter(name="guru").exists()

    def handle_no_permission(self):
        return redirect('denied-access')


# ALL MURID VIEW ------------------------------
class MuridGuruDetailView(UserPassesTestMixin, DetailView):
    model = AnggotaKelas
    template_name = 'account_app/guru/murid_detail.html'

    def test_func(self):
        return self.request.user.groups.filter(name="guru").exists()

    def handle_no_permission(self):
        return redirect('denied-access')


# ALL MAPEL VIEW ------------------------------
class MapelGuruView(UserPassesTestMixin, ListView):
    template_name = 'account_app/guru/mapel_list.html'

    def get_queryset(self):
        return TimMapel.objects.filter(guru=self.request.user.id)

    def test_func(self):
        return self.request.user.groups.filter(name="guru").exists()

    def handle_no_permission(self):
        return redirect('denied-access')


class MapelGuruDetailView(UserPassesTestMixin, DetailView):
    model = Mapel
    template_name = 'account_app/guru/mapel_detail.html'

    def test_func(self):
        return self.request.user.groups.filter(name="guru").exists()

    def handle_no_permission(self):
        return redirect('denied-access')


# ALL KURIKULUM VIEW ------------------------------
class KurikulumGuruDetailView(UserPassesTestMixin, DetailView):
    template_name = 'account_app/guru/kurikulum.html'
    model = Kurikulum

    def test_func(self):
        return self.request.user.groups.filter(name="guru").exists()

    def handle_no_permission(self):
        return redirect('denied-access')


class KurikulumGuruCreateView(UserPassesTestMixin, CreateView):
    form_class = KurikulumForm
    success_url = reverse_lazy('account-app:mapel-guru')
    template_name = 'account_app/guru/kurikulum_form.html'

    def test_func(self):
        return self.request.user.groups.filter(name="guru").exists()

    def handle_no_permission(self):
        return redirect('denied-access')


# ALL LOG MENGAJAR VIEW ------------------------------
class LogMengajarGuruDetailView(UserPassesTestMixin, DetailView):
    template_name = 'account_app/guru/logmengajar.html'
    model = LogMengajar

    def test_func(self):
        return self.request.user.groups.filter(name="guru").exists()

    def handle_no_permission(self):
        return redirect('denied-access')


class LogMengajarGuruCreateView(UserPassesTestMixin, CreateView):
    form_class = LogMengajarForm
    success_url = reverse_lazy('account-app:kelas-guru')
    template_name = 'account_app/guru/logmengajar_form.html'

    def test_func(self):
        return self.request.user.groups.filter(name="guru").exists()

    def handle_no_permission(self):
        return redirect('denied-access')


# ############################## END-GURU VIEWS ##############################


# ############################## MURID VIEWS ##############################
class HomeMuridView(UserPassesTestMixin, TemplateView):
    template_name = 'account_app/murid/home.html'

    def test_func(self):
        return self.request.user.groups.filter(name="murid").exists()

    def handle_no_permission(self):
        return redirect('denied-access')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tagihan_list'] = TagihanMurid.objects.filter(
            tertagih__murid=self.request.user.id).exclude(status_bayar=True)
        context['pengumuman_list'] = Pengumuman.objects.filter(
            kategori__exact='Murid')[:5]
        context['nilai_list'] = NilaiMurid.objects.filter(
            peserta_tes__murid=self.request.user.id)[:5]
        return context


# # ALL MAPEL VIEW ------------------------------
class MapelMuridView(UserPassesTestMixin, ListView):
    model = Mapel
    template_name = 'account_app/murid/mapel_list.html'

    def test_func(self):
        return self.request.user.groups.filter(name="murid").exists()

    def handle_no_permission(self):
        return redirect('denied-access')


class MapelMuridDetailView(UserPassesTestMixin, DetailView):
    model = Mapel
    template_name = 'account_app/murid/mapel_detail.html'

    def test_func(self):
        return self.request.user.groups.filter(name="murid").exists()

    def handle_no_permission(self):
        return redirect('denied-access')


# ALL KURIKULUM VIEW ------------------------------
class KurikulumMuridDetailView(UserPassesTestMixin, DetailView):
    template_name = 'account_app/murid/kurikulum.html'
    model = Kurikulum

    def test_func(self):
        return self.request.user.groups.filter(name="murid").exists()

    def handle_no_permission(self):
        return redirect('denied-access')


# ############################## END-MURID VIEWS ##############################
