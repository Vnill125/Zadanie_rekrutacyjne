from django import forms
from datetime import datetime


class PeselForm(forms.Form):
    pesel_number = forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'myfieldclass', 'placeholder':'Numer PESEL...'}))

    def is_valid_pesel(self, pesel):
        if len(pesel) > 11:
            return False
        try:
            weights = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3, 1]
            checksum = sum(int(p) * w for p, w in zip(str(pesel), weights)) % 10
            return checksum == 0
        except (ValueError, TypeError):
            return False
        
    def clean_pesel_number(self):
        pesel_number = self.cleaned_data["pesel_number"]

        if not self.is_valid_pesel(pesel_number):
            raise forms.ValidationError("Nieprawidłowy numer PESEL.")

        return pesel_number

    def get_birth_date_and_gender(self, pesel):
        try:
            year = int(pesel[0:2])
            month = int(pesel[2:4])
            day = int(pesel[4:6])

            if month > 80:
                year += 1800
                month -= 80
            elif month > 60:
                year += 2200
                month -= 60
            elif month > 40:
                year += 2100
                month -= 40
            elif month > 20:
                year += 2000
                month -= 20
            else:
                year += 1900

            gender = "Mężczyzna" if int(pesel[9]) % 2 == 1 else "Kobieta"

            birth_date = datetime(year, month, day).strftime("%Y-%m-%d")

            return birth_date, gender
        except (ValueError, TypeError):
            return None, None
