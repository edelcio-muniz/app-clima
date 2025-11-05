# 🚀 Guia de Uso - API de Clima

## 📊 Status Atual

✅ **API configurada e rodando**
✅ **Banco de dados operacional**  
✅ **API Key configurada**
⏳ **Aguardando ativação da API Key** (10 min - 2 horas)

## 🔍 Monitoramento

O script `monitor-api-key.sh` está rodando em background e vai te avisar quando a API Key for ativada!

Para ver o status do monitoramento:
```bash
# Ver saída do monitoramento em tempo real
docker-compose logs -f web
```

## 🧪 Testes Disponíveis Agora

### 1. Teste Básico (sem necessidade de API Key)
```bash
./test-basic.sh
```

### 2. Demonstração
```bash
./demo.sh
```

### 3. Teste Manual dos Endpoints
```bash
# Informações da API
curl http://localhost:5000/

# Health Check
curl http://localhost:5000/health

# Histórico (vazio por enquanto)
curl http://localhost:5000/historico
```

## ✅ Quando a API Key for ativada

Você verá uma mensagem assim no terminal:
```
✅ API KEY ATIVADA! 🎉
```

Então poderá executar:

```bash
# Teste de clima para Londres
curl "http://localhost:5000/clima/London" | python3 -m json.tool

# Teste de clima para São Paulo
curl "http://localhost:5000/clima/Sao%20Paulo" | python3 -m json.tool

# Suite completa de testes
python test-api.py
```

## 🛠️ Comandos Úteis

```bash
# Ver logs da aplicação
docker-compose logs -f web

# Ver logs do banco de dados
docker-compose logs -f db

# Reiniciar aplicação
docker-compose restart web

# Parar tudo
docker-compose down

# Iniciar tudo novamente
docker-compose up -d
```

## 📝 Estrutura da Resposta da API (quando ativa)

```json
{
  "cidade": "London",
  "pais": "GB",
  "temperatura": 12.5,
  "sensacao_termica": 11.2,
  "temp_min": 10.0,
  "temp_max": 14.0,
  "umidade": 65,
  "descricao": "céu limpo",
  "vento": 3.5,
  "timestamp": "2025-11-05T03:15:00"
}
```

## ⏰ Timeline Esperada

- **Agora**: API configurada e rodando
- **10-30 min**: API Key provavelmente ativada
- **Até 2h**: Ativação garantida (tempo máximo)

## 🎯 Próximos Passos

Quando a API Key estiver ativa:

1. ✅ Testar consultas de clima
2. ✅ Ver histórico sendo populado
3. ✅ Experimentar diferentes cidades
4. 🚀 Considerar melhorias (cache, autenticação, etc.)

---

**Dica**: Deixe o script `monitor-api-key.sh` rodando em um terminal separado!
