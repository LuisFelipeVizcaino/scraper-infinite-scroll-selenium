from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd


# 1. Inicializamos el navegador con configuración correcta de pantalla
firefox_options = webdriver.FirefoxOptions()
firefox_options.add_argument("--headless")
# La sintaxis correcta para la ventana en Selenium es un método, no un argumento de texto
firefox = webdriver.Firefox(options=firefox_options)
firefox.set_window_size(1366, 768)
firefox.get("https://www.scrapingcourse.com/infinite-scrolling")
wait = WebDriverWait(firefox,10)
ultima_altura = firefox.execute_script("return document.body.scrollHeight")
while True:
    elementos_antes = len(firefox.find_elements(By.CLASS_NAME, "product-name"))
    firefox.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    wait.until(lambda d: len(d.find_elements(By.CLASS_NAME, "product-name")) > elementos_antes)
    nueva_altura = firefox.execute_script("return document.body.scrollHeight")
    if nueva_altura == ultima_altura:
        break
    ultima_altura = nueva_altura

lista_datos=[]
contendedor = firefox.find_elements(By.XPATH, "//div[@class='product-item flex flex-col items-center rounded-lg']")
for producto in contendedor:
    link_elem = producto.find_element(By.TAG_NAME, "a")
    link = link_elem.get_attribute("href")
    titulo= producto.find_element(By.XPATH, './/span[@class="product-name"]')
    precio= producto.find_element(By.XPATH, './/span[@class="product-price"]')
    lista_datos.append({"link": link, "titulo": titulo.text,"precio": precio.text})

df = pd.DataFrame(lista_datos)
print(f"Se extrajeron {len(df)} productos")

df.to_excel("productos_infinite_scroll.xlsx", index=False)
