# CBZ Resizer
Script Python per ridimensionare efficientemente le immagini all'interno dei file CBZ con impostazioni di compressione personalizzabili, con supporto in sola lettura per i file CBR.

## Descrizione
CBZ Resizer è uno script Python sviluppato per ridimensionare le immagini all'interno dei file CBZ. Gli utenti possono specificare una percentuale di compressione per ridurre le dimensioni delle immagini, influenzando così la dimensione complessiva del file CBZ. Offre anche supporto in sola lettura per i file CBR a causa della limitazione della libreria rarfile, che è una libreria in sola lettura. Data questa limitazione e la focalizzazione primaria dello script sui file CBZ, il nome del progetto rimane "CBZ Resizer". Per i file CBR, lo script può decomprimere l'archivio RAR, ridimensionare le immagini come richiesto e ripacchettarle in un nuovo file CBZ.

## Funzionalità
- Ridimensionamento delle immagini in un file CBZ
- Supporto in sola lettura per i file CBR: decomprime i file CBR, ridimensiona le immagini e li converte in file CBZ
- Percentuale di compressione personalizzabile
- Output automatico con suffisso "_resize"

## Requisiti
- Python 3.x
- PIL (Python Imaging Library), installabile tramite `pip install Pillow`
- rarfile, installabile tramite `pip install rarfile` (necessario per il supporto CBR)

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

python3 cbz_resizer.py input_file [compression_percentage]

Dove `input_file` è il file CBZ o CBR da comprimere e `compression_percentage` è un valore opzionale che indica la percentuale di compressione (da 0 a 100, default 50%).

## File di Esempio per Test
Se hai bisogno di file CBZ o CBR di esempio per testare lo script CBZ Resizer, puoi scaricare file pre-costruiti dal seguente link: https://github.com/clach04/sample_reading_media/releases/. Questi file possono essere utili per testare le funzionalità di ridimensionamento e conversione dello script senza la necessità di utilizzare file di grandi dimensioni.

## Contributi
I contributi sono sempre benvenuti! Per contribuire al progetto, per favore segui questi passaggi:

1. Fork il repository.
2. Crea un nuovo branch: `git checkout -b nome_branch`.
3. Apporta le tue modifiche e commit: `git commit -am 'Aggiungi qualche cambiamento'`.
4. Push al branch: `git push origin nome_branch`.
5. Crea una pull request.

## Note
Questo script è stato creato per scopi educativi e non è garantito per l'uso in produzione.

## Crediti
Questo progetto è stato creato da Antonio Troise.

## Ringraziamenti
Un ringraziamento speciale a [clach04](https://github.com/clach04) per aver fornito file di esempio CBZ e CBR, disponibili per il download su [clach04/sample_reading_media/releases](https://github.com/clach04/sample_reading_media/releases/). Questi file di esempio sono estremamente utili per chiunque desideri testare le funzionalità di CBZ Resizer.

## Autore
Antonio Troise

## Licenza
Questo progetto è rilasciato sotto la licenza MIT. Vedi il file LICENSE per maggiori dettagli.
