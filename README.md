El codigo de db.py implementa Singleton a travez de __new__ en la cual cada vez que se crea una instancia de la bdd devuelva siempre la misma
app.py importa flask y la clase de una instancia DB, crea ejemplos dentro de la bdd y inicia el servidor con debug


Al realizar una aplicacion web la conexion con las bases de datos puede conllevar una baja de rendimiento. Utilizando Singeton garantizamos que solo haya una instancia, evitando que se creen nuevas Al no crearse nuevas, mejora el rendimiento.

Como ejecutar: 

python -m venv venv

En windows:
venv\Scripts\activate

pip install -r requirements.txt

python app.py
