# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


#[TG 20200207] Colocar una enumeracion para que sirva de estado, activo e inactivo
ESTADOS_EN_SISTEMA = [ (1, 'Activo'), (-1, 'Inactivo')]


class CentroDistribucion(models.Model):
    cod_centrodis = models.AutoField(db_column='COD_CENTRODIS', primary_key=True)  # Field name made lowercase.
    nom_centrodis = models.CharField(db_column='NOM_CENTRODIS', max_length=200, blank=True, null=True)  # Field name made lowercase.
    dir_centrodis = models.CharField(db_column='DIR_CENTRODIS', max_length=200, blank=True, null=True)  # Field name made lowercase.
    cel_centrodis = models.CharField(db_column='CEL_CENTRODIS', max_length=20, blank=True, null=True)  # Field name made lowercase.
    res_centrdis = models.CharField(db_column='RES_CENTRDIS', max_length=200, blank=True, null=True)  # Field name made lowercase.
    dcd_centrodis = models.FloatField(db_column='DCD_CENTRODIS', blank=True, null=True)  # Field name made lowercase.
    cob_centrodis = models.FloatField(db_column='COB_CENTRODIS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'centro_distribucion'

    def __str__(self):
        return self.nom_centrodis



class Cliente(models.Model):
    cod_cliente = models.AutoField(db_column='COD_CLIENTE', primary_key=True)  # Field name made lowercase.
    cod_tipoid = models.ForeignKey('TipoIdentificacion', models.DO_NOTHING, db_column='COD_TIPOID', blank=True, null=True)  # Field name made lowercase.
    cod_formapag = models.ForeignKey('FormaPago', models.DO_NOTHING, db_column='COD_FORMAPAG', blank=True, null=True)  # Field name made lowercase.
    nom_cliente = models.CharField(db_column='NOM_CLIENTE', max_length=200)  # Field name made lowercase.
    dir_cliente = models.CharField(db_column='DIR_CLIENTE', max_length=200)  # Field name made lowercase.
    cel_cliente = models.CharField(db_column='CEL_CLIENTE', max_length=200)  # Field name made lowercase.
    ema_cliente = models.CharField(db_column='EMA_CLIENTE', max_length=200, blank=True, null=True)  # Field name made lowercase.
    dcd_cliente = models.FloatField(db_column='DCD_CLIENTE', blank=True, null=True)  # Field name made lowercase.
    est_cliente = models.SmallIntegerField(db_column='EST_CLIENTE', choices=ESTADOS_EN_SISTEMA, blank=False, null=False)  # Field name made lowercase.
    ide_cliente = models.CharField(db_column='IDE_CLIENTE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    uin_cliente = models.SmallIntegerField(db_column='UIN_CLIENTE')  # Field name made lowercase.
    uac_cliente = models.SmallIntegerField(db_column='UAC_CLIENTE')  # Field name made lowercase.
    fac_cliente = models.DateTimeField(db_column='FAC_CLIENTE')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'cliente'

    def __str__(self):
        return self.nom_cliente



class ClienteUrbanizacion(models.Model):
    cod_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='COD_CLIENTE')  # Field name made lowercase.
    cod_urbanizacion = models.ForeignKey('Urbanizacion', models.DO_NOTHING, db_column='COD_URBANIZACION')  # Field name made lowercase.
    cod_cliurb = models.AutoField(db_column='COD_CLIURB', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'cliente_urbanizacion'


class ContenedorPatito(models.Model):
    cod_contenedorpat = models.AutoField(db_column='COD_CONTENEDORPAT', primary_key=True)  # Field name made lowercase.
    cod_suministradorcon = models.ForeignKey('SuministradorContenedor', models.DO_NOTHING, db_column='COD_SUMINISTRADORCON', blank=True, null=True)  # Field name made lowercase.
    cod_tipoenv = models.ForeignKey('TipoEnvase', models.DO_NOTHING, db_column='COD_TIPOENV', blank=True, null=True)  # Field name made lowercase.
    nom_contenedorpat = models.CharField(db_column='NOM_CONTENEDORPAT', max_length=200)  # Field name made lowercase.
    smc_contenedorpat = models.IntegerField(db_column='SMC_CONTENEDORPAT', blank=True, null=True)  # Field name made lowercase.
    tal_contenedorpat = models.CharField(db_column='TAL_CONTENEDORPAT', max_length=20, blank=True, null=True)  # Field name made lowercase.
    est_contenedorpat = models.SmallIntegerField(db_column='EST_CONTENEDORPAT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'contenedor_patito'



class Entrega(models.Model):
    cod_entrega = models.AutoField(db_column='COD_ENTREGA', primary_key=True)  # Field name made lowercase.
    cod_ruta = models.ForeignKey('Ruta', models.DO_NOTHING, db_column='COD_RUTA', blank=True, null=True)  # Field name made lowercase.
    cod_contenedorpat = models.ForeignKey(ContenedorPatito, models.DO_NOTHING, db_column='COD_CONTENEDORPAT', blank=True, null=True)  # Field name made lowercase.
    fec_entrega = models.DateTimeField(db_column='FEC_ENTREGA')  # Field name made lowercase.
    obs_entrega = models.CharField(db_column='OBS_ENTREGA', max_length=200, blank=True, null=True)  # Field name made lowercase.
    est_entrega = models.SmallIntegerField(db_column='EST_ENTREGA', blank=True, null=True)  # Field name made lowercase.
    ide_entrega = models.CharField(db_column='IDE_ENTREGA', max_length=200, blank=True, null=True)  # Field name made lowercase.
    uin_entrega = models.SmallIntegerField(db_column='UIN_ENTREGA')  # Field name made lowercase.
    uac_enterga = models.SmallIntegerField(db_column='UAC_ENTERGA')  # Field name made lowercase.
    fac_entrega = models.DateTimeField(db_column='FAC_ENTREGA')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'entrega'


class EnvaseSubtipo(models.Model):
    cod_envasesub = models.SmallAutoField(db_column='COD_ENVASESUB', primary_key=True)  # Field name made lowercase.
    cod_tipoenv = models.ForeignKey('TipoEnvase', models.DO_NOTHING, db_column='COD_TIPOENV', blank=True, null=True)  # Field name made lowercase.
    nom_envasesub = models.CharField(db_column='NOM_ENVASESUB', max_length=50)  # Field name made lowercase.
    vol_envasesub = models.FloatField(db_column='VOL_ENVASESUB')  # Field name made lowercase.
    uvo_envasesub = models.FloatField(db_column='UVO_ENVASESUB')  # Field name made lowercase.
    cos_envasesub = models.FloatField(db_column='COS_ENVASESUB', blank=True, null=True)  # Field name made lowercase.
    est_envasesub = models.SmallIntegerField(db_column='EST_ENVASESUB', choices=ESTADOS_EN_SISTEMA, blank=False, null=False)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'envase_subtipo'

    def __str__(self):
        return self.nom_envasesub


class Factura(models.Model):
    cod_factura = models.AutoField(db_column='COD_FACTURA', primary_key=True)  # Field name made lowercase.
    cod_formapag = models.ForeignKey('FormaPago', models.DO_NOTHING, db_column='COD_FORMAPAG', blank=True, null=True)  # Field name made lowercase.
    fec_factura = models.DateTimeField(db_column='FEC_FACTURA')  # Field name made lowercase.
    ruc_factura = models.CharField(db_column='RUC_FACTURA', max_length=13)  # Field name made lowercase.
    sub_factura = models.FloatField(db_column='SUB_FACTURA')  # Field name made lowercase.
    iva_factura = models.FloatField(db_column='IVA_FACTURA')  # Field name made lowercase.
    tot_factura = models.FloatField(db_column='TOT_FACTURA')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'factura'


class FacturaDetalle(models.Model):
    cd_facturadet = models.AutoField(db_column='CD_FACTURADET', primary_key=True)  # Field name made lowercase.
    cod_factura = models.ForeignKey(Factura, models.DO_NOTHING, db_column='COD_FACTURA', blank=True, null=True)  # Field name made lowercase.
    nui_facturadet = models.FloatField(db_column='NUI_FACTURADET')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'factura_detalle'


class FormaPago(models.Model):
    cod_formapag = models.AutoField(db_column='COD_FORMAPAG', primary_key=True)  # Field name made lowercase.
    nom_formapag = models.CharField(db_column='NOM_FORMAPAG', max_length=200)  # Field name made lowercase.
    est_formapag = models.SmallIntegerField(db_column='EST_FORMAPAG', choices=ESTADOS_EN_SISTEMA, blank=False, null=False)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'forma_pago'

    def __str__(self):
        return self.nom_formapag


class PedidoCliente(models.Model):
    cod_pedidocli = models.AutoField(db_column='COD_PEDIDOCLI', primary_key=True)  # Field name made lowercase.
    cod_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='COD_CLIENTE', blank=True, null=True)  # Field name made lowercase.
    ide_pedidocli = models.CharField(db_column='IDE_PEDIDOCLI', max_length=200, blank=True, null=True)  # Field name made lowercase.
    fec_pedidocli = models.DateTimeField(db_column='FEC_PEDIDOCLI')  # Field name made lowercase.
    obs_pedidocli = models.CharField(db_column='OBS_PEDIDOCLI', max_length=200, blank=True, null=True)  # Field name made lowercase.
    val_pedidocli = models.FloatField(db_column='VAL_PEDIDOCLI')  # Field name made lowercase.
    est_pedidocli = models.SmallIntegerField(db_column='EST_PEDIDOCLI', choices=ESTADOS_EN_SISTEMA, blank=False, null=False)  # Field name made lowercase.
    npp_pedidocli = models.IntegerField(db_column='NPP_PEDIDOCLI', blank=True, null=True)  # Field name made lowercase.
    uin_pedidocli = models.SmallIntegerField(db_column='UIN_PEDIDOCLI')  # Field name made lowercase.
    uac_pedidocli = models.SmallIntegerField(db_column='UAC_PEDIDOCLI')  # Field name made lowercase.
    fac_pedidocli = models.DateTimeField(db_column='FAC_PEDIDOCLI')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'pedido_cliente'

    def __str__(self):
        return str(self.cod_pedidocli)


class PedidoClienteDetalle(models.Model):
    cod_pedidoclidet = models.AutoField(db_column='COD_PEDIDOCLIDET', primary_key=True)  # Field name made lowercase.
    cod_producto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='COD_PRODUCTO', blank=True, null=True)  # Field name made lowercase.
    cod_pedidocli = models.ForeignKey(PedidoCliente, models.DO_NOTHING, db_column='COD_PEDIDOCLI', blank=True, null=True)  # Field name made lowercase.
    cod_contenedorpat = models.ForeignKey(ContenedorPatito, models.DO_NOTHING, db_column='COD_CONTENEDORPAT', blank=True, null=True)  # Field name made lowercase.
    nud_pedidoclidet = models.FloatField(db_column='NUD_PEDIDOCLIDET')  # Field name made lowercase.
    pnu_pedidoclidet = models.FloatField(db_column='PNU_PEDIDOCLIDET', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'pedido_cliente_detalle'


class PedidoEntrega(models.Model):
    cod_entrega = models.ForeignKey(Entrega, models.DO_NOTHING, db_column='COD_ENTREGA')  # Field name made lowercase.
    cod_pedidocli = models.ForeignKey(PedidoCliente, models.DO_NOTHING, db_column='COD_PEDIDOCLI')  # Field name made lowercase.
    cod_entped = models.AutoField(db_column='COD_ENTPED', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'pedido_entrega'


class PedidoProveedor(models.Model):
    cod_pedidopro = models.AutoField(db_column='COD_PEDIDOPRO', primary_key=True)  # Field name made lowercase.
    cod_proveedor = models.ForeignKey('Proveedor', models.DO_NOTHING, db_column='COD_PROVEEDOR', blank=True, null=True)  # Field name made lowercase.
    fec_pedidopro = models.DateField(db_column='FEC_PEDIDOPRO', blank=True, null=True)  # Field name made lowercase.
    obs_pedidopro = models.CharField(db_column='OBS_PEDIDOPRO', max_length=200, blank=True, null=True)  # Field name made lowercase.
    est_pedidopro = models.SmallIntegerField(db_column='EST_PEDIDOPRO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'pedido_proveedor'


class PedidoProveedorDetalle(models.Model):
    cod_pedidoprodet = models.AutoField(db_column='COD_PEDIDOPRODET', primary_key=True)  # Field name made lowercase.
    cod_pedidopro = models.ForeignKey(PedidoProveedor, models.DO_NOTHING, db_column='COD_PEDIDOPRO', blank=True, null=True)  # Field name made lowercase.
    cod_producto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='COD_PRODUCTO', blank=True, null=True)  # Field name made lowercase.
    nup_pedidoprodet = models.FloatField(db_column='NUP_PEDIDOPRODET')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'pedido_proveedor_detalle'


class Producto(models.Model):
    cod_producto = models.SmallAutoField(db_column='COD_PRODUCTO', primary_key=True)  # Field name made lowercase.
    cod_envasesub = models.ForeignKey(EnvaseSubtipo, models.DO_NOTHING, db_column='COD_ENVASESUB', blank=True, null=True)  # Field name made lowercase.
    cod_categoriapro = models.ForeignKey('ProductoCategoria', models.DO_NOTHING, db_column='COD_CATEGORIAPRO', blank=True, null=True)  # Field name made lowercase.
    cod_proveedor = models.ForeignKey('Proveedor', models.DO_NOTHING, db_column='COD_PROVEEDOR', blank=True, null=True)  # Field name made lowercase.
    nom_producto = models.CharField(db_column='NOM_PRODUCTO', max_length=200)  # Field name made lowercase.
    pvp_producto = models.FloatField(db_column='PVP_PRODUCTO', blank=True, null=True)  # Field name made lowercase.
    ppr_producto = models.FloatField(db_column='PPR_PRODUCTO', blank=True, null=True)  # Field name made lowercase.
    cos_producto = models.FloatField(db_column='COS_PRODUCTO', blank=True, null=True)  # Field name made lowercase.
    ori_producto = models.CharField(db_column='ORI_PRODUCTO', max_length=200, blank=True, null=True)  # Field name made lowercase.
    gra_producto = models.FloatField(db_column='GRA_PRODUCTO', blank=True, null=True)  # Field name made lowercase.
    tep_producto = models.FloatField(db_column='TEP_PRODUCTO', blank=True, null=True)  # Field name made lowercase.
    ump_producto = models.CharField(db_column='UMP_PRODUCTO', max_length=200, blank=True, null=True)  # Field name made lowercase.
    smp_producto = models.FloatField(db_column='SMP_PRODUCTO', blank=True, null=True)  # Field name made lowercase.
    tal_producto = models.CharField(db_column='TAL_PRODUCTO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    est_producto = models.SmallIntegerField(db_column='EST_PRODUCTO', blank=True, null=True)  # Field name made lowercase.
    uin_producto = models.SmallIntegerField(db_column='UIN_PRODUCTO')  # Field name made lowercase.
    uac_producto = models.SmallIntegerField(db_column='UAC_PRODUCTO')  # Field name made lowercase.
    fac_producto = models.DateTimeField(db_column='FAC_PRODUCTO')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'producto'

    def __str__(self):
        return self.nom_producto


class ProductoCategoria(models.Model):
    cod_categoriapro = models.AutoField(db_column='COD_CATEGORIAPRO', primary_key=True)  # Field name made lowercase.
    nom_categoriapro = models.CharField(db_column='NOM_CATEGORIAPRO', max_length=200)  # Field name made lowercase.
    est_categoriapro = models.SmallIntegerField(db_column='EST_CATEGORIAPRO', choices=ESTADOS_EN_SISTEMA, blank=False, null=False)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'producto_categoria'

    def __str__(self):
        return self.nom_categoriapro


class Proveedor(models.Model):
    cod_proveedor = models.AutoField(db_column='COD_PROVEEDOR', primary_key=True)  # Field name made lowercase.
    nom_proveedor = models.CharField(db_column='NOM_PROVEEDOR', max_length=200)  # Field name made lowercase.
    dir_proveedor = models.CharField(db_column='DIR_PROVEEDOR', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ema_proveedor = models.CharField(db_column='EMA_PROVEEDOR', max_length=200, blank=True, null=True)  # Field name made lowercase.
    cel_proveedor = models.CharField(db_column='CEL_PROVEEDOR', max_length=200, blank=True, null=True)  # Field name made lowercase.
    dcd_proveedor = models.FloatField(db_column='DCD_PROVEEDOR', blank=True, null=True)  # Field name made lowercase.
    est_proveedor = models.SmallIntegerField(db_column='EST_PROVEEDOR', choices=ESTADOS_EN_SISTEMA)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'proveedor'

    def __str__(self):
        return self.nom_proveedor



class Repartidor(models.Model):
    cod_repartidor = models.AutoField(db_column='COD_REPARTIDOR', primary_key=True)  # Field name made lowercase.
    cod_centrodis = models.ForeignKey(CentroDistribucion, models.DO_NOTHING, db_column='COD_CENTRODIS', blank=True, null=True)  # Field name made lowercase.
    nom_repartidor = models.CharField(db_column='NOM_REPARTIDOR', max_length=200)  # Field name made lowercase.
    cel_repartidor = models.CharField(db_column='CEL_REPARTIDOR', max_length=20)  # Field name made lowercase.
    fot_repartidor = models.CharField(db_column='FOT_REPARTIDOR', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'repartidor'

    def __str__(self):
        return self.nom_repartidor



class Ruta(models.Model):
    cod_ruta = models.AutoField(db_column='COD_RUTA', primary_key=True)  # Field name made lowercase.
    cod_repartidor = models.ForeignKey(Repartidor, models.DO_NOTHING, db_column='COD_REPARTIDOR', blank=True, null=True)  # Field name made lowercase.
    dis_ruta = models.FloatField(db_column='DIS_RUTA', blank=True, null=True)  # Field name made lowercase.
    tie_ruta = models.FloatField(db_column='TIE_RUTA', blank=True, null=True)  # Field name made lowercase.
    cob_ruta = models.FloatField(db_column='COB_RUTA', blank=True, null=True)  # Field name made lowercase.
    fec_ruta = models.DateTimeField(db_column='FEC_RUTA', blank=True, null=True)  # Field name made lowercase.
    est_ruta = models.SmallIntegerField(db_column='EST_RUTA', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'ruta'


class SuministradorContenedor(models.Model):
    cod_suministradorcon = models.AutoField(db_column='COD_SUMINISTRADORCON', primary_key=True)  # Field name made lowercase.
    nom_suministradorcon = models.CharField(db_column='NOM_SUMINISTRADORCON', max_length=200)  # Field name made lowercase.
    dir_suministradorcon = models.CharField(db_column='DIR_SUMINISTRADORCON', max_length=200, blank=True, null=True)  # Field name made lowercase.
    cel_suministradorcon = models.CharField(db_column='CEL_SUMINISTRADORCON', max_length=20, blank=True, null=True)  # Field name made lowercase.
    est_suministradorcon = models.SmallIntegerField(db_column='EST_SUMINISTRADORCON', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'suministrador_contenedor'


class TipoEnvase(models.Model):
    cod_tipoenv = models.AutoField(db_column='COD_TIPOENV', primary_key=True)  # Field name made lowercase.
    nm_tipoenv = models.CharField(db_column='NM_TIPOENV', max_length=200)  # Field name made lowercase.
    obs_tipoenv = models.CharField(db_column='OBS_TIPOENV', max_length=200, blank=True, null=True)  # Field name made lowercase.
    est_tipoenv = models.SmallIntegerField(db_column='EST_TIPOENV', choices=ESTADOS_EN_SISTEMA, blank=False, null=False)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'tipo_envase'

    def __str__(self):
        return self.nm_tipoenv


class TipoIdentificacion(models.Model):
    cod_tipoid = models.AutoField(db_column='COD_TIPOID', primary_key=True)  # Field name made lowercase.
    nm_tipoid = models.CharField(db_column='NM_TIPOID', max_length=200)  # Field name made lowercase.
    est_tipoid = models.SmallIntegerField(db_column='EST_TIPOID', choices=ESTADOS_EN_SISTEMA, blank=False, null=False)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'tipo_identificacion'

    def __str__(self):
        return self.nm_tipoid


class TipoUrbanizacionCliente(models.Model):
    cod_tipourb = models.AutoField(db_column='COD_TIPOURB', primary_key=True)  # Field name made lowercase.
    nom_tipurb = models.CharField(db_column='NOM_TIPURB', max_length=200)  # Field name made lowercase.
    est_tipourb = models.SmallIntegerField(db_column='EST_TIPOURB', choices=ESTADOS_EN_SISTEMA, blank=False, null=False)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'tipo_urbanizacion_cliente'

    def __str__(self):
        return self.nom_tipurb


class Urbanizacion(models.Model):
    cod_urbanizacion = models.AutoField(db_column='COD_URBANIZACION', primary_key=True)  # Field name made lowercase.
    cod_tipourb = models.ForeignKey(TipoUrbanizacionCliente, models.DO_NOTHING, db_column='COD_TIPOURB', blank=True, null=True)  # Field name made lowercase.
    nom_urbanizacion = models.CharField(db_column='NOM_URBANIZACION', max_length=200)  # Field name made lowercase.
    dir_urbanizacion = models.CharField(db_column='DIR_URBANIZACION', max_length=200, blank=True, null=True)  # Field name made lowercase.
    zon_urbanizacion = models.CharField(db_column='ZON_URBANIZACION', max_length=200, blank=True, null=True)  # Field name made lowercase.
    dcd_urbanizacion = models.FloatField(db_column='DCD_URBANIZACION', blank=True, null=True)  # Field name made lowercase.
    est_urbanizacion = models.SmallIntegerField(db_column='EST_URBANIZACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'urbanizacion'

    def __str__(self):
        return self.nom_urbanizacion
