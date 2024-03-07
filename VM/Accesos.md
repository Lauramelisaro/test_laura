# Accesos a la VM de Desarrollo

## Creación de la SSH Key
Ir a CMD para escribir el siguiente comando, **no poner contraseña y guardar donde lo sugiere el terminal**.
Porfa crear un usuario con su nombre, para poder ser identificados y **sin** espacios, comas, numeros, etc.
``` 
ssh-keygen -C "<usuario>"
```

## Consulta de SSH Key
Imprimir y guardar lo que imprime este comando
``` type C:\Users\<usuario-pc-sb>\.ssh\id_rsa.pub```

## Proceso de Acceso
Compartir la clave de acceso con el equipo de AI Lab para brindar acceso.

## Acceso
1. Descargar la extensión de VS Code **Remote - SSH** (con chulito de certificacción de Microsoft)
2. Ir a la extensión en el panel izquierdo en la sección de remotes y SSH
3. Al lado derecho de SSH hacer click en el simbolo de **+**
4. Escribir "VM", después dar Enter y otra vez Enter
5. Agregar el siguiente código con su respectiva ruta a las SSH, usuario e IP díaria de la VM
```
Host VM
  HostName <IP VM>
  User <usuario>
  IdentityFile C:\Users\<usuario-pc-sb>\.ssh\id_rsa.pub
```
6. En la extensión ir al lado de "SSH" a la opción de actualizar (flecha) y hacer click, allí te debería aparecer la conexión a la VM
7. Hacer click en "VM" y en la flecha que señala a la derecha para realizar la conexión a la VM
8. Dar Linux y Continue


**Notas**: 
* Si existen errores en la primera conexión contactar a un miembro de AI Lab 
* Si existen errores de conexión validar si la VM está prendida, cambios de IP, rutas y por último eliminar el archivo de ``` C:\Users\<usuario-pc-sb>\.ssh\know_host ``` y volver a intentar conectarse