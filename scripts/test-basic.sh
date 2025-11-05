#!/bin/bash
echo "=========================================="
echo "  🧪 TESTES BÁSICOS - SEM API KEY"
echo "=========================================="
echo ""

echo "1️⃣ Teste do endpoint principal:"
curl -s http://localhost:5000/ | python3 -m json.tool
echo ""

echo "=========================================="
echo "2️⃣ Teste do Health Check:"
curl -s http://localhost:5000/health | python3 -m json.tool
echo ""

echo "=========================================="
echo "3️⃣ Teste do Histórico:"
curl -s http://localhost:5000/historico | python3 -m json.tool
echo ""

echo "=========================================="
echo "4️⃣ Teste da API Key do OpenWeatherMap:"
curl -s "http://localhost:5000/clima/London" | python3 -m json.tool
echo ""

echo "=========================================="
echo "📝 NOTA: Se o teste 4 retornar 'API Key inválida',"
echo "aguarde 10-30 minutos para a chave ser ativada."
echo ""
echo "Mais info: https://openweathermap.org/faq#error401"
echo "=========================================="
