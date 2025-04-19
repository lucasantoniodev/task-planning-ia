# Serviço para estimativa de atividades com IA

## Instruções para execução do projeto

### 1º Criar ambiente virtual
    python -m venv .venv

### 2º Inciar ambiente virtual no terminal
    .\.venv\Scripts\activate 

### 3º Instalar dependências
    pip install -r requirements.txt

### 4º Rodar seeds
    python -m src.config.database.seeds

### 5º Treinar inteligência artificial
     python -m src.modules.artificial_intelligence.process.train

### 5º Iniciar servidor
    python main.py