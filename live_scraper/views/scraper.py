import json
import atexit
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from django.shortcuts import render
from django.http import JsonResponse, HttpResponseBadRequest
from live_scraper.models import LiveInfo  # Modelo atualizado para armazenar JSON
import time

# Lista global para acumular coletas (pode ser substituída por um cache)
collected_data = []
live_title = ""  # Variável global para armazenar o título da live
live_platform = ""  # Variável global para armazenar a plataforma da live


# Função para salvar os dados restantes ao encerrar o servidor ou script
def save_collected_data_on_exit():
    global collected_data, live_title, live_platform
    if collected_data:
        LiveInfo.objects.create(
            title=live_title,
            platform=live_platform,
            json_data=collected_data,
        )
        print(
            f"\nDados restantes salvos automaticamente antes do encerramento: {len(collected_data)} coletas.\n"
        )
        collected_data = []  # Limpa a lista


# Registra a função para ser executada quando o script encerrar
atexit.register(save_collected_data_on_exit)


def live_scraper(request):
    global collected_data, live_title, live_platform  # Para manter os dados entre as execuções

    if request.method == "POST":
        live_url = request.POST.get("live_url")  # Captura a URL enviada pelo formulário
        if not live_url:
            return HttpResponseBadRequest("A URL da live é obrigatória.")

        # Configuração do ChromeDriver
        driver_path = (
            "C:\\Users\\Marcos\\Desktop\\PROJETO - Numbers\\drivers\\chromedriver.exe"
        )
        chrome_options = Options()
        chrome_options.add_argument("--headless")

        # Inicializando o WebDriver
        driver = webdriver.Chrome(service=Service(driver_path), options=chrome_options)

        try:
            print("\n------------------------")
            print("\nIniciando coleta de dados...\n")
            # Navega para a URL fornecida
            driver.get(live_url)

            # Espera a página carregar e o elemento aparecer
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//div[@data-e2e='user-profile-live-title']")
                )
            )

            # Coleta as informações da live
            live_platform = "Tiktok"  # Aqui, definimos a plataforma
            live_title = driver.find_element(
                By.XPATH, "//div[@data-e2e='user-profile-live-title']"
            ).text
            views = driver.find_element(
                By.XPATH, "//div[@data-e2e='live-people-count']"
            ).text
            likes = driver.find_element(
                By.XPATH, "//div[@class='css-i3v4z1-DivLikeCount exkv4261']"
            ).text

            print(f"\nPlataforma: {live_platform}")
            print(f"Título: {live_title}")
            print(f"Visualizações: {views}")
            print(f"Likes: {likes}\n")

            # Adiciona os dados coletados na lista
            collected_data.append(
                {
                    "views": views,
                    "likes": likes,
                    "scraped_at": time.strftime("%Y-%m-%d %H:%M:%S"),  # Timestamp atual
                }
            )
            print(f"Dados coletados: {len(collected_data)}\n")
            print("------------------------\n")

            # Verifica se a quantidade de coletas atingiu 50 ou mais
            if len(collected_data) >= 50:
                # Salva o lote no banco de dados com título e plataforma fora do JSON
                LiveInfo.objects.create(
                    title=live_title, platform=live_platform, json_data=collected_data
                )
                print(
                    f"\nLote salvo no banco de dados com {len(collected_data)} coletas.\n"
                )
                collected_data = []  # Reseta a lista após o salvamento

        except Exception as e:
            print("Erro durante a coleta de dados:", str(e))

            # Salva o JSON imediatamente se ocorrer um erro
            if collected_data:
                LiveInfo.objects.create(
                    title=live_title, platform=live_platform, json_data=collected_data
                )
                print(
                    f"Lote salvo no banco de dados após erro com {len(collected_data)} coletas."
                )
                collected_data = []  # Reseta a lista após o salvamento

        finally:
            # Fecha o navegador
            driver.quit()

        return render(request, "lives_scraper/live_dashboard.html")

    return HttpResponseBadRequest("Método não suportado.")
