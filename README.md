
Resumen de Funcionalidad de la Página de Inicio (URLS MEJORADAS EN TODO SENTIDO, EL USUARIO TIENE ACCESO A LA NAVEGACION Y SOLAMENTE EL ADMIN QUE ES TEST PUEDE CAMBIAR TODA LA INFORMACION DE LOS USUARIOS QUE HAY EN LA WEB UPDATE SEPTIEMBRE)
LINK FUNCIONALIDAD youtube https://youtu.be/rdd5tZM8zb8

En mi aplicación web, la página de inicio está diseñada para ofrecer a los usuarios una serie de funcionalidades clave mediante varios botones de navegación. A continuación, detallo cada una de estas funcionalidades y cómo están implementadas:

1. Quiero Ser Cliente (Registrarme)-CAMBIADO AL LOGIN DE REGISTRO DE USUARIO CON UN SOLO CLICK POR LO CUAL ES MAS FACIL

    Funcionalidad: Este botón dirige a los usuarios a una página que contiene un formulario para el registro de nuevos clientes.
    URL: /form-con-api/
    Descripción: Los usuarios pueden completar un formulario con su nombre de usuario, contraseña y número de caso para registrarse como clientes. La información ingresada se almacena en la base de datos para su posterior uso.

2. Ya Soy Cliente (Ver mi Caso)- FUNCION CAMBIADA POR EL LOGIN Y REGISTRO DONDE SOLAMENTE EL USUARIO CORRECTAMENTE REGISTRADO PUEDE VER SU CASO

    Funcionalidad: Este botón lleva a los clientes existentes a una página donde pueden buscar y ver su información.
    URL: /buscar-numero-caso/
    Descripción: Los clientes ingresan su número de caso para buscar y visualizar sus datos (usuario, contraseña y número de caso). Si el número de caso ingresado coincide con uno en la base de datos, se muestran los detalles correspondientes.

3. Contáctame Ahora

    Funcionalidad: Este botón redirige a una página con un formulario de contacto.
    URL: /crear-datos-contacto/
    Descripción: Permite a los usuarios ingresar su nombre, apellido, correo electrónico y teléfono para ponerse en contacto con la empresa. La información proporcionada se guarda en la base de datos, facilitando que el equipo de atención al cliente pueda responder a sus consultas.

4. Búsqueda Juicio por Número (usuarios logeados unicamente)

    Funcionalidad: Este botón permite a los usuarios buscar información sobre un juicio por número de caso.
    URL: /buscar-numero-caso/ (la misma URL que "Ya Soy Cliente")
    Descripción: Funciona de manera similar al botón "Ya Soy Cliente", permitiendo a los usuarios buscar información sobre juicios utilizando el número de caso proporcionado.

Detalles de Implementación

Modelos

    Cliente: Modelo que guarda la información del cliente, incluyendo el usuario, la contraseña y el número de caso.
    Datosdecontacto: Modelo que almacena la información de contacto de los usuarios interesados en contactar a la empresa.

Formularios

    ClienteFormulario: Utilizado para el registro de nuevos clientes.
    BuscarNumeroCasoForm: Utilizado para la búsqueda de clientes por número de caso.
    DatosdecontactoForm: Utilizado para el formulario de contacto.

Vistas

    form_con_api: Maneja el registro de nuevos clientes.
    buscar_numero_caso: Maneja la búsqueda de clientes por número de caso.
    crear_datos_contacto: Maneja el registro de datos de contacto.

Templates

    base.html: Plantilla base que proporciona la estructura común para todas las páginas.
    buscar_numero_caso.html: Muestra el formulario para buscar el número de caso y los resultados de la búsqueda.
    crear_datos_contacto.html: Muestra el formulario de contacto para que los usuarios puedan enviar consultas.

URLs

    Form-Con-Api: URL que dirige al formulario de registro de clientes.
    buscar_numero_caso: URL que dirige a la página de búsqueda de clientes por número de caso.
    crear-datos-contacto: URL que dirige al formulario de contacto.

Estructura y Navegación

La página de inicio está diseñada para facilitar la navegación hacia las funcionalidades principales de la aplicación. Los botones de la página ofrecen acceso intuitivo a las opciones de registro, búsqueda de información de clientes y contacto con la empresa.

En resumen, mi aplicación permite a los usuarios registrar nuevos clientes, buscar información sobre clientes existentes y enviar consultas a la empresa, proporcionando una experiencia de usuario completa y funcional.

Superusuario
usuario Test
email matias@abc.com
contraseña maradona

usuario comun
messi
contraseña 5587messi

usuario = models.IntegerField()
    contraseña= models.CharField(max_length=8)
    numero_de_caso= models.CharField(max_length=10)
