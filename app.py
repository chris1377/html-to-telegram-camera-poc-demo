from flask import Flask, request, jsonify, render_template_string
import os
import requests
import base64

app = Flask(__name__)

# Configurazione Sicura: Usa le variabili d'ambiente per i dati sensibili
# NON scrivere i token in chiaro nel codice sorgente!
BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')

@app.route('/', methods=['GET'])
def index():
    # Per semplicità, serviamo l'HTML dalla stessa app Flask
    # (Sostituisci questo blocco con 'render_template' se usi file HTML separati)
    with open('index.html', 'r', encoding='utf-8') as f:
        html_content = f.read()
    return render_template_string(html_content)

@app.route('/upload-photo', methods=['POST'])
def upload_photo():
    if not BOT_TOKEN or not CHAT_ID:
        print("Errore: Variabili d'ambiente Telegram non configurate.")
        return jsonify(success=False, error="Server misconfigured"), 500

    data = request.get_json()
    if not data or 'image' not in data:
        return jsonify(success=False, error="Invalid input"), 400

    # Pulisce l'intestazione Base64 per ottenere solo i dati dell'immagine
    image_data = data['image'].replace('data:image/png;base64,', '')
    
    # Definisce un nome file temporaneo
    filename = 'temp_photo.png'
    
    try:
        # 1. Salva temporaneamente l'immagine decodificando la stringa Base64
        with open(filename, 'wb') as f:
            f.write(base64.b64decode(image_data))
        
        # 2. Invia il file immagine a Telegram tramite le Bot API
        with open(filename, 'rb') as f:
            files = {'photo': f}
            response = requests.post(
                f'https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto',
                data={'chat_id': CHAT_ID}, 
                files=files
            )
            
        # 3. Gestione della risposta e pulizia
        if response.status_code == 200:
            return jsonify(success=True), 200
        else:
            print(f"Errore Telegram: {response.text}")
            return jsonify(success=False, error="Failed to send to Telegram"), 500
            
    except Exception as e:
        print(f"Errore interno: {e}")
        return jsonify(success=False, error="Internal server error"), 500
        
    finally:
        # Assicurati che il file temporaneo venga rimosso in ogni caso
        if os.path.exists(filename):
            os.remove(filename)

if __name__ == '__main__':
    # Esegui l'app. Avvertenza: debug=True non è sicuro per la produzione.
    app.run(host='0.0.0.0', port=5000, debug=True)
