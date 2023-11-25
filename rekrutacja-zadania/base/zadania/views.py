from django.shortcuts import render
import random

from .forms import PeselForm
# # Create your views here.

def home(request):
    return render(request, 'index.html')


def shuffle(text):
    file = text.split()
    shuffled_file = [word[0] + ''.join(random.sample(word[1:-1], len(word)-2)) + word[-1] if len(word) > 2 else word for word in file]
    return ' '.join(shuffled_file)

def task1(request):
    if request.method == 'POST' and request.FILES['file']:
        file = request.FILES['file']
        content = file.read().decode('utf-8')
        shuffled_file = shuffle(content)
        return render(request, 'task1.html', {'file': content, 'shuffled_file': shuffled_file})
    return render(request, 'task1.html', {'page':'file'})

def task2(request):
    birth_date = None
    gender = None

    if request.method == 'POST':
        form = PeselForm(request.POST)
        if form.is_valid():
            pesel_number = form.cleaned_data['pesel_number']
            birth_date, gender = form.get_birth_date_and_gender(pesel_number)
            return render(request,'task2.html', {'pesel_number': pesel_number, 'birth_date': birth_date, 'gender': gender})
    else:
        form = PeselForm()

    return render(request, 'task2.html', {'form': form, 'birth_date': birth_date, 'gender': gender, 'page': 'pesel'})