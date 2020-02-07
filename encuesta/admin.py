from django.contrib import admin

from . import models

# Register your models here.
# [TG20200207] Registrar las entidades de nuestro modelo
admin.site.register(models.TipoIdentificacion)
admin.site.register(models.TipoUrbanizacionCliente)
admin.site.register(models.TipoEnvase)
admin.site.register(models.EnvaseSubtipo)
admin.site.register(models.FormaPago)
admin.site.register(models.ProductoCategoria)
admin.site.register(models.Cliente)
admin.site.register(models.Producto)
admin.site.register(models.PedidoCliente)
admin.site.register(models.Proveedor)
