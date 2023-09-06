import json
from django.http import JsonResponse
from django.shortcuts import render,HttpResponse
from productor.models import Productor
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def crearproductor(request,idproductor=''):

    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8')) 

        productortemp = Productor(
            cedula = data.get('cedula'),
            nombre = data.get('nombre'),
            apellido = data.get('apellido'),
            telefono = data.get('telefono'),
            correo = data.get('correo')
        )

        productortemp.save()
        idregistro = productortemp.productorid

        msg = {
            "mesaje":{
                "data":{
                    "productorid":idregistro
                }
            },
            "error":""
        }
        return JsonResponse(msg, status=200)
    elif request.method == 'GET':

        arryresponse = []

        todosproductores = Productor.objects.all()

        for productortemp in todosproductores:
            jsontemp = {
                "productorid":productortemp.productorid,
                "cedula":productortemp.cedula,
                "nombre":productortemp.nombre,
                "apellido":productortemp.apellido,
                "telefono":productortemp.telefono,
                "correo":productortemp.correo,
                "created_at":productortemp.created_at,
                "updated_at":productortemp.updated_at
            }
            arryresponse.append(jsontemp)

        msgtemp = {
            "mesaje":{
                "data":{
                    "productores":arryresponse
                }
            },
            "error":""
        }

        return JsonResponse(msgtemp, status=200)
    
    elif request.method == 'DELETE':

        if idproductor == '':
            return JsonResponse({'error': "No se incluyó un id de productor para eliminar -> /"+"{productorid}"}, status=400)
        
        try:
            productortemp = Productor.objects.get(productorid=idproductor) 

            productortemp.delete()
            
            return JsonResponse({"mesaje":"eliminación completa"}, status=200)
        
        except Productor.DoesNotExist:
            return JsonResponse({'error': 'El productor no existe'}, status=400)
    else:   
        return JsonResponse({'error': 'Method = POST,GET,PATCH'}, status=400)
    