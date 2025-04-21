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

# Jenkins in Docker with Python and Google Cloud CLI Setup

## 📦 Step 1: Install Docker Desktop

Download and install Docker Desktop for your system. Make sure Docker is running in the background.

---

## 🛠️ Step 2: Setup Jenkins in Docker

### 1. Create a `custom_jenkins` folder

```bash
mkdir custom_jenkins
cd custom_jenkins
```

### 2. Create a Dockerfile in the folder and paste the following:

```Dockerfile
# Use the Jenkins image as the base image
FROM jenkins/jenkins:lts

# Switch to root user to install dependencies
USER root

# Install prerequisites and Docker
RUN apt-get update -y && \
    apt-get install -y apt-transport-https ca-certificates curl gnupg software-properties-common && \
    curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add - && \
    echo "deb [arch=amd64] https://download.docker.com/linux/debian bullseye stable" > /etc/apt/sources.list.d/docker.list && \
    apt-get update -y && \
    apt-get install -y docker-ce docker-ce-cli containerd.io && \
    apt-get clean

# Add Jenkins user to the Docker group (create if it doesn't exist)
RUN groupadd -f docker && \
    usermod -aG docker jenkins

# Create Docker directory and volume for DinD
RUN mkdir -p /var/lib/docker
VOLUME /var/lib/docker

# Switch back to Jenkins user
USER jenkins
```

---

## 🚀 Step 3: Build and Run Jenkins Container

```bash
cd custom_jenkins

# Build the Docker image
docker build -t jenkins-dind .

# Check the image
docker images

# Run the Jenkins container
docker run -d --name jenkins-dind ^
--privileged ^
-p 8080:8080 -p 50000:50000 ^
-v //var/run/docker.sock:/var/run/docker.sock ^
-v jenkins_home:/var/jenkins_home ^
jenkins-dind
```

Get initial admin password:

```bash
docker ps
docker logs jenkins-dind
```

Go to `http://localhost:8080` and follow the installation steps:
- Paste the initial password
- Install suggested plugins
- Create your admin user

---

## :rocket: Step 3: Build and Run Jenkins Container

## 🐍 Step 4: Install Python inside Jenkins Container

```bash
docker exec -u root -it jenkins-dind bash
apt update -y
apt install -y python3
python3 --version
ln -s /usr/bin/python3 /usr/bin/python
python --version
apt install -y python3-pip
apt install -y python3-venv
exit
```

Restart Jenkins container:

```bash
docker restart jenkins-dind
```

---

## 🧪 Step 5: Sample Project Dockerfile (For Python Project)

Create a `Dockerfile` for your project:

```Dockerfile
# Use a lightweight Python image
FROM python:slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Install system dependencies required by LightGBM
RUN apt-get update && apt-get install -y --no-install-recommends \
    libgomp1 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY . .

RUN pip install --no-cache-dir -e .

RUN python pipeline/training_pipeline.py

EXPOSE 5000

CMD ["python", "application.py"]
```

---

## ☁️ Step 6: Install Google Cloud CLI in Jenkins Container

```bash
docker exec -u root -it jenkins-dind bash

apt-get update
apt-get install -y curl apt-transport-https ca-certificates gnupg

curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add -

echo "deb https://packages.cloud.google.com/apt cloud-sdk main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list

apt-get update && apt-get install -y google-cloud-sdk

gcloud --version
exit
```

---

## 🔐 Step 7: Grant Docker Permissions to Jenkins User

```bash
docker exec -u root -it jenkins-dind bash
groupadd docker
usermod -aG docker jenkins
usermod -aG root jenkins
exit

docker restart jenkins-dind
```

---

## ✅ Final Steps

- Go back to `http://localhost:8080` and log in.
- Follow any project-specific videos for detailed guidance.

---

**🎥 Note:** All remaining setup/configuration and advanced use cases are covered in your tutorial videos.