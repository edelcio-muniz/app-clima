#!/usr/bin/env python3
"""
Script para testar a API de Clima
"""

import requests
import json
from time import sleep

BASE_URL = 'http://localhost:5000'

def print_separator():
    print("\n" + "="*60 + "\n")

def test_home():
    """Testa endpoint principal"""
    print("🏠 Testando endpoint HOME...")
    response = requests.get(f'{BASE_URL}/')
    print(f"Status: {response.status_code}")
    print(json.dumps(response.json(), indent=2, ensure_ascii=False))
    return response.status_code == 200

def test_health():
    """Testa health check"""
    print("💚 Testando HEALTH CHECK...")
    response = requests.get(f'{BASE_URL}/health')
    print(f"Status: {response.status_code}")
    print(json.dumps(response.json(), indent=2, ensure_ascii=False))
    return response.status_code == 200

def test_clima(cidade):
    """Testa consulta de clima"""
    print(f"🌤️  Testando CLIMA para {cidade}...")
    response = requests.get(f'{BASE_URL}/clima/{cidade}')
    print(f"Status: {response.status_code}")
    print(json.dumps(response.json(), indent=2, ensure_ascii=False))
    return response.status_code == 200

def test_historico():
    """Testa histórico de consultas"""
    print("📋 Testando HISTÓRICO...")
    response = requests.get(f'{BASE_URL}/historico?limit=5')
    print(f"Status: {response.status_code}")
    data = response.json()
    print(f"Total de consultas: {data.get('total', 0)}")
    if data.get('consultas'):
        print("Últimas consultas:")
        for consulta in data['consultas'][:3]:
            print(f"  - {consulta['cidade']}: {consulta['temperatura']}°C - {consulta['descricao']}")
    return response.status_code == 200

def test_historico_cidade(cidade):
    """Testa histórico de uma cidade específica"""
    print(f"📍 Testando HISTÓRICO de {cidade}...")
    response = requests.get(f'{BASE_URL}/historico/{cidade}')
    print(f"Status: {response.status_code}")
    data = response.json()
    print(f"Total de consultas para {cidade}: {data.get('total', 0)}")
    return response.status_code == 200

def main():
    """Executa todos os testes"""
    print("\n" + "🧪 INICIANDO TESTES DA API DE CLIMA ".center(60, "=") + "\n")
    
    tests_passed = 0
    tests_total = 0
    
    # Aguardar API estar pronta
    print("⏳ Aguardando API estar disponível...")
    max_retries = 10
    for i in range(max_retries):
        try:
            requests.get(f'{BASE_URL}/', timeout=2)
            print("✅ API disponível!\n")
            break
        except:
            if i == max_retries - 1:
                print("❌ API não está respondendo. Verifique se está rodando.")
                return
            sleep(2)
    
    # Teste 1: Home
    print_separator()
    tests_total += 1
    if test_home():
        tests_passed += 1
    
    # Teste 2: Health
    print_separator()
    tests_total += 1
    if test_health():
        tests_passed += 1
    
    # Teste 3: Clima - São Paulo
    print_separator()
    tests_total += 1
    if test_clima('São Paulo'):
        tests_passed += 1
    
    sleep(1)
    
    # Teste 4: Clima - Rio de Janeiro
    print_separator()
    tests_total += 1
    if test_clima('Rio de Janeiro'):
        tests_passed += 1
    
    sleep(1)
    
    # Teste 5: Clima - Londres
    print_separator()
    tests_total += 1
    if test_clima('London'):
        tests_passed += 1
    
    sleep(1)
    
    # Teste 6: Histórico geral
    print_separator()
    tests_total += 1
    if test_historico():
        tests_passed += 1
    
    # Teste 7: Histórico de São Paulo
    print_separator()
    tests_total += 1
    if test_historico_cidade('São Paulo'):
        tests_passed += 1
    
    # Resumo
    print_separator()
    print(f"{'RESUMO DOS TESTES'.center(60)}")
    print(f"\n✅ Testes passou: {tests_passed}/{tests_total}")
    
    if tests_passed == tests_total:
        print("\n🎉 Todos os testes passaram com sucesso!")
    else:
        print(f"\n⚠️  {tests_total - tests_passed} teste(s) falharam")
    
    print_separator()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Testes interrompidos pelo usuário")
    except Exception as e:
        print(f"\n❌ Erro ao executar testes: {e}")
