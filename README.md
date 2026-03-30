# 🤖 RPA - Monitoramento de Cotação de Moedas

![Python](https://img.shields.io/badge/Python-3.10-blue)
![RPA](https://img.shields.io/badge/RPA-BotCity-green)
![Automation](https://img.shields.io/badge/Automation-TaskScheduler-orange)
![Status](https://img.shields.io/badge/Status-Active-success)

Projeto de automação desenvolvido em **Python** utilizando **BotCity** para monitoramento automático da cotação de moedas.

O robô coleta periodicamente os valores do **Dólar, Euro e Real**, registra em uma base histórica Excel e envia relatórios automáticos por email.

---

# 🚀 Funcionalidades

✔ Coleta automática de cotações  
✔ Registro histórico em planilha Excel  
✔ Envio automático de relatório por email  
✔ Execução automática via Task Scheduler  
✔ Automação estruturada com BotCity  

---

# 💰 Moedas Monitoradas

| Moeda | Código |
|------|------|
| Dólar | USD |
| Euro | EUR |
| Real | BRL |

---

# 🧠 Arquitetura do Projeto

cotacao-dolar-rpa
│
├── src
│ ├── main.py
│ ├── coletor_moedas.py
│ ├── excel_manager.py
│ └── email_sender.py
│
├── Database
│ └── dados_cotacoes.xlsx
│
├── requirements.txt
├── README.md
└── .gitignore


---

# ⚙️ Tecnologias Utilizadas

- Python
- BotCity
- Pandas
- Requests
- OpenPyXL
- SMTP Email
- Windows Task Scheduler

---

# 📊 Fluxo da Automação


Coletar Cotação
↓
Salvar Dados no Excel
↓
Atualizar Histórico
↓
Enviar Relatório por Email
↓
Executar Automaticamente


---

# ⚙️ Como Executar o Projeto

## 1️⃣ Clonar repositório


git clone https://github.com/josetads/cotacao-dolar-rpa.git


---

## 2️⃣ Entrar na pasta


cd cotacao-dolar-rpa


---

## 3️⃣ Criar ambiente virtual


python -m venv venv


---

## 4️⃣ Ativar ambiente virtual

Windows


venv\Scripts\activate


---

## 5️⃣ Instalar dependências


pip install -r requirements.txt


---

## 6️⃣ Executar o robô


python src/main.py


---

# 📈 Exemplo de Resultado

| Data | Dólar | Euro | Real |
|-----|-----|-----|-----|
| 2026-03-30 18:00 | 5.23 | 5.67 | 1.00 |

Os dados são armazenados automaticamente na planilha Excel.

---

# 📧 Envio Automático por Email

Após cada execução o sistema envia automaticamente um relatório contendo:

📊 cotações atualizadas  
📎 planilha Excel em anexo  

---

# ⏰ Automação

O projeto pode ser configurado para execução automática utilizando:

**Windows Task Scheduler**

Exemplo de horários:


08:00
12:00
18:00


---

# 🔒 Segurança

As credenciais de email podem ser configuradas utilizando **variáveis de ambiente** para evitar exposição de dados sensíveis.

---

# 👨‍💻 Autor

José Oiris Inácio da Costa  

Projeto desenvolvido para estudos em **Automação, Python e RPA com BotCity**.

---

# ⭐ Contribuição

Se este projeto foi útil para você, considere dar uma ⭐ no repositório.
Depois de atualizar

Execute no terminal:

git add README.md
git commit -m "README profissional"
git push
Resultado
