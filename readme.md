# FastAPI con Esempi CRUD per la Tabella "Persona" 👤

Benvenuto nel nostro straordinario repository dedicato all'utilizzo di FastAPI per gestire operazioni CRUD (Create, Read, Update, Delete) sulla tabella "Persona". 🚀

## Introduzione

FastAPI è un framework moderno e veloce per la creazione di API con Python. In questo progetto, esploreremo come utilizzare FastAPI per gestire in modo elegante e coinvolgente le operazioni sulla nostra tabella "Persona".

## Setup Iniziale

1. Installa FastAPI eseguendo `pip install fastapi`.

2. Installa un server ASGI come uvicorn con `pip install uvicorn`.

3. Configura l'ambiente virtuale e installa le dipendenze con `pip install -r requirements.txt`.

## Esempi di Utilizzo

### 1. Creazione di una Nuova Persona

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Persona(BaseModel):
    nome: str
    età: int

@app.post("/crea_persona/")
async def crea_persona(persona: Persona):
    # Logica per aggiungere la persona al database
    return {"messaggio": "Persona creata con successo"}
```

### 2. Lettura di Tutte le Persone

```python
@app.get("/persone/")
async def leggi_persone():
    # Logica per leggere tutte le persone dal database
    return {"messaggio": "Lista di persone"}
```

### 3. Aggiornamento di una Persona

```python
@app.put("/aggiorna_persona/{persona_id}")
async def aggiorna_persona(persona_id: int, nuova_informazione: str):
    # Logica per aggiornare una persona nel database
    return {"messaggio": f"Persona {persona_id} aggiornata con successo"}
```

### 4. Cancellazione di una Persona

```python
@app.delete("/cancella_persona/{persona_id}")
async def cancella_persona(persona_id: int):
    # Logica per cancellare una persona dal database
    return {"messaggio": f"Persona {persona_id} cancellata con successo"}
```

## Contribuisci

Se hai idee o miglioramenti da suggerire, invia una pull request! 🎉

Grazie per essere parte di questa avventura con FastAPI e le operazioni CRUD sulla tabella delle Persone! 👥💻
