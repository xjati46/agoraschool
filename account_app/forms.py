from django import forms
from account_app.models import Kurikulum, LogMengajar
from tempus_dominus.widgets import DateTimePicker


class KurikulumForm(forms.ModelForm):
    class Meta:
        model = Kurikulum
        fields = '__all__'


class LogMengajarForm(forms.ModelForm):
    tanggal_buat = forms.DateTimeField(widget=DateTimePicker())

    class Meta:
        model = LogMengajar
        fields = '__all__'
