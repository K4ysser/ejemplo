from django.http import *
from django.template import Template, Context, loader

# Request -> Todas las peticiones que hace un usuario desde el navegador
# HTTPResponse -> Todas las respuestas mediante protocolo HTTP

def inicio(request):
    return HttpResponse("Prueba de lenvatamiento con DJango.")

def estudiante(request):
    template = loader.get_template('estudiante.html')
    document = template.render()
    return HttpResponse(document)

def curso(request) :
     template = loader.get_template('curso.html')
     document = template.render()
     return HttpResponse(document)

def saludo(request, nombre, edad) :
    return HttpResponse(f"Elaborado por {nombre} y tengo la edad de {edad} ")

def saludo2(request, nombre, edad):
    if str(edad).isnumeric():
        cadena = f"Me llamo {nombre} y tengo {edad} años, mucho gustoo..."
    else: 
        cadena = "El parametro edad no es un numero válido."
    return HttpResponse(cadena)

def saludo3(request, nombre) :
   cadena = f"Me llamo {nombre} ,mucho gusto..."
   return HttpResponse(cadena)

def html(request):
    ## CODIGO HTML
    #cadena = """
    #        <ul>
    #            <li>platano</li>
    #            <li>fresa</li>
    #            <li>pera</li>
    #        </ul>
    #        """       
    ## EQUIVALENTE AL CODIGO ARRIBA
    frutas = ['platano','fresa','pera']
    cadena = ''
    for data in frutas :
        cadena += f'<li>{data}</li>'
    cadena=f"<ul>{cadena}</ul>"
    return HttpResponse(cadena)

def html2(request) :
    titulo = "Prueba pagina con DJango"
    alumnos = ['Lionel Messi','Marco Reus','Florian Wirtz','Jamal Musiala']
    alumno_curso = [
        {'nombre': 'Lionel Messi','Equipo':'Barcelona , Argentina','dorsal':'10'},
        {'nombre': 'Marco Reus','Equipo':'Borussia Dortmund , Alemania','dorsal':'11'},
        {'nombre': 'Florian Wirtz','Equipo':'Bayer Leverkusen , Alemania','dorsal':'11'},
        {'nombre': 'Jamal Musiala','Equipo':'Bayer Munich , Inglaterra','dorsal':'11'}
    ]
    context = {
        'list_alumnos' : alumnos,
        'titulo' : titulo, 
        'list_alumnocurso' : alumno_curso,
    }   
    #Para cargar una plantilla en Django
    template = loader.get_template('plantilla.html')
    #Renderizar la plantilla con valores
    document = template.render(context)
    return HttpResponse(document)


