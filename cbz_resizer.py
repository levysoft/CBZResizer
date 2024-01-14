"""
CBZ Resizer

Descrizione:
Questo script ridimensiona le immagini all'interno di un file CBZ (formato di file usato per i fumetti digitali) 
modificandone la risoluzione in base a una percentuale di compressione specificata dall'utente.

Autore: Antonio Troise
Data: 14/01/2024
Versione: 1.0
Licenza: MIT

Utilizzo:
python3 cbz_resizer.py input.cbz [compression_percentage]

Dove `input.cbz` è il file CBZ da comprimere e `compression_percentage` è la percentuale opzionale di compressione 
(0-100, default 50%).

Installazione:
1. Clona o scarica il repository di 'CBZResizer'.

2. Naviga nella directory:
   cd CBZResizer

3. Crea un ambiente virtuale Python nella directory:
   python3 -m venv env

4. Attiva l'ambiente virtuale:
   source env/bin/activate

5. Installa i pacchetti richiesti:
   pip install -r requirements.txt
   oppure
   pip install Pillow

6. Esegui lo script:
   python3 cbz_resizer.py input.cbz 50
   
   Di default la percentuale di compressione è del 50%

7. Una volta terminato, disattiva l'ambiente virtuale:
   deactivate

"""

import os
import sys
import zipfile
from PIL import Image
import shutil

def remove_temp_folder(temp_folder):
    try:
        shutil.rmtree(temp_folder)
    except Exception as e:
        print(f"Errore durante la rimozione della cartella temporanea {temp_folder}: {str(e)}")

def get_file_size_mb(file_path):
    # Ottieni la dimensione del file in megabyte
    return os.path.getsize(file_path) / (1024 * 1024)

def update_progress_bar(total_images, processed_images):
    progress = processed_images / total_images * 20  # Calcola la percentuale di progresso
    sys.stdout.write('\r')
    sys.stdout.write("[%-20s] %d%%" % ('='*int(progress), processed_images / total_images * 100))
    sys.stdout.flush()

def compress_cbz(input_cbz, output_cbz, compression_percentage):
    # Crea una cartella temporanea per estrarre le immagini dal file .cbz
    temp_folder = 'temp_folder'
    os.makedirs(temp_folder, exist_ok=True)
    
    # Estrai il contenuto del file .cbz nella cartella temporanea
    with zipfile.ZipFile(input_cbz, 'r') as cbz_file:
        for file_info in cbz_file.infolist():
            if not file_info.filename.startswith('__MACOSX'):
                cbz_file.extract(file_info, temp_folder)

    # Lista di estensioni di file immagine supportate
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']

    # Calcola il numero totale di immagini
    total_images = sum([len(files) for _, _, files in os.walk(temp_folder) if any(file.lower().endswith(tuple(image_extensions)) for file in files)])
    processed_images = 0

    # Nella logica precedente del codice, la "percentuale di compressione" è utilizzata per ridimensionare la dimensione dell'immagine, e non per la compressione effettiva del file. Un valore di compressione del 90% riduce ciascuna dimensione dell'immagine del 10%, mentre un valore del 10% riduce ciascuna dimensione del 90%. Questo spiega perché una compressione impostata al 10% produce un file molto più piccolo rispetto a una compressione al 90%.
    # Per avere che una percentuale di compressione più alta significhi una riduzione maggiore della dimensione dell'immagine (e quindi un file più piccolo), devo calcolare il fattore di ridimensionamento come 1 - (compression_percentage / 100).
    # Con questo aggiornamento, una percentuale di compressione del 90% ridurrà significativamente la dimensione delle immagini (e del file), mentre una percentuale del 10% avrà un impatto molto minore sulle dimensioni
    # Calcola il fattore di ridimensionamento in base alla percentuale di compressione
    resize_factor = 1 - (compression_percentage / 100)

    # Ridimensiona le immagini nella cartella temporanea
    for root, _, files in os.walk(temp_folder):
        for file in files:
            file_extension = os.path.splitext(file)[-1].lower()
            if file_extension in image_extensions:
                image_path = os.path.join(root, file)
                try:
                    image = Image.open(image_path)
                    width, height = image.size
                    #new_width = int(width * (compression_percentage / 100))
                    #new_height = int(height * (compression_percentage / 100))
                    new_width = int(width * resize_factor)
                    new_height = int(height * resize_factor)
                    resized_image = image.resize((new_width, new_height))
                    resized_image.save(image_path)
                except Exception as e:
                    print(f"Errore durante l'apertura dell'immagine {image_path}: {str(e)}")
                processed_images += 1
                update_progress_bar(total_images, processed_images)
    
    # Comprimi nuovamente la cartella temporanea in un nuovo file .cbz
    with zipfile.ZipFile(output_cbz, 'w', zipfile.ZIP_DEFLATED) as new_cbz:
        for root, _, files in os.walk(temp_folder):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, temp_folder)
                new_cbz.write(file_path, arcname=arcname)

    # Elimina la cartella temporanea solo se il nuovo file CBZ è stato creato con successo
    if os.path.exists(output_cbz):
        remove_temp_folder(temp_folder)
        
    # Stampa la risoluzione originale e nuova di un campione di immagine (l'ultimo)
    original_file_size_mb = get_file_size_mb(input_cbz)
    new_file_size_mb = get_file_size_mb(output_cbz)
    print("\nRisoluzione".ljust(40) + "Dimensioni".rjust(30))
    print("=" * 70)
    print(f"Originale: {width}x{height}".ljust(40) + f"{original_file_size_mb:.2f} MB".rjust(30))
    print(f"Nuova: {new_width}x{new_height}".ljust(40) + f"{new_file_size_mb:.2f} MB".rjust(30))
    print(f"Percentuale di compressione: {compression_percentage}%".ljust(40))
    print("-" * 70)

if __name__ == '__main__':
     if len(sys.argv) < 2 or len(sys.argv) > 3:
         print("Usage: python3 cbz_resizer.py input.cbz [compression_percentage]")
         sys.exit(1)
    
     input_cbz = sys.argv[1]
    
     # Genera il nome del file di output aggiungendo "_resize" prima dell'estensione
     base_name, ext = os.path.splitext(input_cbz)
     output_cbz = f"{base_name}_resize{ext}"
    
     # Imposta il valore di default per la percentuale di compressione
     compression_percentage = 50
     if len(sys.argv) == 3:
         try:
             compression_percentage = int(sys.argv[2])
             if compression_percentage < 0 or compression_percentage > 100:
                 raise ValueError
         except ValueError:
             print("La percentuale di compressione deve essere un numero tra 0 e 100.")
             sys.exit(1)
    
     compress_cbz(input_cbz, output_cbz, compression_percentage)
