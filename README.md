# 🎓 Sistema de Cadastro de Alunos

Sistema desenvolvido para fins **educacionais**, com o objetivo de praticar conceitos fundamentais de programação em Python, organização de projetos e desenvolvimento colaborativo utilizando **Git e GitHub**.

O projeto simula um sistema simples de gerenciamento de alunos executado diretamente pelo terminal.

---

## 👥 Integrantes

O projeto foi desenvolvido por:

- **Kauan de Palma Cordeiro**
- **Gabriel de Souza Andrade**
- **Carlos Eduardo Santos de Araújo**

---

## 📋 Sobre o projeto

O **Sistema de Cadastro de Alunos** foi desenvolvido como atividade acadêmica para colocar em prática conceitos de programação e trabalho colaborativo.

A aplicação permite realizar operações básicas relacionadas ao gerenciamento de alunos diretamente pelo terminal.

Durante o desenvolvimento, cada integrante pôde trabalhar em diferentes funcionalidades utilizando **branches**, permitindo posteriormente a integração das alterações através de **merge**.

> ⚠️ **Observação:** atualmente, os dados utilizados pelo programa não são armazenados permanentemente. Ao encerrar a execução, as informações podem ser perdidas.

---

## ⚙️ Funcionalidades

O sistema possui as seguintes funcionalidades:

- 📝 **Cadastro de alunos**
  - Permite inserir informações de novos alunos no sistema.

- 🔎 **Consulta de alunos**
  - Permite consultar informações dos alunos cadastrados.

- 🗑️ **Exclusão de alunos**
  - Permite remover alunos cadastrados no sistema.

---

## 🛠️ Tecnologias utilizadas

As principais tecnologias e ferramentas utilizadas foram:

- **Python** — desenvolvimento da aplicação
- **Git** — controle de versão
- **GitHub** — armazenamento e colaboração no repositório
- **Visual Studio Code** — desenvolvimento e edição do código

---

## 📂 Estrutura do projeto

Exemplo da organização dos arquivos:

```text
sistema-cadastro-alunos/
│
├── Cadastro.py
├── Consulta.py
├── Exclusao.py
├── .gitignore
└── README.md
```

> A estrutura pode variar conforme a versão atual do projeto.

---

## ▶️ Como executar

### 1. Clone o repositório

```bash
git clone URL_DO_REPOSITORIO
```

### 2. Entre na pasta do projeto

```bash
cd sistema-cadastro-alunos
```

### 3. Verifique se o Python está instalado

```bash
python --version
```

Caso o comando acima não funcione, tente:

```bash
python3 --version
```

### 4. Execute o programa

```bash
python Cadastro.py
```

---

## 🌿 Desenvolvimento com Git

Durante o desenvolvimento, foram utilizadas branches para separar as funcionalidades do projeto.

Exemplo:

```text
main
│
├── Cadastro
├── Consulta
└── Exclusão
```

Cada funcionalidade pôde ser desenvolvida separadamente e posteriormente integrada à branch principal através de **merge**.

Exemplo:

```bash
git switch main
git merge Cadastro
git merge Consulta
git merge Exclusão
```

Depois da integração:

```bash
git push origin main
```

---

## 🎯 Objetivos de aprendizagem

Este projeto foi utilizado para praticar:

- Lógica de programação com Python
- Entrada e processamento de dados
- Organização de código
- Criação e gerenciamento de branches
- Commits e histórico de alterações
- Push e pull com repositórios remotos
- Merge entre branches
- Resolução de conflitos
- Desenvolvimento colaborativo com GitHub

---

## 📌 Status do projeto

**Em desenvolvimento acadêmico.**

Funcionalidades principais:

- [x] Cadastro de alunos
- [x] Consulta de alunos
- [x] Exclusão de alunos
- [x] Versionamento com Git
- [x] Desenvolvimento utilizando branches
- [x] Integração das funcionalidades
- [ ] Persistência permanente dos dados
- [ ] Interface gráfica

---

## 📚 Finalidade

Este projeto possui finalidade **exclusivamente educacional** e foi desenvolvido como parte do processo de aprendizagem de programação e versionamento de software.

---

### Desenvolvido por

**Kauan de Palma Cordeiro • Gabriel de Souza Andrade • Carlos Eduardo Santos de Araújo**