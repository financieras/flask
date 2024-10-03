# Proyect Secret Number
## Descripción
Usamos:
    - Flask y peticiones HTTP
    - No usamos WebSockets
    
Creamos un juego muy sencillo para adivinar el número secreto.


## Configuración

**1. Clona el repositorio:**
```bash
git clone [https://github.com/tu_usuario/tu_repositorio.git](https://github.com/tu_usuario/tu_repositorio.git)
```

**2. Crea el archivo .env:**

Copia el archivo .env.example:

```bash
cp .env.example .env
```

**Reemplaza** `tu_clave_secreta_muy_segura` por una clave secreta fuerte: Puedes utilizar un generador de claves aleatorias como [enlace a un generador de claves aleatorias].

**3. Instala las dependencias:**

```bash
pip install -r requirements.txt
```

**4. Ejecuta la aplicación:**

```bash
flask run
```

**Generando una clave secreta segura**

Para generar una clave secreta aleatoria y segura, puedes utilizar el siguiente comando en tu terminal:

```bash
python -c 'import secrets; print(secrets.token_urlsafe(32))'
```

**Recomendaciones:**

* No publiques tu clave secreta en repositorios públicos.
* Rotar las claves periódicamente mejora la seguridad de tu aplicación.

**Contribuciones**
* ¡Las contribuciones son bienvenidas!
* Si encuentras algún error o quieres mejorar este proyecto, por favor, abre un issue o crea una pull request.

**Licencia**
* Este proyecto está licenciado bajo la licencia MIT. Consulta el archivo LICENSE para obtener más detalles. 