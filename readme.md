SUSCRIBETE: https://www.youtube.com/channel/UCJ_twZENBaL3L6AmIGYHVrw

Por si me quieres apoyar:https://www.buymeacoffee.com/antoniovalv


APIs usadas:
- google sheet  (necesario crear credenciales)
- invoice generator 
    info: https://github.com/Invoice-Generator/invoice-generator-api#subtotal-lines

Credenciales necesarias:

- google sheet
- email

Para las credenciales del email es necesario crear un archivo secrets.toml en la carpeta .streamlit con la siguiente estructura:
[db_credentials]
smtp_username = ''
smtp_password = ''

run the code:

streamlit run app.py

Para usar logo en las facturas es necesario subir el logo a un hosting de imagenes y envíarle a la API la url de la imagen.

- upload the image logo the a hot image. Used: https://imgbb.com/
("https://i.ibb.co/12MHwBs/logo.png")

ICONS:

- web: https://www.webfx.com/tools/emoji-cheat-sheet/
- tab menu: https://icons.getbootstrap.com/
