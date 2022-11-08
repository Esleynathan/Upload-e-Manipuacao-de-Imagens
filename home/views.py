from django.shortcuts import render
from django.http import HttpResponse
from PIL import Image
import os
from django.conf import settings
from datetime import date
from .models import MyFile

# Create your views here.
def home(request):
    if request.method == "GET":
        return render(request, "home.html")
    elif request.method =="POST":
        file = request.FILES.get("my_file")
            
        for b in file.chunks():
            print(b)
        
        ## DEFININDO TAMANHO DA IMAGEM.
        ##if file.size > 200000000:
        ##    return HttpResponse('Arquivo muito grande.')
        
        mf = MyFile(title="minha_imagem" , arq=file)
        mf.save()
        
        ## OUTRA ALTERNATIVA PARA SALVAR.
        ##img = Image.open(file)
        ##path = os.path.join(settings.BASE_DIR, f'media/{file.name}-{date.today()}.jpg')
        ##img = img.save(path)
        
        print (file)    

        return HttpResponse('teste')