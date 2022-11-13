# Talana Kombat JRPG
Talana Kombat es un juego donde 2 personajes se enfrentan hasta la muerte. Cada personaje tiene 2 golpes especiales que se ejecutan con una combinación de movimientos + 1 botón de golpe.

## Botones
- **Movimientos** (W)Arriba, (S)Abajo, (A)Izquierda, (D)Derecha
- **Golpes** (P)Puño, (K)Patada

## Specials
| Tony        | Tony    | Tony  
| ----------- | ------- | -------------
| Combinación | Energía | Nombre  
| DSD + P     | 3       | Taladoken  
| SD + K      | 2       | Remuyuken  
| P o K       | 1       | Puño o Patada  

| Araldor     | Araldor | Araldor  
| ----------- | ------- | -------------
| Combinación | Energía | Nombre  
| SA + K      | 3       | Remuyuken  
| ASA + P     | 2       | Taladoken  
| P o K       | 1       | Puño o Patada


# Instalacion

## Usando env
- Crea un entorno
```
python -m venv .env
```
- Activa el entorno
```
source .env/bin/activate
```
- Instala las dependencias
```
pip3 install -r requirements/base.txt
```
- Ejecuta el proyecto
```
uvicorn app.main:app --reload
```
- Visita http://127.0.0.1:8000/docs para que puedas jugar con el

## Usando docker compose
- Inicia Docker
- Ejecuta
```
 docker-compose up
```
- Visita http://127.0.0.1:8080/docs para que puedas jugar con el

## Usando Make file
- Build
```
make build
```
- Run en local
```
make run.local
```
Visita http://127.0.0.1:8181/docs para que puedas jugar con el

# Test
Luego de haber instalado el proyecto con env ejecuta
```
pytest -s -v
```

Con makefiole
```
make build.tests
```
luego
```
make test.local
```

## Preguntas generales
1. Supongamos que en un repositorio GIT hiciste un commit y olvidaste un archivo. Explica cómo se soluciona si hiciste push, y cómo si aún no hiciste.
De ser posible, que quede solo un commit con los cambios.
- Si no he hecho pus puedo hacer uso de primero añadir el archivo con git add achivo y luego usar git commit --amend para añadirlo al ultimo comit
- Si ya hice push a master,  agrego un nuevo commit donde el mensaje inciia con FIX
2. Si has trabajado con control de versiones ¿Cuáles han sido los flujos con los que has trabajado?
 - He trabajado dde la siguiente manera cada Feature una rama, que se mergea con qa, luego de probar que todo bien qa se mergea con master
3. ¿Cuál ha sido la situación más compleja que has tenido con esto?
- Se nos han pasado a master bugs que olvidamos probar en qa
4. ¿Qué experiencia has tenido con los microservicios?:
- He trabajado creando microservicios en diferentes frameworks de python, cada uno usando su propio servidor y database gestionados por kubernetes
5. ¿Cuál es tu servicio favorito de GCP o AWS? ¿Por qué?
- De AWS step functions ya que me permite encadenar lambdas de acuerdo  a condiciones preestablecidad
- De GCP App Engine porque es barato (Si no hay mucho flujo xD) y BigQuery ya que siendo una base de datos columnar me permite hacer querys sql
