from django.db import models

# Create your models here.


class categoria(models.Model):
    nombre = models.CharField(max_length=20, null=False, unique=True, verbose_name='nombre')
    nada = models.CharField(null=True,max_length=100)
   
    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'categoria'
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['id']


class producto(models.Model):
    nombre = models.CharField(max_length=50, null=False, verbose_name='nombre')
    descripcion = models.CharField(max_length=1000, null=True, verbose_name='descripcion')
    imagen = models.ImageField(verbose_name='imagen',null=True, upload_to='productosfotos/')
    categoria = models.ForeignKey(categoria, on_delete=models.CASCADE, null=False)
    precio = models.FloatField(null=True, verbose_name='precio')
    nada = models.CharField(null=True,max_length=100)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'producto'
        verbose_name = 'Producto'
        verbose_name_plural = 'productos'
        ordering = ['id']
