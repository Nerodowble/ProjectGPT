from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Configurar o WebDriver para o Microsoft Edge (não é necessário especificar o caminho do executável)
driver = webdriver.Chrome()

# Abrir a página
url = "https://bing.com/chat"
driver.get(url)

# Ler o conteúdo do arquivo input.txt
with open('input.txt', 'r', encoding='utf-8') as arquivo:
    texto_inserido = arquivo.read().strip()

# Aguarde alguns segundos (opcional)
time.sleep(10)  # Aguarde até 10 segundos para que a página seja carregada, se necessário

#Botão de aceitar os cookies (se necessário)
try:
    btn_cookies = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div[2]/div[2]/button[1]/a")
    btn_cookies.click()
except Exception as e:
    pass

time.sleep(10)
#JS para clicar em aceitar os termos de uso
try:
    driver.execute_script("""
    document.querySelector("#b_sydConvCont > cib-serp")
    .shadowRoot.querySelector("#cib-conversation-main")
    .shadowRoot.querySelector("#cib-chat-main > cib-chat-turn")
    .shadowRoot.querySelector("cib-message-group.response-message-group")
    .shadowRoot.querySelector("cib-message:nth-child(2)")
    .shadowRoot.querySelector("cib-shared > div > cib-muid-consent")
    .shadowRoot.querySelector("div.get-started-btn-wrapper-inline > button")
    .click();
    """)
    time.sleep(2)
except Exception as e:
    # Se o botão "Concordo com os termos" não estiver presente, clique diretamente no botão "Mais Preciso"
    driver.execute_script("""
    document.querySelector("#b_sydConvCont > cib-serp")
    .shadowRoot.querySelector("#cib-conversation-main")
    .shadowRoot.querySelector("#cib-chat-main > cib-welcome-container")
    .shadowRoot.querySelector("div.controls > cib-tone-selector")
    .shadowRoot.querySelector("#tone-options > li:nth-child(3) > button")
    .click();
    """)
time.sleep(3)
#JS para clicar no botão MAIS PRECISO depois que foi clicado em concordar com os termos.
driver.execute_script("""
    document.querySelector("#b_sydConvCont > cib-serp")
    .shadowRoot.querySelector("#cib-conversation-main")
    .shadowRoot.querySelector("#cib-chat-main > cib-welcome-container")
    .shadowRoot.querySelector("div.controls > cib-tone-selector")
    .shadowRoot.querySelector("#tone-options > li:nth-child(3) > button")
    .click();
    """)

#JS para clicar na caixa de texto
driver.execute_script(
    """
document
.querySelector("#b_sydConvCont > cib-serp")
.shadowRoot.querySelector("#cib-action-bar-main")
.shadowRoot.querySelector("div > div.main-container > div > div.input-row > cib-text-input")
.shadowRoot.querySelector("#searchbox")
.click();
"""
)
time.sleep(3)
driver.execute_script(
    f"""
    const shadowRoot1 = document.querySelector("#b_sydConvCont > cib-serp").shadowRoot;
    const shadowRoot2 = shadowRoot1.querySelector("#cib-action-bar-main").shadowRoot;
    const shadowRoot3 = shadowRoot2.querySelector("div > div.main-container > div > div.input-row > cib-text-input").shadowRoot;
    const searchbox = shadowRoot3.querySelector("#searchbox");

    // Inserindo texto na caixa de texto
    searchbox.value = "{texto_inserido}";

    // Disparando um evento de entrada para simular o comportamento do usuário
    const inputEvent = new Event('input', {{
        bubbles: true,
        cancelable: true,
    }});
    searchbox.dispatchEvent(inputEvent);
    """
)

time.sleep(3)

driver.execute_script(
    """
document
.querySelector("#b_sydConvCont > cib-serp")
.shadowRoot.querySelector("#cib-action-bar-main")
.shadowRoot.querySelector("div > div.main-container > div > div.bottom-controls > div.bottom-right-controls > div.control.submit > cib-icon-button")
.shadowRoot.querySelector("button").click();
"""
)

time.sleep(60)

# Obter a resposta usando JavaScript
resposta_element = driver.execute_script(
    """
    const shadowRoot1 = document.querySelector("#b_sydConvCont > cib-serp").shadowRoot;
    const shadowRoot2 = shadowRoot1.querySelector("#cib-conversation-main").shadowRoot;
    const shadowRoot3 = shadowRoot2.querySelector("#cib-chat-main > cib-chat-turn:nth-child(4)").shadowRoot;
    const responseMessageGroup = shadowRoot3.querySelector("cib-message-group.response-message-group").shadowRoot;
    const responseMessage = responseMessageGroup.querySelector("cib-message:nth-child(3)").shadowRoot;
    const respostaElement = responseMessage.querySelector("cib-shared > div");

    return respostaElement.innerText; // ou respostaElement.textContent;
    """
)

# Imprimir a resposta da requisição
print("Resposta da requisição: " + resposta_element)


# Fechar o navegador quando terminar
driver.quit()
