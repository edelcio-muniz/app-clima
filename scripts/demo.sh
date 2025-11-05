#!/bin/bash

echo "=========================================="
echo "  🌤️  DEMO API DE CLIMA"
echo "=========================================="
echo ""

echo "📍 1. Informações da API:"
curl -s http://localhost:5000/ | python3 -m json.tool
echo ""

echo "=========================================="
echo "💚 2. Health Check:"
curl -s http://localhost:5000/health | python3 -m json.tool
echo ""

echo "=========================================="
echo "📊 3. Histórico de Consultas:"
curl -s http://localhost:5000/historico | python3 -m json.tool
echo ""

echo "=========================================="
echo "✅ API está funcionando corretamente!"
echo ""
echo "📝 Para usar consultas de clima reais:"
echo "   1. Obtenha uma API Key em: https://openweathermap.org/api"
echo "   2. Adicione no docker-compose.yml:"
echo "      environment:"
echo "        WEATHER_API_KEY: sua_chave_aqui"
echo "   3. Execute: docker-compose up -d --build"
echo ""
echo "🧪 Endpoints disponíveis:"
echo "   GET  /                    - Informações da API"
echo "   GET  /health              - Status da aplicação"
echo "   GET  /clima/<cidade>      - Clima de uma cidade"
echo "   GET  /historico           - Histórico de consultas"
echo "   GET  /historico/<cidade>  - Histórico de uma cidade"
echo "=========================================="
