from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("<h1>:D</h1>")

def cuestionario(request, id):
    preguntas = ["Como te llamas?", "Edad"]
    pagina = """
    <html>
    <body>
    <h1>:Pregunta %s </h1>
    </body>
    </html>
            """ % preguntas[id -1]
    return HttpResponse(pagina)

def a(request):
    return render(request,"home.html")