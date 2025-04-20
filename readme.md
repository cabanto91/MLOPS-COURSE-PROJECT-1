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

2. *Paso 02 Configurar jenkis container:*
   - Logear docker en mi maquina
   - correr el codigo `docker build -t jenkins-dind .`
   - comprobar la instalacion de docker `docker images`
   - levanta la imagen de docker en terminal de windows(no en power shell) `docker run -d --name jenkins-dind ^`
   - `--privileged ^`
   - `-p 8080 -p 5000:5000`
   - `-v //var/run/docker.sock:/var/run/docker.sock ^`
   - `-v jenkins_home:/var/jenkis_home`
   - `jenkins-dind`
3. *Paso 02 Configurar jenkis container:*
   - ejecutar codigo `docker logs jenkins-dind`
   - Buscas la contraseña y lo copias en al abrir el localhosta q se muestra en al contenedor
   - luego instala los plugis despues de ingresar en la web-localhost de jenkins.
4. *Paso 02 Configurar jenkis container:*
   - `docker exec -u root -it jenkins-dind bash`
   - `python3 --version`
   - `ln -s /usr/bin/python3 /usr/bin/python`
   - `python3 --version`
   - `apt install -y python3-pip`
   - `apt install -y python3-venv`
   - `exit`