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

### 4. Configure as variáveis de ambiente
Crie um arquivo `.env` na raiz do projeto:
```env
SECRET_KEY=sua_chave_secreta_aqui
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3
GOOGLE_MAPS_API_KEY=sua_chave_do_google_maps
EMAIL_HOST_USER=seu_email@exemplo.com
EMAIL_HOST_PASSWORD=sua_senha_de_app
```

### 5. Execute as migrações
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Execute o servidor de desenvolvimento
```bash
python manage.py runserver
```

O site estará disponível em `http://127.0.0.1:8000/`

## 📁 Estrutura do Projeto

```
manutencao-celular-site/
├── core/                   # App principal
│   ├── models.py          # Modelos de dados
│   ├── views.py           # Views/Controllers
│   ├── urls.py            # URLs do app
│   └── templates/         # Templates HTML
├── static/                # Arquivos estáticos
│   └── images/
├── media/                 # Upload de arquivos
├── requirements.txt       # Dependências
├── manage.py             # Script de gerenciamento Django
└── settings.py           # Configurações do projeto
```


### Adicionando Novos Serviços
- Acesse o admin Django em `/admin/`
```
```


⭐ Se este projeto foi útil para você, considere dar uma estrela no repositório!