# Instruções - App Clima

## Arquitetura do Projeto

API REST em Python Flask para consulta de informações meteorológicas, containerizada com Docker e usando MySQL para persistência.

**Stack:**
- Python 3.11 + Flask 3.0 (porta 5000)
- MySQL 8 (porta 3306)
- Docker Compose para orquestração

**Estrutura de Serviços:**
- `web`: Aplicação Flask (`api_clima`) - API REST
- `db`: MySQL (`mysql_clima`) - Persistência de histórico

## Padrões de Código

### Estrutura da Aplicação (`app.py`)

**Inicialização com retry automático:**
- Função `init_db()` tenta conectar ao MySQL por até 60 segundos (30 tentativas x 2s)
- Cria tabela `consultas_clima` automaticamente se não existir
- Pattern usado: retry loop com `time.sleep(2)` entre tentativas

**Rotas REST:**
- `GET /` - Informações da API e lista de endpoints
- `GET /health` - Health check (status da app + database)
- `GET /clima/<cidade>` - Consulta clima e salva no banco
- `GET /historico?limit=10` - Lista últimas N consultas
- `GET /historico/<cidade>?limit=10` - Histórico filtrado por cidade

**Conexão com banco:**
```python
DB_CONFIG = {
    'host': os.getenv('DB_HOST', 'db'),
    'cursorclass': pymysql.cursors.DictCursor  # Retorna dict ao invés de tupla
}
```

**Tratamento de erros:**
- API externa retorna 401: indica problema com `WEATHER_API_KEY`
- API externa retorna 404: cidade não encontrada
- Timeout configurado em 10s nas requisições HTTP

### Banco de Dados

**Tabela `consultas_clima`:**
```sql
id INT AUTO_INCREMENT PRIMARY KEY
cidade VARCHAR(100) NOT NULL
temperatura FLOAT
descricao VARCHAR(200)
umidade INT
data_consulta TIMESTAMP DEFAULT CURRENT_TIMESTAMP
INDEX idx_cidade (cidade)
INDEX idx_data (data_consulta)
```

## Workflows Essenciais

**Iniciar ambiente completo:**
```bash
docker-compose up -d --build
```

**Ver logs em tempo real:**
```bash
docker-compose logs -f web  # App Flask
docker-compose logs -f db   # MySQL
```

**Testar API rapidamente:**
```bash
./demo.sh  # Script de demonstração
python test-api.py  # Suite de testes completa
```

**Debug interativo:**
```bash
docker exec -it api_clima bash
docker exec -it mysql_clima mysql -u usuario -psenha projeto
```

**Parar e limpar:**
```bash
docker-compose down          # Para containers
docker-compose down -v       # Para + remove volumes (limpa banco)
```

## Dependências Críticas

**`requirements.txt` essenciais:**
- `cryptography==41.0.7` - OBRIGATÓRIA para autenticação MySQL sha256_password
- `pymysql==1.1.0` - Driver MySQL puro Python
- `Flask-CORS==4.0.0` - Habilita CORS para APIs externas

## Configuração Externa

**OpenWeatherMap API:**
- Requer `WEATHER_API_KEY` configurada no `docker-compose.yml`
- Gratuita em https://openweathermap.org/api (60 chamadas/minuto)
- Sem chave válida, endpoint `/clima/<cidade>` retorna 401

**Adicionar API Key:**
```yaml
# docker-compose.yml
services:
  web:
    environment:
      WEATHER_API_KEY: sua_chave_real_aqui
```

## Troubleshooting

**Erro "cryptography package required":**
- Falta `cryptography` no requirements.txt
- Rebuild necessário: `docker-compose up -d --build`

**App não conecta no MySQL:**
- Verificar se `depends_on: db` está no docker-compose
- Logs: `docker-compose logs db` para ver se MySQL iniciou
- Função `init_db()` tem retry automático (30 tentativas)

**Hot reload não funciona:**
- Verificar volume `.:/app` montado no docker-compose
- Flask em debug mode (`debug=True` no `app.run()`)

## Arquivos Importantes

- `app.py` - Aplicação Flask (core da API)
- `requirements.txt` - Dependências Python
- `Dockerfile` - Build da imagem (instala libmysqlclient-dev)
- `docker-compose.yml` - Orquestração dos serviços
- `test-api.py` - Suite de testes automatizados
- `demo.sh` - Script de demonstração rápida
- `README.md` - Documentação completa do usuário
