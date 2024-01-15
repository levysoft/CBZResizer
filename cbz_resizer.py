import os
import sys
import zipfile
from PIL import Image
import shutil
from pathlib import Path

def remove_temp_folder(temp_folder):
    """ Rimuove la cartella temporanea. """
    try:
        shutil.rmtree(temp_folder)
    except Exception as e:
        print(f"Errore durante la rimozione della cartella temporanea {temp_folder}: {e}")

def get_file_size_mb(file_path):
    """ Restituisce la dimensione del file in megabyte. """
    return os.path.getsize(file_path) / (1024 * 1024)

def update_progress_bar(total_images, processed_images):
    """ Aggiorna la barra di progresso della compressione delle immagini. """
    progress = processed_images / total_images * 20
    sys.stdout.write('\r')
    #sys.stdout.write(f"[{'='*int(progress)}] {processed_images / total_images * 100:.2f}%") # Barra di progresso che visualizza una barra di avanzamento più precisa con una percentuale formattata a due decimali.
    #sys.stdout.write("[%-20s] %d%%" % ('='*int(progress), processed_images / total_images * 100)) # Barra di avanzamento che riempie esattamente lo spazio di 20 caratteri, rendendo più chiaro visivamente quando il progresso ha raggiunto il 100%.
    sys.stdout.write(f"[{'='*int(progress)}{' '*(20-int(progress))}] {processed_images / total_images * 100:.2f}%") # Barra di progresso che riempie esattamente 20 caratteri, con percentuale di avanzamento formattata a due decimali

    sys.stdout.flush()

def compress_image(image_path, resize_factor):
    """ Comprime un'immagine ridimensionandola in base al fattore specificato. """
    with Image.open(image_path) as image:
        original_width, original_height = image.size
        new_width = int(original_width * resize_factor)
        new_height = int(original_height * resize_factor)
        resized_image = image.resize((new_width, new_height))
        resized_image.save(image_path)
    return original_width, original_height, new_width, new_height

def compress_cbz(input_cbz, output_cbz, compression_percentage):
    """ Comprime un file CBZ ridimensionando le immagini al suo interno. """
    temp_folder = Path('temp_folder')
    temp_folder.mkdir(exist_ok=True)

    with zipfile.ZipFile(input_cbz, 'r') as cbz_file:
        cbz_file.extractall(temp_folder, members=[f for f in cbz_file.infolist() if not f.filename.startswith('__MACOSX')])

    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']
    images = list(temp_folder.glob('**/*'))
    images = [img for img in images if img.suffix.lower() in image_extensions]
    total_images = len(images)
    processed_images = 0

    resize_factor = 1 - (compression_percentage / 100)

    last_original_width = last_original_height = 0
    last_new_width = last_new_height = 0

    for image_path in images:
        original_width, original_height, new_width, new_height = compress_image(image_path, resize_factor)
        last_original_width, last_original_height = original_width, original_height
        last_new_width, last_new_height = new_width, new_height
        processed_images += 1
        update_progress_bar(total_images, processed_images)

    with zipfile.ZipFile(output_cbz, 'w', zipfile.ZIP_DEFLATED) as new_cbz:
        for file in temp_folder.rglob('*'):
            new_cbz.write(file, file.relative_to(temp_folder))

    if output_cbz.exists():
        remove_temp_folder(temp_folder)

    print_size_info(input_cbz, output_cbz, last_original_width, last_original_height, last_new_width, last_new_height, compression_percentage)

def print_size_info(input_cbz, output_cbz, original_width, original_height, new_width, new_height, compression_percentage):
    """ Stampa le informazioni sulla dimensione originale e compressa del file CBZ. """
    original_file_size_mb = get_file_size_mb(input_cbz)
    new_file_size_mb = get_file_size_mb(output_cbz)
    print("\nRisoluzione".ljust(40) + "Dimensioni".rjust(30))
    print("=" * 70)
    print(f"Originale: {original_width}x{original_height}".ljust(40) + f"{original_file_size_mb:.2f} MB".rjust(30))
    print(f"Nuova: {new_width}x{new_height}".ljust(40) + f"{new_file_size_mb:.2f} MB".rjust(30))
    print(f"Percentuale di compressione: {compression_percentage}%".ljust(40))
    print("-" * 70)

def main():
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Usage: python3 cbz_resizer.py input.cbz [compression_percentage]")
        sys.exit(1)

    input_cbz = Path(sys.argv[1])
    output_cbz = input_cbz.with_name(f"{input_cbz.stem}_resize{input_cbz.suffix}")

    compression_percentage = 50
    if len(sys.argv) == 3:
        try:
            compression_percentage = int(sys.argv[2])
            if not 0 <= compression_percentage <= 100:
                raise ValueError
        except ValueError:
            print("La percentuale di compressione deve essere un numero tra 0 e 100.")
            sys.exit(1)

    compress_cbz(input_cbz, output_cbz, compression_percentage)

if __name__ == '__main__':
    main()
