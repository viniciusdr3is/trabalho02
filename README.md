<img width="1410" alt="image" src="https://github.com/user-attachments/assets/4df4f927-ceb3-4789-9d51-9399b22d3000" />


# 📱 Site de Manutenção de Celular e MacBook

Um site profissional desenvolvido em Django para uma empresa especializada em manutenção e reparo de dispositivos móveis e computadores Apple.

## 🚀 Sobre o Projeto

Este projeto é um site institucional completo para uma empresa de assistência técnica especializada em:
- Manutenção e reparo de smartphones
- Manutenção e reparo de MacBooks
- Venda de peças e acessórios
- Serviços técnicos especializados

## ✨ Funcionalidades

- **Página Inicial**: Apresentação da empresa e principais serviços
- **Sobre a Empresa**: História, missão, visão e valores da empresa
- **Produtos e Serviços**: Catálogo completo de serviços oferecidos
- **Contato**: Formulário de contato e informações de atendimento
- **Localização**: Mapa interativo e endereço da loja física

## 🛠️ Tecnologias Utilizadas

- **Backend**: Python 3.11 + Django
- **Frontend**: HTML5, CSS3, JavaScript
- **Banco de Dados**: SQLite (desenvolvimento) / PostgreSQL (produção)
- **Styling**: Bootstrap/CSS customizado
- **Maps**: Google Maps API para localização

## 📋 Pré-requisitos

- Python 3.8+
- pip (gerenciador de pacotes Python)
- Virtualenv (recomendado)

## 🔧 Instalação e Configuração

### 1. Abra o projeto .zip enviado no Visual Studio
```
```

### 2. Crie um ambiente virtual
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Execute as migrações
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Execute o servidor de desenvolvimento
```bash
python manage.py runserver
```

O site estará disponível em `http://127.0.0.1:8000/`
