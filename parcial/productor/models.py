from django.db import models
import datetime
# Create your models here.
class Productor(models.Model):
    productorid = models.AutoField(primary_key=True)
    cedula = models.CharField(max_length=20)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.IntegerField()
    correo = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Finca(models.Model):
    fincaid = models.AutoField(primary_key=True)
    numeroCastro = models.IntegerField()
    municipio = models.CharField(max_length=50)
    productor = models.ForeignKey(Productor, on_delete=models.CASCADE)

class Tipocultivo(models.Model):
    tipocultivoid = models.AutoField(primary_key=True)
    nombreTipoCultivo = models.CharField(max_length=50)

class Vivero(models.Model):
    viveroid = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=30,unique=True)
    tipocultivo = models.ForeignKey(Tipocultivo,on_delete=models.DO_NOTHING)

class Labor(models.Model):
    laborid = models.AutoField(primary_key=True)
    fecha = models.DateTimeField()
    descripcion = models.TextField(max_length=200)
    vivero = models.ForeignKey(Vivero,on_delete=models.DO_NOTHING)

class ProductoControl(models.Model):
    productocontrolid = models.AutoField(primary_key=True)
    registroICA = models.CharField(max_length=30,unique=True)
    nombreproducto = models.CharField(max_length=50)
    frecuenciaDias = models.IntegerField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    labor = models.ForeignKey(Labor,on_delete=models.DO_NOTHING)

class ControlHongo(models.Model):
    controlhongoid = models.AutoField(primary_key=True)
    diasPeriodoCarencia =models.IntegerField()
    nombre = models.CharField(max_length=50)
    productocontrol = models.ForeignKey(ProductoControl,on_delete=models.DO_NOTHING)

class ControlPlaga(models.Model):
    controlplagaid = models.AutoField(primary_key=True)
    diasPeriodoCarencia =models.IntegerField()
    productocontrol = models.ForeignKey(ProductoControl,on_delete=models.DO_NOTHING)

class ControlFertilizantes(models.Model):
    controlfertilizantesid = models.AutoField(primary_key=True)
    fechaUltimaAplicacion = models.DateTimeField()
    productocontrol = models.ForeignKey(ProductoControl,on_delete=models.DO_NOTHING)



