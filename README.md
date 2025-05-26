# PASID Validator (Python)
---

## 📌 Visão Geral

- Geração de dados simulados
- Balanceamento de carga entre múltiplos proxies
- Validação dos dados (simulada)
- Registro de resultados e tempo de resposta

---

## 🚀 Como Executar

1. Clone o repositório:

```bash
  git clone https://github.com/seu-usuario/Pasid-Validator-Python-main.git
  cd Pasid-Validator-Python-main
```

2. Rode os arquivos separadamente

```bash
  # Para rodar os serviços em suas respectivas portas e valor do service_time_ms
  #(o tempo do service_time_ms pode ser mudado)
  
  > python main.py service 3000 100
  > python main.py service 3001 100
  
  # Para rodar os load balances com suas respectivas portas 
  
  > python main.py load_balance 2000
  > python main.py load_balance 2100
  
  # Por fim, rodar o source
  
  > python main.py source
  
```
