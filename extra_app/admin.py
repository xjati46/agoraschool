from django.contrib import admin
from extra_app.models import Pengumuman, NilaiMurid, LaporanMurid, TagihanMurid

# Register your models here.


@admin.register(Pengumuman)
class PengumumanAdmin(admin.ModelAdmin):
    pass


@admin.register(NilaiMurid)
class NilaiMuridAdmin(admin.ModelAdmin):
    pass


@admin.register(LaporanMurid)
class LaporanMuridAdmin(admin.ModelAdmin):
    pass


@admin.register(TagihanMurid)
class TagihanMuridAdmin(admin.ModelAdmin):
    pass
