# # AI Code Reviewer

Uma aplicação serverless de revisão de código utilizando **Amazon Bedrock** e **AWS Step Functions**.

O projeto recebe um trecho de código-fonte, executa um pipeline de análise automatizada e gera um relatório de revisão utilizando um modelo de inteligência artificial.

---

# Arquitetura


O fluxo da aplicação:

```
User Input
    |
    v
AWS Step Functions
    |
    +----------------+
    |                |
    v                v
Validate Code   Analyze Code
 Lambda            Lambda
                      |
                      v
               Amazon Bedrock
                      |
                      v
               Generate Report
                   Lambda
                      |
                      v
                Final Review
```

---

# Como funciona

## 1. Validate Code

A primeira etapa valida a entrada recebida pelo sistema.

Responsabilidades:

* verificar se o código foi enviado;
* verificar a linguagem informada;
* interromper o fluxo caso os dados sejam inválidos.

Exemplo de entrada:

```json
{
  "language": "python",
  "code": "def soma(a,b): return a+b"
}
```

---

## 2. Analyze Code (Amazon Bedrock)

A segunda etapa utiliza o Amazon Bedrock para realizar a análise inteligente do código.

O modelo recebe um prompt contendo:

* linguagem utilizada;
* código fonte;
* critérios de avaliação.

Critérios analisados:

* legibilidade;
* boas práticas;
* possíveis bugs;
* segurança;
* performance.

Exemplo de retorno:

```json
{
  "score": 3,
  "summary": "The code is simple but requires improvements.",
  "issues": [
    {
      "type": "Readability",
      "description": "Function name should be more descriptive."
    }
  ],
  "suggestions": [
    {
      "type": "Best Practices",
      "suggestion": "Add type hints."
    }
  ]
}
```

---

## 3. Generate Report

A última etapa organiza a resposta gerada pela inteligência artificial.

Ela transforma a análise em um formato consistente para consumo da aplicação.

Resultado:

```json
{
  "title": "AI Code Review Report",
  "score": 3,
  "summary": "...",
  "issues_count": 4,
  "suggestions": []
}
```

---

# Tecnologias utilizadas

## AWS

* **AWS Step Functions**

  * Orquestração do workflow.

* **AWS Lambda**

  * Execução das funções serverless.

* **Amazon Bedrock**

  * Análise inteligente utilizando modelos fundacionais.

* **AWS IAM**

  * Controle de permissões entre serviços.

---

# Workflow

```
                Start
                  |
                  v
          Validate Code
                  |
                  v
          Analyze Code
                  |
                  v
          Generate Report
                  |
                  v
                 End
```

---

# Exemplo de execução

Entrada:

```json
{
  "language": "python",
  "code": "def soma(a,b): return a+b"
}
```

Processamento:

```
Step Functions
      |
      |
      +--> Lambda Validation
      |
      +--> Lambda Analysis
              |
              +--> Amazon Bedrock
      |
      +--> Lambda Report
```

Saída:

```json
{
  "title": "AI Code Review Report",
  "score": 3,
  "summary": "The code is simple but has improvements opportunities."
}
```

---

# Próximos passos

Possíveis evoluções:

* [ ] Criar infraestrutura utilizando AWS SAM/Terraform;
* [ ] Adicionar API Gateway para exposição via HTTP;
* [ ] Criar autenticação de usuários;
* [ ] Armazenar histórico de reviews no DynamoDB;
* [ ] Criar dashboard de métricas;
* [ ] Adicionar testes automatizados.

---

# Objetivo do projeto

Este projeto demonstra a utilização de arquiteturas serverless orientadas a eventos, combinando orquestração de workflows com inteligência artificial generativa através do Amazon Bedrock.
