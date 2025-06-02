# PASID Validator (Python)
---

## 📌 Visão Geral

- Geração de Dados Simulados: Cria pacotes de dados para processamento.
- Balanceamento de Carga: Distribui requisições recebidas para múltiplas instâncias de serviço de backend usando uma estratégia round-robin. Os balanceadores de carga podem ser configurados dinamicamente com uma lista de serviços ativos.
- Simulação de Serviço: Serviços de backend processam requisições, simulam trabalho (atraso configurável) e podem interagir com um serviço de IA externo (Groq).
- Integração com IA: Inclui um módulo (IA_service.py) para interagir com a API Groq, especificamente usando modelos como "gemma2-9b-it", apresentando mecanismos de retentativa manual para limites de taxa e erros de API.
- Logging de Desempenho: Registra informações detalhadas sobre cada mensagem processada, incluindo timestamps em vários estágios e Tempo Médio de Resposta (MRT) para cada mensagem e médias de ciclo.
- Implantação Conteinerizada: Utiliza Docker e docker-compose.yaml para configurar todo o ambiente, incluindo source, balanceadores de carga e múltiplas instâncias de serviço.
- Análise de Desempenho Automatizada: Um script Python (graphs/graficos.py) analisa o arquivo log.txt gerado para criar gráficos:
    Tempo Médio de Resposta (MRT) vs. Número de Serviços Ativos.
    Tempo Médio de Resposta (MRT) vs. Taxa de Geração de Mensagens (simulada).
- Experimentação Cíclica: O componente source pode executar experimentos em ciclos, variando o número de serviços de backend ativos para observar mudanças de desempenho.
- Configuração Dinâmica: Endereços de serviço para balanceadores de carga podem ser passados como argumentos de linha de comando ou atualizados via mensagens especiais durante a execução.

---


## 📁 Estruturação dos arquivos

```text
  Pasid-Validator-Python/
  │
  ├── main.py                      # Script principal para iniciar Source, Load Balancer ou Service
  ├── docker-compose.yaml          # Configuração Docker Compose para setup multi-container
  ├── requirements.txt             # Dependências Python
  ├── log.txt                      # Arquivo de log gerado com resultados (timestamps, status, MRT)
  ├── README.md                    # Este arquivo
  ├── .env.example                 # Exemplo de arquivo de ambiente (usuário deve criar .env)
  └── src/
      ├── abstract_proxy.py        # Classe base com funcionalidade de logging
      ├── config.py                # Configurações gerais do sistema
      ├── IA_service.py            # Serviço para interagir com a API de IA Groq
      ├── load_balance.py          # Implementação do Load Balancer (round-robin)
      ├── service.py               # Implementação da instância do Serviço de backend
      ├── source.py                # Nó Source: gera mensagens e orquestra experimentos
      └── utils.py                 # Funções utilitárias (ex: geração de timestamp)
  └── graphs/
      └── graficos.py              # Script para analisar log.txt e gerar gráficos de desempenho

```
## ⚙️ Pré-requisitos

- Python 3.x
- Docker e Docker Compose
- Chave API Groq: Para a funcionalidade do serviço de IA, você precisa de uma chave API da Groq.

## 🚀 Como Executar

1. Clone o repositório:

```bash
  git clone git@github.com:MarcosAndreLS/Pasid-Validator-Python.git
  cd Pasid-Validator-Python-main
```

2. Crie o arquivo .env
   
```text
  GROQ_API_KEY=sua_chave_api_groq_aqui
```

3. Executando com Docker Compose
   
O arquivo docker-compose.yaml está pré-configurado para executar todo o sistema com múltiplos serviços e balanceadores de carga.

- Iniciar o sistema:
  
```bash
  docker-compose up --build
```

- Visualizando Logs:
  
O Docker Compose irá exibir logs de todos os contêineres no console. Você também pode visualizar logs de serviços específicos:

```bash
  docker-compose logs -f source
  docker-compose logs -f loadbalancer1
  docker-compose logs -f service1
```

## 📊 Análise de Desempenho com graphs/graficos.py

O script graphs/graficos.py é usado para analisar o arquivo log.txt e gerar visualizações de desempenho.

1. Como Executar:

Navegue até o diretório raiz do projeto (ou certifique-se de que log.txt está no diretório pai de graphs/) e execute:

```bash
  python graphs/graficos.py
```

2. Gráficos Gerados:
   
O script salvará arquivos de gráfico PNG no diretório graphs/ (ou no diretório do script).

3. Dependências para graficos.py:
   
Certifique-se de que matplotlib está instalado (deve estar se requirements.txt for usado).

```bash
  pip install matplotlib
```

## 📊 Alguns Resultados...

<table>
  <tr>
    <td><img src="https://github.com/user-attachments/assets/77e05578-a1f1-45c2-93d1-848f15e14c16" alt="Gráfico com arrival_delay de 2000ms" width="500"></td>
    <td><img src="https://github.com/user-attachments/assets/8ef67cf5-c48c-4120-aa38-931dee182fab" alt="Gráfico com arrival_delay de 3000ms" width="500"></td>
  </tr>
</table>

