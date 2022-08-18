
from django.http import HttpResponse
from datetime import date



def my_age(request, edad:int, nombre:str):

    today = date.today()
    b_date = today.year - edad

    data = """<div align="center" style="border: 1px solid #444; color:#444">
    <h1>Hola """ + nombre + """</h1>
    <h3>Tu año de nacimiento es: """+ str(b_date)+"""</h3>
    </div>
    """
    return HttpResponse(data)