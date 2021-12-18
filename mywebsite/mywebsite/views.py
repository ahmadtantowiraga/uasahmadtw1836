
from django.shortcuts import render
from.import sintak

def index(request):
    return render(request,'index.html')

def enkripsi(request):
    context={
        'judul':'ENKRIPSI',
        'hasil':'Hasil Enkripsi',
    }
    if request.method=='POST':
        print('ini method post')
        context['teks']=request.POST['teks']
        context['kunci'] = request.POST['kunci']
        c=request.POST['teks']
        ku=request.POST['kunci']
        e=sintak.enkrip2(c,ku)
        context['e'] = e
    else:
        print('ini method get')
    return render(request,'enkripsi.html',context)

def deskripsi(request):
    context={
        'judul':'DESKRIPSI',
        'hasil':'Hasil Deskripsi',
    }
    if request.method=='POST':
        print('ini method post')
        context['teks']=request.POST['teks']
        context['kunci'] = request.POST['kunci']
        t=request.POST['teks']
        k=request.POST['kunci']
        c = sintak.deskrip(t, k)
        context['e'] = c
    else:
        print('ini method get')
    return render(request,'deskripsi.html',context)