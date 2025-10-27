from django.db import models

# Create your models here.
class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    contacto = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    email = models.EmailField()
    direccion = models.TextField()
    foto_proveedor = models.ImageField(upload_to='img_proveedores/', blank=True, null=True)
    
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name = "Proveedor"
        verbose_name_plural = "proveedores"
        
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    fech_creacion = models.DateField()
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, related_name='productos')
    
    def __str__(self):
        return f"{self.nombre} - {self.descripcion} - {self.precio} - {self.stock} - {self.fech_creacion} - {self.proveedor.nombre}"
    
    
    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
    
