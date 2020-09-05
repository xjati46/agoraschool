import django_filters
from account_app.models import AnggotaKelas, TimMapel


class MuridAdminFilter(django_filters.FilterSet):
    murid__nama_lengkap = django_filters.CharFilter(
        field_name='murid__nama_lengkap',
        lookup_expr='icontains',
        label='Nama Lengkap')

    class Meta:
        model = AnggotaKelas
        fields = ['murid__nama_lengkap', 'kelas']


class GuruAdminFilter(django_filters.FilterSet):
    guru__nama_lengkap = django_filters.CharFilter(
        field_name='guru__nama_lengkap',
        lookup_expr='icontains',
        label='Nama Lengkap')

    class Meta:
        model = TimMapel
        fields = ['guru__nama_lengkap', 'mapel']
