# Sistema de Cadastro de Alunos

## Desenvolvedores

* **Miguel Martins**
* **Karina Braga**

---

## Descrição

Este projeto implementa um sistema de gerenciamento de alunos utilizando **Python**, **pandas** e armazenamento em arquivo **CSV**.

O sistema permite:

* Inserir novos alunos
* Pesquisar por matrícula ou nome (case-insensitive)
* Editar dados do aluno (exceto matrícula)
* Remover registros com confirmação
* Utilizar uma interface Tkinter para facilitar o uso

---

## Requisitos

* **Python 3.8+**
* Biblioteca **pandas**

Para instalar as dependências, execute:

```bash
pip install pandas
```

---

## Como Executar

1. Baixe ou clone o repositório.
2. Abra o terminal na pasta do projeto.
3. Execute o comando:

```bash
python "Sistema De Alunos.py"
```

O arquivo `alunos.csv` será criado automaticamente caso não exista.

---

## Exemplo de Uso

* Clique em **Inserir Aluno** para adicionar um novo registro.
* Clique em **Pesquisar** e digite uma matrícula ou nome.
* Utilize as opções **Editar** e **Remover** conforme necessário.

---

## Commits

O uso correto de Git e GitHub faz parte da avaliação. Recomenda-se:

* Fazer **commits pequenos e frequentes**.
* Utilizar mensagens claras e diretamente relacionadas às mudanças, como:

  * "Adiciona função de pesquisa por nome"
  * "Corrige bug no cadastro de alunos"
  * "Implementa interface Tkinter"

### Histórico do Projeto

* **07/12** – Publicação inicial do sistema no modo terminal.
* **08/12** – Implementação da interface Tkinter.
* **09/12** – Correção dos erros entre Tkinter e manipulação do CSV.

---

Sistema concluído para fins acadêmicos e aberto para futuras melhorias.
