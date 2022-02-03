# User manual:
# ----------------------------------------------------------------------------------------------------------------
# Ohjelmaa käyttääksesi aktivoi Pythonin virtual environment terminaalissa
# Terminal -> New terminal tai Ctrl + Shift + ö
# Navigoi oikeaan kansioon: C:\Users\Kassa\Desktop\Korjaamotarjoukset 
# C:\Users\Kassa:sta oikeaan pääsee kahdella komennolla, "cd Desktop" ja "cd Korjaamotarjoukset" oikeaan kansioon.
# Vihje: "ls"-komento luettelee sen hetkisessä kansiossa olevat kansiot ja tiedostot. 
# "cd .."-komennolla pääsee "taaksepäin".
# ----------------------------------------------------------------------------------------------------------------
# Jos terminaalin rivin alussa ei vihreällä "(venv)", aktivoi virtual environment: 
# Kopioi ja liitä seuraavat komennot yksi kerrallaan terminaaliin. Aja komento Enterillä. 
# 1. Set-ExecutionPolicy Unrestricted -Scope Process
# 2. venv/Scripts/activate.ps1 
# 3. .\pdftoimg.py
# 4. Kopioi viikkotarjousten tiedoston nimi latauskansiosta ilman ".pdf"-päätettä, 
# eli juuri niin kuin kone sen automaattisesti maalaa, kun tiedoston nimeä muutetaan "Nimeä uudelleen"-komennolla.
# ----------------------------------------------------------------------------------------------------------------

import sys, fitz
from PIL import Image

#Lataa viikkotarjoukset-PDF ja copy-paste tiedostonimi.
pdfname = input('Kopioi PDF-tiedoston nimi: ')
path = "C:\\Users\\Kassa\\Downloads\\" + str(pdfname) + ".pdf"
doc = fitz.open(path)
# "Zoomataan" PDF paremman resoluution saavuttamiseksi, isompi luku = tarkempi resoluutio ja isompi tiedosto.
zoom_x = 2.0
zoom_y = 2.0
mat = fitz.Matrix(zoom_x, zoom_y)
# Loopataan jokainen PDF:n sivu. Jokaisesta oma kuvansa.
for page in doc:
    pix = page.get_pixmap(matrix=mat)
    pix.save("page-%i.png" % page.number)

# Avataan jokainen kuva, jotta ohjelma pääsee niihin käsiksi.
image0 = Image.open("page-0.png")
image1 = Image.open("page-1.png")
image2 = Image.open("page-2.png")
image3 = Image.open("page-3.png")

# Tallennetaan kuvien koko muuttujaan (jokainen luotu kuva on saman kokoinen).
image_size = image0.size

# Luodaan uusi tyhjä kuva, johon mahtuu kaksi luotua kuvaa vierekkäin.
new_image1 = Image.new('RGB', (2*image_size[0], image_size[1]), (250, 250, 250))

# Liitetään kaksi ensimmäistä kuvaa vierekkäin uuteen kuvaan.
new_image1.paste(image0, (0,0))
new_image1.paste(image1, (image_size[0],0))

# Tallennetaan muuttujaan sama kuva puolet pienempänä.
resized_im = new_image1.resize((round(new_image1.size[0]*0.5), round(new_image1.size[1]*0.5)))

# Toistetaan uuden tyhjän kuvan luominen, liitetään siihen kaksi jälkimmäistä kuvaa ja pienennetään sekin.
new_image2 = Image.new('RGB', (2*image_size[0], image_size[1]), (250, 250, 250))
new_image2.paste(image2, (0,0))
new_image2.paste(image3, (image_size[0],0))


resized_im1 = new_image2.resize((round(new_image2.size[0]*0.5), round(new_image2.size[1]*0.5)))

image_size2 = resized_im.size
new_image3 = Image.new('RGB', (image_size2[0], 2*image_size2[1]), (250, 250, 250))
new_image3.paste(resized_im, (0,0))
new_image3.paste(resized_im1, (0,image_size2[1]))
new_image3.save(pdfname+'.png', 'PNG')

