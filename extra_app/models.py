from django.db import models
from account_app.models import AnggotaKelas, TimMapel, Mapel, CustomUser
from django_quill.fields import QuillField

# Create your models here.


class Pengumuman(models.Model):
    PILIHAN_KATEGORI = models.TextChoices(
        'Kategori',
        'Guru Murid',)

    judul = models.CharField(max_length=100,)
    konten = QuillField()
    kategori = models.CharField(
        max_length=10, choices=PILIHAN_KATEGORI.choices,)
    waktu_post = models.DateTimeField(auto_now_add=True,)

    def __str__(self):
        return self.judul

    class Meta:
        ordering = ['-waktu_post']
        verbose_name_plural = 'Pengumuman'


class NilaiMurid(models.Model):
    peserta_tes = models.ForeignKey(
        AnggotaKelas, on_delete=models.CASCADE, verbose_name="Peserta Tes")
    mapel_tes = models.ForeignKey(
        Mapel, on_delete=models.CASCADE, verbose_name="Mata Pelajaran")
    pembuat_tes = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, verbose_name="Penilai")
    waktu = models.DateTimeField()
    deskripsi = models.CharField(max_length=300)
    nilai = models.FloatField()

    def __str__(self):
        return f'{self.peserta_tes}, {self.mapel_tes}, {self.nilai}'

    class Meta:
        ordering = ['mapel_tes']
        verbose_name_plural = 'Nilai Murid'


class LaporanMurid(models.Model):
    terlapor = models.ForeignKey(
        AnggotaKelas, on_delete=models.CASCADE, verbose_name="Murid")
    pelapor = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, verbose_name="Guru")
    waktu = models.DateTimeField()
    konten = QuillField()

    def __str__(self):
        return f'{self.terlapor}, {self.pelapor}, {self.waktu}'

    class Meta:
        ordering = ['-waktu']
        verbose_name_plural = 'Laporan Murid'


class TagihanMurid(models.Model):
    judul = models.CharField(max_length=200)
    tertagih = models.ForeignKey(
        AnggotaKelas, on_delete=models.CASCADE, verbose_name="Murid")
    nilai = models.IntegerField()
    status_bayar = models.BooleanField(null=True, blank=True)
    waktu_bayar = models.DateTimeField(null=True, blank=True)
    keterangan = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return f'{self.judul}, {self.tertagih}, {self.status_bayar}'

    class Meta:
        ordering = ['status_bayar']
        verbose_name_plural = 'Tagihan Murid'
