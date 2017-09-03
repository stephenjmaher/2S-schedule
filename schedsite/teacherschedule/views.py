from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .forms import NameForm
from .writefile import writeCollectedData

# Create your views here.

def index(request):
    return HttpResponse("This is the first reponse from the scheduling project.")

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required

            writeCollectedData(form.cleaned_data)

            # redirect to a new URL:
            return HttpResponseRedirect('./thanks')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})

def thank_you(request):
    return HttpResponse("This is the finish page.")
