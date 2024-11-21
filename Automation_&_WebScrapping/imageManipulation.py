from PIL import Image # type: ignore
from os import path
import glob


def Typeconversion(filePath:str, FromType:str, ToType:str, quality:int=100):
    """
    Converts the image from one file format to another. (eg., .jpg -> .png).\n
    It takes four argrument: "filePath", "quality", "FromType", "ToType".

    Args:\n
    filePath (str): The path to the image file.\n
    quality (int): The quality of the image after conversion.\n
    FromType (str): The original file format of the image.\n
    ToType (str): The target file format of the image.\n
    """

    # filepath = filePath + "\\*." + FromType if filePath[-(len(FromType)+1)] != '.' else filePath  # only works for windows..
    filepath = path.join(filePath, f"*.{FromType.lower()}") if path.isfile(filePath) != True else filePath  # works on any OS..
    if not filepath:
        print(f"No files with extension '{FromType}' found in '{filePath}'")
        return
    
    for file in glob.glob(filepath):
        filename = path.basename(file)
        print(f"Converting {filename} to {filename[:-len(FromType)]}{ToType} .......")
        try:
            image = Image.open(file)
            colorSchema = image.convert('RGBA')
            colorSchema.save(file.replace(FromType, ToType), quality=quality)
            print("Conversion Completed..")
        except Exception as e:
            print(f"Failed to convert {filename} : {e}")

# Typeconversion(filePath=r"C:\image\imagetrans", FromType='jpg', ToType='png')


def Sizecompression(filePath: str, mode: str, quality: int = 75):
    """
    Compresses image files in a directory or a specific file based on the provided mode and quality.

    Parameters:
        filePath (str): Path to the file or directory containing images.
        mode (str): File extension of the images ('jpg', 'png', 'webp', etc.).
        quality (int): Compression quality (1-100 for lossy formats, 0-9 for PNG).

    Returns:
        None
    """

    if path.isfile(filePath):
        files = [filePath]
    else:
        pattern = path.join(filePath, f"*.{mode.lower()}")
        files = glob.glob(pattern)

    if not files:
        print(f"No files with extension '{mode}' found in '{filePath}'")
        return

    for file in files:
        filename = path.basename(file)
        print(f"Compressing {filename} .......")
        try:
            image = Image.open(file)
            if mode.lower() in ['jpg', 'jpeg']:
                image.save(file, quality=quality, optimize=True, progressive=True)
            elif mode.lower() == 'png':
                compression_level = max(0, min(9, quality // 11))  # Maping 1-100 to 0-9
                image.save(file, optimize=True, compress_level=compression_level)
            elif mode.lower() == 'webp':
                image.save(file, format="WEBP", quality=quality, lossless=(quality == 100))
            else:
                image.save(file, quality=quality)
            print(f"Compression for {filename} completed.")
        except Exception as e:
            print(f"Failed to compress {filename}: {e}")

# # Work is still going. There will be more features here
