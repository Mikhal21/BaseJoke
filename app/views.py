from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Quote, Person
from django.http import HttpResponseRedirect


from django import forms

quotes = {
    '1': {
        'id': 1,
        'text': 'I have learne that there is no failure in running or in life as long as you keep moving',
        'author': 'Amby Burfoot'
    }
}

# Form for entering a quote
class QuoteForm(forms.Form):
    quote = forms.CharField(label='Quote', max_length=120, widget=forms.TextInput(attrs={'class': 'form-control'}))
    author = forms.ModelChoiceField(queryset=Person.objects.all())


# index page displaying all entries
def index(request):
    # rendered = render(request, 'app/index.html', {'quotes': quotes.values()})
    # highlight = request.GET.get('highlight')
    # try:
    #     highlight = int(highlight)
    # except: 
    #     highlight = None
    
    # return render(request, 'app/index.html', {
    #     'quotes': quotes.values(),
    #     'highlight': highlight
    # })
    
    quotes = Quote.objects.all()
    return render(request, 'app/index.html', {'quotes': quotes})

# page for adding new entries


def add(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            author = form.cleaned_data['author']
            quote_content = form.cleaned_data['quote']
            quote = Quote(text=quote_content, author=author)  # update here
            quote.save()
            return HttpResponseRedirect('/')
    else:
        form = QuoteForm()
    return render(request, 'app/add.html', {'form': form})





# get JSON version of an entry
def get_user_entry(request, id):
    entry = quotes.get(id)
    if entry is None:
        return JsonResponse({'error': 'Entry does not exist'}, status=404)
    else:
        return JsonResponse(entry)