from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.

class Promovete(models.Model):
    promovente = models.CharField(verbose_name="Nombre o razon social del del Promovente", max_length=200)
    rfc = models.CharField(
        verbose_name="Registro Federal de Contribuyentes",
        max_length=13,
        null=True,
        blank=True)
    representante = models.CharField(
        verbose_name="Representante Legal", max_length=200, null = True, blank = True)

    class Meta:
        verbose_name = "Promovente"
        verbose_name_plural = "Promoventes"
        ordering = ['-pk']

    def __str__(self):
        return self.promovente

class Cliente(models.Model):
    cliente = models.CharField(
        verbose_name="Nombre o razon social del Cliente", max_length=200)
    rfc = models.CharField(
        verbose_name="Registro Federal de Contribuyentes",
        max_length=13,
        null=True,
        blank=True)
    ubicacion = models.CharField(
        verbose_name="Ubicación del cliente", max_length=200)
    promovente = models.ForeignKey(
        Promovete, on_delete=models.PROTECT, verbose_name="Promovente")

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ['-pk']

    def __str__(self):
        return self.cliente


class TipoServicios(models.Model):
    nombre = models.CharField(
        verbose_name="Nombre del Tipo de servicio", max_length=200)
    desc = RichTextField(
        verbose_name="Descripcion del servicio", max_length=500)

    class Meta:
        verbose_name = "Tipo de Servicio"
        verbose_name_plural = "Tipos de Servicios"
        ordering = ['-pk']

    def __str__(self):
        return self.nombre


class Servicios(models.Model):
    nombre = models.CharField(verbose_name="Nombre del Servicio", max_length=200)
    fecha_de_inicio = models.DateField(verbose_name="Fecha de inicio")
    fecha_de_entrega = models.DateField(verbose_name="Fecha de entrega")
    tipo_de_servicio = models.ForeignKey(TipoServicios, on_delete=models.PROTECT, verbose_name="Tipo de Servicio")
    capacidad = models.TextField(verbose_name="Capacidad o descripcion del servicio", max_length=500)
    responsable = models.ForeignKey(
        User, on_delete=models.PROTECT, verbose_name="Responsable del Servicio")

    tarea = RichTextField(verbose_name="Tareas")

    class Meta:
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"
        ordering = ['-pk']

    def __str__(self):
        return self.nombre

class TipoProyecto(models.Model):
    nombre = models.CharField(verbose_name="Nombre del Tipo de Proyecto", max_length=200)
    desc = models.TextField(
        verbose_name="Descripcion del Proyecto", max_length=500)

    class Meta:
        verbose_name = "Tipo de Proyecto"
        verbose_name_plural = "Tipos de Proyectos"
        ordering = ['-pk']

    def __str__(self):
        return self.nombre

class Proyectos(models.Model):
    nombre = models.CharField(verbose_name="Nombre del Proyecto", max_length=200)
    promoventes = models.ForeignKey(Promovete,on_delete=models.PROTECT,verbose_name="Nombre del Promovente")
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.PROTECT,
        verbose_name="Nombre del Cliente",
        null=True,
        blank=True)
    fecha_de_inicio = models.DateField(verbose_name="Fecha de inicio")
    tipo_de_proyecto =  models.ForeignKey(TipoProyecto,on_delete=models.PROTECT)
    auto = models.CharField(
        verbose_name="Autorizacion del proyecto",
        max_length=200,
        null=True,
        blank=True)
    superficie = models.CharField(
        verbose_name="Superficie del proyecto",
        max_length=200,
        null=True,
        blank=True)
    estudios = models.ManyToManyField(Servicios,verbose_name="Estudios")
    responsable = models.ForeignKey(User, on_delete=models.PROTECT)
    descripcion = RichTextField(
        verbose_name="Descripcion del proyecto", null=True, blank=True)

    class Meta:
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"
        ordering = ['-pk']

    def __str__(self):
        return self.nombre
