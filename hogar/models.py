from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

TIPO_VIVIENDA_CHOICES=[
    ("1", "Casa o departamento hasta primer piso"), 
    ("2", "Departamentos desde 2do piso en adelante"), 
    ("3", "Country/Barrio cerrado"),
    ("4", "Vivienda de ocupación transitoria"),
]

MATERIALES_CHOICES=[
    ("1", "Material"), 
    ("2", "Mat. Piedra y hasta 50% madera"), 
    ("3", "Madera"),
    ("4", "Construcción en seco"),
    ("5", "Adobe o similar"),
]

TECHO_CHOICES=[
    ("1", "Material"), 
    ("2", "Material y tejas"), 
    ("3", "Tirantería de madera y tejas"),
    ("4", "Tirantería de madera y zinc"),
    ("5", "Zinc"),
    ("6", "Tirantería de madera y paja"),
    ("7", "Tirantería de madera y tejas de madera"),
]

CERRAMIENTO_CHOICES=[
    ("1", "Totalmente cerrados"), 
    ("2", "Al menos un costado abierto"), 
    ("3", "Totalmente abiertos"),]

COMISIONES_CHOICES=[
    ("1", "0%"), 
    ("2", "5%"), 
    ("3", "10%"),
    ("4", "15%"),
    ("5", "20%"),
    ("6", "25%"),]

# Create your models here.
class CotizacionHogar(models.Model):
    tipoVivienda = models.CharField(choices=TIPO_VIVIENDA_CHOICES, max_length=100)
    materialesConstruccion = models.CharField(choices=MATERIALES_CHOICES, max_length=100)
    techo = models.CharField(choices=TECHO_CHOICES, max_length=100)
    cerramiento = models.CharField(choices=CERRAMIENTO_CHOICES, max_length=100)
    CP = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(9999)])
    disyuntor = models.BooleanField()
    alarma= models.BooleanField()
    arlamaMonitoreo= models.BooleanField()
    vigilancia= models.BooleanField()
    comision=models.CharField(choices=COMISIONES_CHOICES, max_length=10)
    cob1_capital = models.IntegerField()
    cob2_capital = models.IntegerField()
    cob3_capital = models.IntegerField()
    cob4_capital = models.IntegerField()
    cob5_capital = models.IntegerField()
    cob6_capital = models.IntegerField()
    cob7_capital = models.IntegerField()
    cob8_capital = models.IntegerField()
    cob9_capital = models.IntegerField()
    cob10_capital = models.IntegerField()
    cob11_capital = models.IntegerField()
    cob12_capital = models.IntegerField()
    cob13_capital = models.IntegerField()
    cob14_capital = models.IntegerField()
    cob15_capital = models.IntegerField()
    cob16_capital = models.IntegerField()
    cob17_capital = models.IntegerField()
    cob18_capital = models.IntegerField()
    cob19_capital = models.IntegerField()
    cob20_capital = models.IntegerField()
 
    class Meta:
        verbose_name ='Cotización'
        verbose_name_plural='Cotizaciones'
    
    def __str__(self):
        return "{}".format(self.pk)
