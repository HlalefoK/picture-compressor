import os
import cv2
import pandas as pd

# Function to resize images
def resize_images(folder_path):

    for filename in os.listdir(folder_path):

        if filename.endswith(".jpg") or filename.endswith(".png"):  # checking to take the images that end with both png and jpg
            
            image_path = os.path.join(folder_path, filename)
            img = cv2.imread(image_path)
            resized_img = cv2.resize(img, (300, 300))
            cv2.imwrite(image_path, resized_img)
            print(f"Resized {filename} to 300x300")


# Function to add Pokémon names to images
def add_pokemon_names(folder_path, dataset_path):

    dataset = pd.read_csv(dataset_path)

    for filename in os.listdir(folder_path):

        if filename.endswith(".jpg") or filename.endswith(".png"):
            
            image_path = os.path.join(folder_path, filename)
            pokemon_id = int(filename.split('.')[0])  # Extract Pokémon ID from the filename
            pokemon_name = dataset.loc[pokemon_id - 1, 'Name']  # Adjusting index to match Pokémon ID
            img = cv2.imread(image_path)
            cv2.putText(img, pokemon_name, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
            cv2.imwrite(image_path, img)
            print(f"Added {pokemon_name} to {filename}")


if __name__ == "__main__":
    
    folder_path = ".\images"
    dataset_path = ".\pokemon.csv"
    
    resize_images(folder_path)
    add_pokemon_names(folder_path, dataset_path)
