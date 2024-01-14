# CBZ Resizer
Script Python per ridimensionare in modo efficiente le immagini all'interno dei file CBZ con impostazioni di compressione personalizzabili

## Descrizione
CBZ Resizer è uno script Python progettato per ridimensionare le immagini all'interno di file CBZ. L'utente può specificare una percentuale di compressione per ridurre le dimensioni delle immagini, influenzando così la dimensione complessiva del file CBZ.

## Funzionalità
- Ridimensionamento delle immagini in un file CBZ
- Percentuale di compressione personalizzabile
- Output automatico con suffisso "_resize"

## Requisiti
- Python 3.x
- PIL (Python Imaging Library), installabile tramite `pip install Pillow`

## Installazione
Per configurare l'ambiente di sviluppo:

1. Clona il repository:

git clone https://github.com/levysoft/CBZResizer/

2. Entra nella directory del progetto:

cd CBZResizer

3. Crea un ambiente virtuale Python:

python3 -m venv venv

4. Attiva l'ambiente virtuale:

- Su Windows:
  ```
  .\venv\Scripts\activate
  ```
- Su Unix o MacOS:
  ```
  source venv/bin/activate
  ```
5. Installa le dipendenze:

pip install -r requirements.txt


## Utilizzo
Per utilizzare lo script, eseguire il comando:

python3 cbz_resizer.py input.cbz [compression_percentage]

Dove `input.cbz` è il file CBZ da comprimere e `compression_percentage` è un valore opzionale che indica la percentuale di compressione (da 0 a 100, default 50%).

## Contributing
Le contribuzioni sono sempre benvenute! Per contribuire al progetto, per favore segui questi passaggi:

1. Fork il repository.
2. Crea un nuovo branch: `git checkout -b nome_branch`.
3. Apporta le tue modifiche e commit: `git commit -am 'Aggiungi qualche cambiamento'`.
4. Push al branch: `git push origin nome_branch`.
5. Crea una pull request.

## Note
Questo script è stato creato per scopi educativi e non è garantito per l'uso in produzione.

## Credits
Questo progetto è stato creato da Antonio Troise.

## Acknowledgements
Ringraziamenti speciali a chiunque contribuisca a questo progetto.

## Autore
Antonio Troise

## Licenza
Questo progetto è rilasciato sotto la licenza MIT. Vedi il file LICENSE per maggiori dettagli.
