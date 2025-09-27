from django.db import models

class FichaEstudiantil(models.Model):
    # Antecedentes Generales
    nombre_completo = models.CharField(max_length=255)
    genero = models.CharField(max_length=50)
    rut = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField()
    telefono = models.CharField(max_length=20)
    centro_salud = models.CharField(max_length=255)
    direccion_actual = models.CharField(max_length=255)
    direccion_origen = models.CharField(max_length=255)
    correo_institucional = models.EmailField()
    correo_personal = models.EmailField()
    prevision = models.CharField(max_length=50)

    # Contacto de emergencia
    contacto_nombre = models.CharField(max_length=255)
    contacto_telefono = models.CharField(max_length=20)

    # Antecedentes Académicos
    nombre_social = models.CharField(max_length=255, blank=True, null=True)
    carrera = models.CharField(max_length=255)
    anio = models.IntegerField()
    estado = models.CharField(max_length=50)
    asignatura = models.CharField(max_length=255)

    # Antecedentes Mórbidos
    alergias = models.BooleanField()
    detalle_alergias = models.TextField(blank=True, null=True)
    grupo_sanguineo = models.CharField(max_length=5)
    enfermedad_cronica = models.BooleanField()
    detalle_enfermedad = models.TextField(blank=True, null=True)
    medicamento_diario = models.BooleanField()
    detalle_medicamento = models.TextField(blank=True, null=True)
    otros_antecedentes = models.TextField(blank=True, null=True)

    # Vacunas / Serología
    covid_dosis = models.CharField(max_length=255)
    hepatitis_b_dosis = models.CharField(max_length=255)
    varicela_dosis = models.CharField(max_length=255)
    influenza_dosis = models.CharField(max_length=255)

    # Documentación Adjunta (solo nombres de archivo o paths)
    ci_pdf = models.FileField(upload_to='documentos/', blank=True, null=True)
    certificado_medico = models.FileField(upload_to='documentos/', blank=True, null=True)
    carnet_hepatitis = models.FileField(upload_to='documentos/', blank=True, null=True)
    examen_varicela = models.FileField(upload_to='documentos/', blank=True, null=True)
    certificado_influenza = models.FileField(upload_to='documentos/', blank=True, null=True)
    certificado_covid = models.FileField(upload_to='documentos/', blank=True, null=True)
    curso_covid = models.FileField(upload_to='documentos/', blank=True, null=True)
    curso_epp = models.FileField(upload_to='documentos/', blank=True, null=True)
    curso_iaas = models.FileField(upload_to='documentos/', blank=True, null=True)
    curso_rcp = models.FileField(upload_to='documentos/', blank=True, null=True)
    induccion_clinico = models.FileField(upload_to='documentos/', blank=True, null=True)

    # Declaración
    declaracion_nombre = models.CharField(max_length=255)
    declaracion_rut = models.CharField(max_length=20)
    declaracion_fecha = models.DateField()

    def __str__(self):
        return self.nombre_completo
