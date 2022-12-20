#:tw-23eb:  Instalando ToDo List
Clonar el repositorio
`git clone https://github.com/rulomak/challenge---`
 Entre detro de la carpeta del proyecto 
`cd challenge---`
Instalar el archivo requirements.txt
`pip install -r requirements.txt`

#  :tw-25b6: Corriendo  App
Para levantar el servidor 
`python manage.py runserver`

Acessando localhost:
`http://127.0.0.1:8000/todo/`

Usuario de prueba:
`usuario: invera_admin |
password: invera123`

Si lo desea puede crear uno nuevo desde:
`http://127.0.0.1:8000/admin/`

# :tw-23ec: consumiendo Api
* Accediendo a la URL:   http://127.0.0.1:8000/todo/
podra ver todas las tareas pendientes.

* Para crear una nueva tarea, dirijase a la parte inferior  en la pestaña 'HTML form'   llene los campos  y click en el boton POST.

* Si desea filtrar buscando una tarea que contenga una palabra o una fecha determinada, puede usar el boton  Filters  en la parte superior derecha

*  Para Editar, Borrar, y Marcar como completada una tarea, primero hay que selecionar la tarea,  se puede  hacer pasando el Id de la misma por la URL  
ejemplo `http://127.0.0.1:8000/todo/5/`

una ves selecionada se puede proceder a:
* Borrar con el boton delete  (esq. superior derecha )
* Marcar como completada (tilde en  is complete  - zona inferior de la pantalla )
* Editar, en la parte inferior de la pantalla pestaña 'Raw Data'  cambiendo lo que necesita  y haciendo click en PUT


