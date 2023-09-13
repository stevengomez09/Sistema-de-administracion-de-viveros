import json
from django.http import JsonResponse
from django.shortcuts import render,HttpResponse
from productor.models import Productor,Finca,Vivero,Tipocultivo,Labor, ProductoControl, ControlHongo, ControlPlaga, ControlFertilizantes
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt

def crearproductor(data):  
    excepciones = []
    if data.get("cedula") == "":
        excepciones.append("Campo cedula es obligatorio")
    if data.get("nombre") == "":
        excepciones.append("Campo nombre es obligatorio")
    if data.get("apellido") == "":
        excepciones.append("Campo apellido es obligatorio")
    if data.get("telefono") == "":
        excepciones.append("Campo telefono es obligatorio")
    if data.get("correo") == "":
        excepciones.append("Campo correo es obligatorio")       
    if excepciones.count > 0:
        raise Exception(", ".join(excepciones)) 
    productortemp = Productor(
        cedula = data.get('cedula'),
        nombre = data.get('nombre'),
        apellido = data.get('apellido'),
        telefono = data.get('telefono'),
        correo = data.get('correo')
    )
    productortemp.save()
    return True

def crearproductor2(request,idproductor=''):

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
    

def crearFinca(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8')) 
        fincatemp = Finca(
            numeroCastro = data.get("numeroCastro"),
            municipio = data.get("municipio"),
            productor = Productor.objects.get(productorid=data.get("productorid"))
        )
        fincatemp.save()
        idregistro = fincatemp.fincaid
        msg = {
            "mesaje":{
                "data":{
                    "finca":idregistro
                }
            },
            "error":""
        }
        return JsonResponse({'mesaje':msg}, status=200)
    else:
        return JsonResponse({'mesaje':"GET"}, status=400)


def crearVivero(datatemp): 
        excepciones = []
        if datatemp.get("codigo") == "":
            excepciones.append("Campo codigo es obligatorio")
        if datatemp.get("tipocultivoid") == "":
            excepciones.append("Campo tipocultivoid es obligatorio")
        if excepciones.count > 0:
            raise Exception(", ".join(excepciones))
        viveroparacrear =   Vivero(
            codigo = datatemp.get("codigo"),
            tipocultivoid = Tipocultivo.objects.get(tipocultivoid=datatemp.get("tipocultivoid"))
        )
        viveroparacrear.save()
        return True

def crearLabor(datatemp):
    excepciones = []
    if datatemp.get("fecha") == "":
        excepciones.append("Campo fecha es obligatorio")
    if datatemp.get("descripcion") == "":
        excepciones.append("Campo descripcion es obligatorio")
    if datatemp.get("viveroid") == "":
        excepciones.append("Campo viveroid es obligatorio")
    if excepciones.count > 0:
            raise Exception(", ".join(excepciones))
    laborparacrear = Labor(
        fecha = datatemp.get("fecha"),
        descripcion = datatemp.get("descripcion"),
        viveroid = Vivero.objects.get(viveroid=datatemp.get("viveroid"))
    )
    laborparacrear.save()
    return True

def crearControlHongo(datatemp):
    excepciones = []
    if datatemp.get("diasPeriodoCarencia") == "":
        excepciones.append("Campo Dias Periodo Carencia es obligatorio")
    if datatemp.get("nombre") == "":
        excepciones.append("Campo Nombre es obligatorio")
    if datatemp.get("productocontrol") == "":
        excepciones.append("Campo Producto control es obligatorio")
    if excepciones.count > 0:
            raise Exception(", ".join(excepciones))
    controlHongoparacrear = ControlHongo(
        controlhongoid = datatemp.get("controlhongoid"),
        diasPeriodoCarencia = datatemp.get("diasPeriodoCarencia"),
        nombre = datatemp.get("nombre"),
        productocontrol = ProductoControl.objects.get(productocontrol=datatemp.get("productocontrol"))
    )
    controlHongoparacrear.save()
    return True


def crearControlPlaga(datatemp):
    excepciones = []
    if datatemp.get("diasPeriodoCarencia") == "":
        excepciones.append("Campo Dias Periodo Carencia es obligatorio")
    if datatemp.get("productocontrol") == "":
        excepciones.append("Campo Producto control es obligatorio")
    if excepciones.count > 0:
            raise Exception(", ".join(excepciones))
    controlPlagaparacrear = ControlHongo(
        controlplagaid = datatemp.get("controlhongoid"),
        diasPeriodoCarencia = datatemp.get("diasPeriodoCarencia"),
        productocontrol = ProductoControl.objects.get(productocontrol=datatemp.get("productocontrol"))
    )
    controlPlagaparacrear.save()
    return True

def crearControlFertilizantes(datatemp):
    excepciones = []
    if datatemp.get("fechaUltimaAplicacion") == "":
        excepciones.append("Campo Fecha Ultima Aplicación es obligatorio")
    if datatemp.get("productocontrol") == "":
        excepciones.append("Campo Producto control es obligatorio")
    if excepciones.count > 0:
            raise Exception(", ".join(excepciones))
    controlFertilizantesparacrear = ControlHongo(
        controlfertilizantesid = datatemp.get("controlfertilizantesid"),
        fechaUltimaAplicacion = datatemp.get("fechaUltimaAplicacion"),
        productocontrol = ProductoControl.objects.get(productocontrol=datatemp.get("productocontrol"))
    )
    controlFertilizantesparacrear.save()
    return True
