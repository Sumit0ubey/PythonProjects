from PIL import Image
from os.path import basename
import glob


def Typeconversion(filePath, FromType:str, ToType:str, quality:int=90):
    """
    Converts the image from one file format to another. (eg., .jpg -> .png).\n
    It takes four argrument: "filePath", "quality", "FromType", "ToType".

    Args:\n
    filePath (str): The path to the image file.\n
    quality (int): The quality of the image after conversion.\n
    FromType (str): The original file format of the image.\n
    ToType (str): The target file format of the image.\n
    """

    filepath = filePath + "\\*." + FromType if filePath[-(len(FromType)+1)] != '.' else filePath
    for file in glob.glob(filepath):
        filename = basename(file)
        print(f"Converting {filename} to {filename[:-len(FromType)]}{ToType} .......")

        image = Image.open(file)
        colorSchema = image.convert('RGBA')
        colorSchema.save(file.replace(FromType, ToType), quality=quality)
        print("Conversion Completed..")

# Typeconversion(filePath=r"C:\image\imagetrans", FromType='jpg', ToType='png')

# Work is still going. There will be more features here
