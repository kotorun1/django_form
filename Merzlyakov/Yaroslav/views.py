from django.shortcuts import render
from .forms import AdressForm

def index(request):
    return render(request,'Yaroslav\index.html')
def adress_form(request):
    adress_form = AdressForm()
    return render(request, 'Yaroslav\\adress_form.html',{'form':adress_form})
def adress_result(request):
    if request.method =='POST':
        name =  request.POST.get('name', 'quest')
        surname =  request.POST.get('surname','None')
        side =   request.POST.get('side','Russia')
        region =   request.POST.get('region','Moscow region')
        city =  request.POST.get('city','Moscow')
        street =   request.POST.get('street','Center')
        house = request.POST.get('house','1')
        data = {'name':name,'surname':surname,'side':side,'region':region,
        'city':city,'street':street,'house':house}
        return render(request, 'Yaroslav\\address_result.html', {'data':data})
    else:
        adress_form = AdressForm()
        return render(request, 'Yaroslav\\adress_form.html',{'form':adress_form})

def appointment(request):
    if request.method =='POST':
        name =  request.POST.get('form__name')
        email =  request.POST.get('email')
        phone =   request.POST.get('phone')
        service =   request.POST.get('service')
        about =  request.POST.get('about')
        data = {'name':name,'email':email,'phone':phone,'service':service,
        'about':about}
        return render(request, 'Yaroslav\\appointment.html', {'data':data})
    else:
        adress_form = AdressForm()
        return render(request,'Yaroslav\index.html')
