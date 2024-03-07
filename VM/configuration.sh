#!/bin/bash

# Actualizar el sistema y instalar dependencias necesarias
sudo apt-get update
sudo apt-get install -y ca-certificates curl git

# Instalar Docker
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/debian/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/debian $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

# Permitir a todos los usuarios usar Docker sin sudo
sudo groupadd docker
sudo usermod -aG docker $USER
echo "Si hay más usuarios, deberás agregarlos manualmente al grupo 'docker' para permitirles usar Docker sin sudo."

# Probar Docker
sudo docker run hello-world

# Definir el directorio de instalación de MiniConda
MINICONDA_DIR="/opt/miniconda3"

# Verificar y eliminar el directorio de MiniConda si ya existe
if [ -d "$MINICONDA_DIR" ]; then
    echo "$MINICONDA_DIR ya existe. Eliminando para una instalación limpia."
    sudo rm -rf $MINICONDA_DIR
fi

# Descargar e instalar MiniConda
echo "Instalando MiniConda en $MINICONDA_DIR..."
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
chmod +x Miniconda3-latest-Linux-x86_64.sh
sudo ./Miniconda3-latest-Linux-x86_64.sh -b -p $MINICONDA_DIR

# Agregar MiniConda al PATH para todos los usuarios
echo 'export PATH="'$MINICONDA_DIR'/bin:$PATH"' | sudo tee /etc/profile.d/miniconda.sh > /dev/null

# Asegurar que el PATH se actualice inmediatamente para el usuario actual
echo 'export PATH="/opt/miniconda3/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc

# Limpieza
rm Miniconda3-latest-Linux-x86_64.sh

echo "Para que los cambios en MiniConda surtan efecto, tendrás que reiniciar la VM o cerrar sesión y volver a entrar."
echo "La instalación de Docker, MiniConda y Git ha finalizado."
