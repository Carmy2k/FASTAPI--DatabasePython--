# Titolo della descrizione
Salve
Per creare la tua applicazione hai solo bisogno di un milione di piccole cose da fare, che nell'ordine sono

* Scrivere un file *.sql : scrivi un file `PersonDB.sql` questo file conterrà le istruzioni sql da inserire nel tuo dbms di fiducia
* installare le tue dipendenze: crea un file requirements.txt nel quale scrivi una sotto l'altra tutte le dipendenze. Installa poi le dipendenze col comando
```bash
python -m pip install -r .\requirements.txt
```
* scrivi il tuo file `getConnection.py` questo particolare file ti permetterà di connetteerti al tuo dbms e cominciare con esso le diverse operazioni **CRUD** 
* per ogni entità scrivi una classe con PyDantic, inizia da `Person.py`
* scrivi un file html per il tuo personale templating, chiamalo `./templates/root.html`
* Disponi la tua speciale cartella per le immagini in `./static/src/image/`
