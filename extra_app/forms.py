from django import forms
from extra_app.models import Pengumuman, NilaiMurid, LaporanMurid, TagihanMurid
from tempus_dominus.widgets import DateTimePicker


class PengumumanForm(forms.ModelForm):
    class Meta:
        model = Pengumuman
        fields = '__all__'


class NilaiMuridForm(forms.ModelForm):
    waktu = forms.DateTimeField(widget=DateTimePicker())

    class Meta:
        model = NilaiMurid
        fields = '__all__'


class LaporanMuridForm(forms.ModelForm):
    waktu = forms.DateTimeField(widget=DateTimePicker())

    class Meta:
        model = LaporanMurid
        fields = '__all__'


class TagihanMuridForm(forms.ModelForm):
    waktu_bayar = forms.DateTimeField(widget=DateTimePicker(), required=False)

    class Meta:
        model = TagihanMurid
        fields = '__all__'
