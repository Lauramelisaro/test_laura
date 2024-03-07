# Sincronizar Git en la VM
*Prerequisitos*: Tener GitHub, haber solicitado la inclusión del usuario en la Organización y tener acceso a la VM

1. Copiar SSH que se tengan localmente en la VM en la siguiente ubicación:
```
/home/<usuario-pc-sb>/.ssh
```

2. Ir a  ```GitHub > Settings > SSH and GPG keys > SSH keys``` y agregar una nueva SSH key con la SSH personal

3. Dar permisos y sincronizar
```
eval "$(ssh-agent -s)"
chmod 600 /home/<usuario-pc-sb>/.ssh/id_rsa
ssh-add ~/.ssh/id_rsa
ssh -T git@github.com

Sincronizar el user y correo

git clone git@github.com:<user>/<repo>.git
cd <repo>
git checkout <rama>
```
