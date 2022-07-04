from django.shortcuts import redirect, render
from .forms import FormName

# Create your views here.
def index(request):
    return render(request, 'basicapp/index.html')

def form(request):
    form = FormName
    if request.method == 'POST':
        form = FormName(request.POST)
        if form.is_valid():
            print('VALIDATION SUCESS!') 
            print('Name: '+ form.cleaned_data['name'])
            print('email: ' + form.cleaned_data['email'])
            print('messages: ' + form.cleaned_data['Textarea'])
            return redirect('form')
        else:
            return redirect('form')
    else:
        return render(request,'basicapp/form_page.html', {'form':form} )
