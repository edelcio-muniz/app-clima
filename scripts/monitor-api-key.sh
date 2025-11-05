#!/bin/bash
echo "🔍 Monitorando ativação da API Key do OpenWeatherMap..."
echo "⏰ Verificando a cada 30 segundos. Pressione Ctrl+C para parar."
echo ""

attempts=0
max_attempts=120  # 1 hora de tentativas (120 x 30s)

while [ $attempts -lt $max_attempts ]; do
    attempts=$((attempts + 1))
    current_time=$(date '+%H:%M:%S')
    
    echo -n "[$current_time] Tentativa $attempts: "
    
    # Fazer requisição e capturar apenas o código de status
    response=$(curl -s "http://localhost:5000/clima/London")
    
    # Verificar se contém erro
    if echo "$response" | grep -q '"erro"'; then
        echo "❌ API Key ainda não ativada"
    else
        echo "✅ API KEY ATIVADA! 🎉"
        echo ""
        echo "=========================================="
        echo "Resposta completa:"
        echo "$response" | python3 -m json.tool
        echo "=========================================="
        echo ""
        echo "✅ Sua API está pronta para uso!"
        echo "🧪 Execute os testes completos: python tests/test_api.py"
        exit 0
    fi
    
    # Aguardar 30 segundos antes da próxima tentativa
    sleep 30
done

echo ""
echo "⚠️  Limite de tentativas atingido (1 hora)."
echo "💡 A ativação pode levar até 2 horas. Execute o script novamente mais tarde."
