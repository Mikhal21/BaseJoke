from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import render, redirect

from django import forms

jokes = {
    '1': {
        'id': 1,
        'text': 'Why did the tomato turn red? Because it saw the salad dressing!',
        'author': 'Anna'
    }
}

# Form for entering a joke
class JokeForm(forms.Form):
    joke = forms.CharField(label='Joke', max_length=120, widget=forms.TextInput(attrs={'class': 'form-control'}))
    author = forms.CharField(label='Author', max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))


# index page displaying all entries
def index(request):
    rendered = render(request, 'app/index.html', {'jokes': jokes.values()})
    highlight = request.GET.get('highlight')
    try:
        highlight = int(highlight)
    except: 
        highlight = None
    
    return render(request, 'app/index.html', {
        'jokes': jokes.values(),
        'highlight': highlight
    })

# page for adding new entries
def add(request):
    global id

    if request.method == 'POST':
        form = JokeForm(request.POST)
        if form.is_valid():
            id = len(jokes) + 1
            jokes[id] = {
                'id': id,
                'text': form.cleaned_data['joke'],
                'author': form.cleaned_data['author']
            }
            
            # add GET request parameter to highlight correct joke
            response = redirect('app:index')
            response['Location'] += f'?highlight={id}'
            return response
    else:
        form = JokeForm()

    return render(request, 'app/add.html', { 'form': form })

# get JSON version of an entry
def get_user_entry(request, id):
    entry = jokes.get(id)
    if entry is None:
        return JsonResponse({'error': 'Entry does not exist'}, status=404)
    else:
        return JsonResponse(entry)