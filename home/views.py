from django.shortcuts import render

# Create your views here.

def homepage(request):
    contexto ={'nombre': "Alfreo Huante Tellez",
            'lugar': "Laboratorio Estatal de Salud Pública"
               }
    return render(request, 'index.html', contexto)