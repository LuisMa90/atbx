from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from proyecto.models import Proyectos, Servicios, TipoProyecto, TipoServicios

# Create your models here.
class Vehiculos(models.Model):
    modelo = models.CharField(verbose_name="Modelo del vehículo", max_length=200)
    marca = models.CharField(verbose_name="Marca del vehículo", max_length=200)

    class Meta:
        verbose_name = "Vehículo"
        verbose_name_plural = "Vehículos"

    def __str__(self):
        return self.modelo



class Actividad(models.Model):
    actividad = models.CharField(verbose_name="Actividad", max_length=200)
    desc = models.CharField(
        verbose_name="Descripcion del servicio", max_length=500)
    img = models.ImageField(verbose_name="Evidencia", upload_to="reporte", null=True, blank=True)

    class Meta:
        verbose_name = "Actividad"
        verbose_name_plural = "Actividades"

    def __str__(self):
        return self.actividad

class Diario(models.Model):
    fecha = models.DateField(verbose_name="Fecha")
    proyecto = models.ForeignKey(Proyectos,on_delete=models.PROTECT, verbose_name="Proyecto", null=True,blank=True )
    inicio_jornada = models.TimeField(verbose_name="Inicio de jornada")
    termino_jornada = models.TimeField(verbose_name="Termino de jornada")
    no_vehiculo = models.SmallIntegerField(verbose_name="numero de vehículos",blank=True,  null=True)
    modelos_vehiculos = models.ManyToManyField(Vehiculos, verbose_name="Modelo",blank=True, null=True, related_name='Modelo')
    tipos_servicios = (('Supervision','Supervision'),('Rescate de Flora','Rescate de Flora'),('Rescate de Fauna','Resctae de Fauna'),('Mantenimiento de Flora','Mantenimiento de Flora'),('Monitoreo','Monitoreo'),('Fomento de Seguridad','Fomento de Seguridad'))
    servicio = models.CharField(max_length=20, choices=tipos_servicios, default='SUPERVISION')
    responsable = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        verbose_name="Responsable en sitio",
        related_name='responsable')
    supervisor = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        verbose_name="Supervisor de seguridad y ambiente",
        related_name='supervisor')
    no_coordi = models.SmallIntegerField(verbose_name="numero de coordinadores")
    coordinadores = models.ManyToManyField(User,verbose_name="Coordinadores", related_name='Coordinadores')
    no_especialistas = models.SmallIntegerField(verbose_name="numero de Especialistas")
    especialistas = models.ManyToManyField(User,verbose_name="Especialistas",related_name='Especialistas')
    no_tec = models.SmallIntegerField(verbose_name="numero de Técnicos")
    tecnicos = models.ManyToManyField(User,verbose_name="Técnicos", related_name='Tecnicos')
    actividad = models.ForeignKey(Actividad,on_delete=models.PROTECT, verbose_name="Actividad a realizar")
    desc = RichTextField(verbose_name="Descripcion de la actividad", max_length=5000)
    img = models.ImageField(verbose_name="Evidencia", upload_to="reporte", null=True, blank=True)
    #mas actividades si son necesarias
    act_1 = models.ForeignKey(Actividad,on_delete=models.PROTECT, verbose_name="Actividad a realizar", null=True, blank=True, related_name ='actividad_1')
    desc_1 = RichTextField(verbose_name="Descripcion de la actividad", max_length=5000,  null=True, blank=True)
    img_1 = models.ImageField(verbose_name="Evidencia", upload_to="reporte", null=True, blank=True)
    act_2 = models.ForeignKey(Actividad,on_delete=models.PROTECT, verbose_name="Actividad a realizar",  null=True, blank=True, related_name ='actividad_2')
    desc_2 = RichTextField(verbose_name="Descripcion de la actividad", max_length=5000,  null=True, blank=True)
    img_2 = models.ImageField(verbose_name="Evidencia", upload_to="reporte", null=True, blank=True)
    act_3 = models.ForeignKey(Actividad,on_delete=models.PROTECT, verbose_name="Actividad a realizar",  null=True, blank=True, related_name ='actividad_3')
    desc_3 = RichTextField(verbose_name="Descripcion de la actividad", max_length=5000,  null=True, blank=True)
    img_3 = models.ImageField(verbose_name="Evidencia", upload_to="reporte", null=True, blank=True)
    act_4 = models.ForeignKey(Actividad,on_delete=models.PROTECT, verbose_name="Actividad a realizar",  null=True, blank=True, related_name ='actividad_4')
    desc_4 = RichTextField(verbose_name="Descripcion de la actividad", max_length=5000,  null=True, blank=True)
    img_4 = models.ImageField(verbose_name="Evidencia", upload_to="reporte", null=True, blank=True)
    act_5 = models.ForeignKey(Actividad,on_delete=models.PROTECT, verbose_name="Actividad a realizar",  null=True, blank=True, related_name ='actividad_5')
    desc_5 = RichTextField(verbose_name="Descripcion de la actividad", max_length=5000,  null=True, blank=True)
    img_5 = models.ImageField(verbose_name="Evidencia", upload_to="reporte", null=True, blank=True)
    act_6 = models.ForeignKey(Actividad,on_delete=models.PROTECT, verbose_name="Actividad a realizar",  null=True, blank=True, related_name ='actividad_6')
    desc_6 = RichTextField(verbose_name="Descripcion de la actividad", max_length=5000,  null=True, blank=True)
    img_6 = models.ImageField(verbose_name="Evidencia", upload_to="reporte", null=True, blank=True)
    act_7 = models.ForeignKey(Actividad,on_delete=models.PROTECT, verbose_name="Actividad a realizar",  null=True, blank=True, related_name ='actividad_7')
    desc_7 = RichTextField(verbose_name="Descripcion de la actividad", max_length=5000,  null=True, blank=True)
    img_7 = models.ImageField(verbose_name="Evidencia", upload_to="reporte", null=True, blank=True)
    act_8 = models.ForeignKey(Actividad,on_delete=models.PROTECT, verbose_name="Actividad a realizar",  null=True, blank=True, related_name ='actividad_8')
    desc_8 = RichTextField(verbose_name="Descripcion de la actividad", max_length=5000,  null=True, blank=True)
    img_8 = models.ImageField(verbose_name="Evidencia", upload_to="reporte", null=True, blank=True)
    act_9 = models.ForeignKey(Actividad,on_delete=models.PROTECT, verbose_name="Actividad a realizar",  null=True, blank=True, related_name ='actividad_9')
    desc_9 = RichTextField(verbose_name="Descripcion de la actividad", max_length=5000,  null=True, blank=True)
    img_9 = models.ImageField(verbose_name="Evidencia", upload_to="reporte", null=True, blank=True)

    class Meta:
        verbose_name = "Reporte diario"
        verbose_name_plural = "Reportes Diarios"
        ordering = ['-pk']

    def __str__(self):
        return self.servicio