from django.contrib import admin
from account_app.models import (
                                CustomUser, Kelas, AnggotaKelas,
                                Mapel, TimMapel, Kurikulum, LogMengajar
                                )

# Register your models here.


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):

    def group(self, user):
        groups = []
        for group in user.groups.all():
            groups.append(group.name)
        return ', '.join(groups)

    group.short_description = 'Grup'

    list_display = ('__str__', 'id', 'group')
    fieldsets = (
        (None, {
            'fields': ['username']
        }),
        ('Informasi Pribadi', {
            'fields': (
                'nama_lengkap',
                ('nama_panggilan', 'jenis_kelamin'),
                ('jenis_id', 'nomor_id'),
                ('tempat_lahir', 'tanggal_lahir'),
                )
        }),
        ('Kontak', {
            'fields': (
                'alamat_tinggal', 'nomor_ponsel', 'email',
                )
        }),
        ('Akses', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions'
                )
        }),
        ('Lain-lain', {
            'fields': ('last_login', 'date_joined')
        }),
    )
    readonly_fields = ['username']


@admin.register(Kelas)
class KelasAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'id')


@admin.register(AnggotaKelas)
class AnggotaKelasAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'id')


@admin.register(Mapel)
class MapelAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'id')


@admin.register(TimMapel)
class TimMapelAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'id')


@admin.register(Kurikulum)
class KurikulumAdmin(admin.ModelAdmin):
    pass


@admin.register(LogMengajar)
class LogMengajarAdmin(admin.ModelAdmin):
    pass
