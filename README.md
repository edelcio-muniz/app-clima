# 🌤️ API de Clima

API REST em Flask para consulta de informações meteorológicas com armazenamento em banco de dados MySQL.

## 🚀 Funcionalidades

- ✅ Consulta de clima atual de qualquer cidade do mundo
- ✅ Armazenamento de histórico de consultas
- ✅ Endpoints REST bem documentados
- ✅ Containerização com Docker
- ✅ Banco de dados MySQL

## 📋 Requisitos

- Docker
- Docker Compose

## 🔧 Configuração

1. **Clone o repositório** (se aplicável)

2. **Configure a API Key do OpenWeatherMap** (opcional para testes básicos)
   - Crie uma conta gratuita em https://openweathermap.org/api
   - Obtenha sua API Key
   - Adicione no `docker-compose.yml` na seção `environment` do serviço `web`:
   ```yaml
   WEATHER_API_KEY: sua_chave_aqui
   ```

## 🏃 Como Executar

### Iniciar a aplicação
```bash
docker-compose up -d
```

### Ver logs
```bash
# Logs da aplicação
docker-compose logs -f web

# Logs do banco de dados
docker-compose logs -f db
```

### Parar a aplicação
```bash
docker-compose down
```

### Rebuild (após mudanças no código)
```bash
docker-compose up -d --build
```

## 📡 Endpoints da API

### `GET /`
Informações da API e lista de endpoints disponíveis

### `GET /health`
Health check da aplicação e status do banco de dados

### `GET /clima/<cidade>`
Obtém informações de clima atual de uma cidade

**Exemplo:**
```bash
curl http://localhost:5000/clima/São%20Paulo
```

**Resposta:**
```json
{
  "cidade": "São Paulo",
  "pais": "BR",
  "temperatura": 22.5,
  "sensacao_termica": 21.8,
  "temp_min": 20.0,
  "temp_max": 24.0,
  "umidade": 65,
  "descricao": "céu limpo",
  "vento": 3.5,
  "timestamp": "2025-11-04T10:30:00"
}
```

### `GET /historico?limit=10`
Retorna histórico das últimas consultas

**Parâmetros:**
- `limit` (opcional): número de registros a retornar (padrão: 10)

### `GET /historico/<cidade>?limit=10`
Retorna histórico de consultas de uma cidade específica

## 🧪 Testes

Execute o script de testes:

```bash
python test-api.py
```

Ou manualmente:

```bash
# Teste básico
curl http://localhost:5000/

# Teste health check
curl http://localhost:5000/health

# Teste consulta de clima
curl http://localhost:5000/clima/London

# Teste histórico
curl http://localhost:5000/historico
```

## 🗄️ Banco de Dados

O banco MySQL é inicializado automaticamente com a tabela `consultas_clima`:

- `id`: INT AUTO_INCREMENT (Primary Key)
- `cidade`: VARCHAR(100)
- `temperatura`: FLOAT
- `descricao`: VARCHAR(200)
- `umidade`: INT
- `data_consulta`: TIMESTAMP

## 🐳 Estrutura Docker

- **web**: Container da aplicação Flask (porta 5000)
- **db**: Container MySQL 8 (porta 3306)

## 📝 Notas

- A aplicação aguarda o MySQL estar pronto antes de iniciar (retry automático)
- Hot reload habilitado para desenvolvimento (volume montado)
- API Key demo incluída (limitada, recomenda-se obter uma própria)

## 🔐 Segurança

**⚠️ IMPORTANTE:** As credenciais do banco estão hardcoded no `docker-compose.yml` para desenvolvimento. Para produção:
- Use variáveis de ambiente em arquivo `.env`
- Nunca commite credenciais reais
- Configure secrets apropriados

## 🛠️ Tecnologias

- Python 3.11
- Flask 3.0
- MySQL 8
- Docker & Docker Compose
- PyMySQL
- Requests

## 📄 Licença

Projeto de exemplo para fins educacionais.
