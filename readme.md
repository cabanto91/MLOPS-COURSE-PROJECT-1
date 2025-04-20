---

# **Interactive Guide: Jenkins & Docker Setup for MLOps Project**

---

1. *Paso 01 para Credenciales y Conectar GCP en Local:*

   - Instalar gcp cliente
   - ejecutar el codigo gcloud init y seleccion el proyecto que estoy trabajando
   - creo una cuenta de servicio añdiendo permiso de adminstora y object view (aplica a mi bucket tambien)
   - genero un key de `<JSON_KEY_GCP>` y almaceno en un lugar
   - Iniciar para conectarse: `gcloud auth application-default login`
   - Setear la key_user: `set GOOGLE_APPLICATION_CREDENTIALS=<JSON_KEY_GCP>`
- 
# MLOPS-COURSE-PROJECT-1
