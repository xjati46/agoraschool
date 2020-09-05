from django.db import models
from django.contrib.auth.models import AbstractUser
from django_quill.fields import QuillField

# Create your models here.


class CustomUser(AbstractUser):
    PILIHAN_JENIS_KELAMIN = models.TextChoices(
        'Jenis Kelamin',
        'Laki-laki Perempuan',)

    nama_lengkap = models.CharField(max_length=200, blank=True, null=True)
    nama_panggilan = models.CharField(max_length=50, blank=True, null=True)
    jenis_kelamin = models.CharField(
        max_length=10, choices=PILIHAN_JENIS_KELAMIN.choices,
        blank=True, null=True)
    jenis_id = models.CharField(max_length=100, blank=True, null=True)
    nomor_id = models.CharField(max_length=100, blank=True, null=True)
    tempat_lahir = models.CharField(max_length=100, blank=True, null=True)
    tanggal_lahir = models.DateField(blank=True, null=True)
    alamat_tinggal = models.CharField(max_length=300, blank=True, null=True)
    nomor_ponsel = models.CharField(max_length=50, blank=True, null=True)

    def clean(self):
        try:
            self.nama_lengkap = self.nama_lengkap.capitalize()
        except:
            self.nama_lengkap = self.nama_lengkap


class Kelas(models.Model):
    tingkat = models.IntegerField()
    nama = models.CharField(max_length=20,)
    anggota_kelas = models.ManyToManyField(
        CustomUser, through='AnggotaKelas',)
    guru_pembina = models.ForeignKey(
        'TimMapel', on_delete=models.SET_NULL,
        null=True, blank=True, related_name='guru_pembina')
    ketua_murid = models.ForeignKey(
        'AnggotaKelas', on_delete=models.SET_NULL,
        null=True, blank=True, related_name='ketua_murid')

    def __str__(self):
        return f'{self.tingkat} ({self.nama})'

    class Meta:
        ordering = ['tingkat']
        verbose_name_plural = 'Kelas'


class AnggotaKelas(models.Model):
    murid = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,)
    kelas = models.ForeignKey(
        Kelas,
        on_delete=models.CASCADE,)
    tanggal_gabung = models.DateField()

    def __str__(self):
        return f'{self.murid} | {self.kelas}'

    class Meta:
        ordering = ['kelas', 'murid__nama_lengkap']
        verbose_name_plural = 'Murid'


class Mapel(models.Model):
    nama = models.CharField(max_length=20,)
    tim_mapel = models.ManyToManyField(
        CustomUser,
        through='TimMapel',)

    def __str__(self):
        return self.nama

    class Meta:
        ordering = ['nama']
        verbose_name_plural = 'Mata Pelajaran'


class TimMapel(models.Model):
    guru = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,)
    mapel = models.ForeignKey(
        Mapel,
        on_delete=models.CASCADE,)
    tanggal_gabung = models.DateField()

    def __str__(self):
        return f'{self.guru} | {self.mapel}'

    class Meta:
        ordering = ['mapel']
        verbose_name_plural = 'Guru'


class Kurikulum(models.Model):
    guru = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,)
    mapel = models.ForeignKey(
        Mapel,
        on_delete=models.CASCADE,)
    tingkat_pengajaran = models.CharField(max_length=200)
    deskripsi = QuillField()
    tanggal_buat = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.mapel} | {self.tingkat_pengajaran}'

    class Meta:
        ordering = ['mapel']
        verbose_name_plural = 'Kurikulum'


class LogMengajar(models.Model):
    guru = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,)
    kelas = models.ForeignKey(
        Kelas,
        on_delete=models.CASCADE,)
    kurikulum = models.ForeignKey(
        Kurikulum,
        on_delete=models.CASCADE,)
    tanggal_buat = models.DateTimeField()
    deskripsi = QuillField()

    def __str__(self):
        return f'{self.guru} | {self.tanggal_buat}'

    class Meta:
        ordering = ['-tanggal_buat']
        verbose_name_plural = 'Log Mengajar'
