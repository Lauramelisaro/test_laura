from google.cloud import secretmanager



# Crea un cliente de Secret Manager
client = secretmanager.SecretManagerServiceClient()


# Listar todos los secrets
client.list_secrets(request={"parent": 'projects/709427406268'})


# Info del secreto
secret = client.get_secret(name='projects/709427406268/secrets/secret-test-txt')


# Recupera el secreto
response = client.access_secret_version(name="projects/709427406268/secrets/secret-test-txt/versions/latest")


# Obtiene el valor del secreto
secret_value = response.payload.data.decode("UTF-8")