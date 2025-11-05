from flask import Flask, jsonify, request
from flask_cors import CORS
import requests
import pymysql
import os
from datetime import datetime
import time

app = Flask(__name__)
CORS(app)

# Configurações do banco de dados
DB_CONFIG = {
    'host': os.getenv('DB_HOST', 'db'),
    'user': os.getenv('DB_USER', 'usuario'),
    'password': os.getenv('DB_PASSWORD', 'senha'),
    'database': os.getenv('DB_NAME', 'projeto'),
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor
}

# API Key gratuita da OpenWeatherMap (você deve criar sua própria em https://openweathermap.org/api)
WEATHER_API_KEY = os.getenv('WEATHER_API_KEY', 'demo')
WEATHER_API_URL = 'https://api.openweathermap.org/data/2.5/weather'

def get_db_connection():
    """Cria conexão com o banco de dados"""
    return pymysql.connect(**DB_CONFIG)

def init_db():
    """Inicializa o banco de dados com as tabelas necessárias"""
    max_retries = 30
    retry_count = 0
    
    while retry_count < max_retries:
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            
            # Criar tabela de consultas de clima
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS consultas_clima (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    cidade VARCHAR(100) NOT NULL,
                    temperatura FLOAT,
                    descricao VARCHAR(200),
                    umidade INT,
                    data_consulta TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    INDEX idx_cidade (cidade),
                    INDEX idx_data (data_consulta)
                )
            ''')
            
            conn.commit()
            cursor.close()
            conn.close()
            print("✅ Banco de dados inicializado com sucesso!")
            return True
        except pymysql.err.OperationalError as e:
            retry_count += 1
            print(f"⏳ Aguardando MySQL estar pronto... (tentativa {retry_count}/{max_retries})")
            time.sleep(2)
    
    print("❌ Erro: Não foi possível conectar ao banco de dados")
    return False

@app.route('/')
def home():
    """Rota principal com informações da API"""
    return jsonify({
        'message': 'API de Clima - Bem-vindo!',
        'endpoints': {
            '/': 'Informações da API',
            '/clima/<cidade>': 'Obter clima atual de uma cidade',
            '/historico': 'Ver histórico de consultas',
            '/historico/<cidade>': 'Ver histórico de uma cidade específica',
            '/health': 'Status da aplicação'
        },
        'versao': '1.0.0'
    })

@app.route('/health')
def health():
    """Endpoint de health check"""
    try:
        conn = get_db_connection()
        conn.close()
        db_status = 'ok'
    except:
        db_status = 'erro'
    
    return jsonify({
        'status': 'ok',
        'database': db_status,
        'timestamp': datetime.now().isoformat()
    })

@app.route('/clima/<cidade>')
def get_clima(cidade):
    """Obtém informações de clima para uma cidade"""
    try:
        # Fazer requisição para API do OpenWeatherMap
        params = {
            'q': cidade,
            'appid': WEATHER_API_KEY,
            'units': 'metric',
            'lang': 'pt_br'
        }
        
        response = requests.get(WEATHER_API_URL, params=params, timeout=10)
        
        if response.status_code == 401:
            return jsonify({
                'erro': 'API Key inválida. Configure WEATHER_API_KEY no docker-compose.yml',
                'dica': 'Obtenha uma chave gratuita em https://openweathermap.org/api'
            }), 401
        
        if response.status_code != 200:
            return jsonify({'erro': 'Cidade não encontrada'}), 404
        
        data = response.json()
        
        # Extrair informações relevantes
        clima_info = {
            'cidade': data['name'],
            'pais': data['sys']['country'],
            'temperatura': round(data['main']['temp'], 1),
            'sensacao_termica': round(data['main']['feels_like'], 1),
            'temp_min': round(data['main']['temp_min'], 1),
            'temp_max': round(data['main']['temp_max'], 1),
            'umidade': data['main']['humidity'],
            'descricao': data['weather'][0]['description'],
            'vento': data['wind']['speed'],
            'timestamp': datetime.now().isoformat()
        }
        
        # Salvar no banco de dados
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO consultas_clima (cidade, temperatura, descricao, umidade)
                VALUES (%s, %s, %s, %s)
            ''', (clima_info['cidade'], clima_info['temperatura'], 
                  clima_info['descricao'], clima_info['umidade']))
            conn.commit()
            cursor.close()
            conn.close()
        except Exception as e:
            print(f"Erro ao salvar no banco: {e}")
        
        return jsonify(clima_info)
    
    except requests.exceptions.Timeout:
        return jsonify({'erro': 'Timeout ao consultar API de clima'}), 504
    except Exception as e:
        return jsonify({'erro': f'Erro ao obter clima: {str(e)}'}), 500

@app.route('/historico')
def get_historico():
    """Retorna histórico de consultas"""
    try:
        limit = request.args.get('limit', 10, type=int)
        
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT id, cidade, temperatura, descricao, umidade, data_consulta
            FROM consultas_clima
            ORDER BY data_consulta DESC
            LIMIT %s
        ''', (limit,))
        
        consultas = cursor.fetchall()
        cursor.close()
        conn.close()
        
        # Formatar datas
        for consulta in consultas:
            consulta['data_consulta'] = consulta['data_consulta'].isoformat()
        
        return jsonify({
            'total': len(consultas),
            'consultas': consultas
        })
    
    except Exception as e:
        return jsonify({'erro': f'Erro ao buscar histórico: {str(e)}'}), 500

@app.route('/historico/<cidade>')
def get_historico_cidade(cidade):
    """Retorna histórico de consultas de uma cidade específica"""
    try:
        limit = request.args.get('limit', 10, type=int)
        
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT id, cidade, temperatura, descricao, umidade, data_consulta
            FROM consultas_clima
            WHERE cidade LIKE %s
            ORDER BY data_consulta DESC
            LIMIT %s
        ''', (f'%{cidade}%', limit))
        
        consultas = cursor.fetchall()
        cursor.close()
        conn.close()
        
        # Formatar datas
        for consulta in consultas:
            consulta['data_consulta'] = consulta['data_consulta'].isoformat()
        
        return jsonify({
            'cidade': cidade,
            'total': len(consultas),
            'consultas': consultas
        })
    
    except Exception as e:
        return jsonify({'erro': f'Erro ao buscar histórico: {str(e)}'}), 500

if __name__ == '__main__':
    print("🚀 Iniciando API de Clima...")
    if init_db():
        print("🌤️  API pronta! Acesse http://localhost:5000")
        app.run(host='0.0.0.0', port=5000, debug=True)
    else:
        print("❌ Falha ao inicializar banco de dados")
