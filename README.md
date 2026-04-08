# 🤖 RPA - Monitoramento de Cotação de Moedas

![Python](https://img.shields.io/badge/Python-3.10-blue)
![RPA](https://img.shields.io/badge/RPA-BotCity-green)
![Automation](https://img.shields.io/badge/Automation-TaskScheduler-orange)
![Status](https://img.shields.io/badge/Status-Active-success)

Projeto de automação desenvolvido em **Python** utilizando **BotCity** para monitoramento automático da cotação de moedas.

O robô coleta periodicamente os valores do **Dólar, Euro e Real**, registra em uma base histórica Excel, gera dashboard e envia relatórios automáticos por email.

---

# 🚀 Funcionalidades

✔ Coleta automática de cotações
✔ Registro histórico em planilha Excel
✔ Dashboard automático
✔ Envio automático de relatório por email
✔ Execução automática via Agendador de Tarefas do Windows
✔ Execução via arquivo `.bat`
✔ Registro de logs de execução

---

# 💰 Moedas Monitoradas

| Moeda | Código |
| ----- | ------ |
| Dólar | USD    |
| Euro  | EUR    |
| Real  | BRL    |

---

# 🧠 Arquitetura do Projeto

```
cotacao-dolar-rpa
│
├── src
│   ├── main.py
│   ├── coletor_moedas.py
│   ├── excel_manager.py
│   └── email_sender.py
│
├── Database
│   └── dados_cotacoes.xlsx
│
├── logs
│   └── execucao.log
│
├── executar_rpa.bat
├── requirements.txt
├── README.md
└── .gitignore
```

---

# ⚙️ Tecnologias Utilizadas

* Python
* BotCity
* Pandas
* Requests
* OpenPyXL
* SMTP (envio de email)
* Windows Task Scheduler

---

# 📊 Fluxo da Automação

```
Agendador de Tarefas
        ↓
executar_rpa.bat
        ↓
Python (venv)
        ↓
main.py
        ↓
Coleta cotações
        ↓
Atualiza Excel + Dashboard
        ↓
Envia relatório por email
        ↓
Salva logs
```

---

# ⚙️ Como Executar o Projeto

## 1️⃣ Clonar repositório

```
git clone https://github.com/josetads/cotacao-dolar-rpa.git
```

## 2️⃣ Entrar na pasta

```
cd cotacao-dolar-rpa
```

## 3️⃣ Criar ambiente virtual

```
python -m venv venv
```

## 4️⃣ Ativar ambiente virtual

Windows:

```
venv\Scripts\activate
```

## 5️⃣ Instalar dependências

```
pip install -r requirements.txt
```

## 6️⃣ Executar o robô

```
python src/main.py
```

---

# 🖥️ Execução Automática (.bat)

O projeto utiliza um arquivo `.bat` para execução automática:

```
executar_rpa.bat
```

Exemplo:

```
@echo off
cd /d "C:\caminho\do\projeto"
"venv\Scripts\python.exe" "src\main.py"
```

---

# ⏰ Automação com Agendador de Tarefas

O robô é executado automaticamente utilizando o **Agendador de Tarefas do Windows**.

### Configuração:

* Programa/script:

```
executar_rpa.bat
```

* Frequência:

```
Diariamente
```

* Horários:

```
08:00
12:00
18:00
```

---

# 📈 Exemplo de Resultado

| Data             | Dólar | Euro | Real |
| ---------------- | ----- | ---- | ---- |
| 2026-03-30 18:00 | 5.23  | 5.67 | 1.00 |

Os dados são armazenados automaticamente na planilha Excel.

---

# 📧 Envio Automático por Email

Após cada execução o sistema envia automaticamente:

📊 cotações atualizadas
📎 planilha Excel em anexo

---

# 📂 Logs

As execuções são registradas em:

```
logs/execucao.log
```

---

# 🔒 Segurança

As credenciais de email devem ser configuradas via **variáveis de ambiente**, evitando exposição no código.

---

# 👨‍💻 Autor

José Oiris Inácio da Costa

Projeto desenvolvido para estudos em **Automação, Python e RPA com BotCity**.

---

# ⭐ Contribuição

Se este projeto foi útil, considere dar uma ⭐ no repositório.
