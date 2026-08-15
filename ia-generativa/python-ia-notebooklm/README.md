# 🐍 Aprendizado de Python com Inteligência Artificial

> Projeto de curadoria, estudo guiado e engenharia de prompts utilizando o NotebookLM para acelerar o domínio de linguagem Python aplicada à Inteligência Artificial e Data Science.

---

## 🎯 Contexto e Objetivos

### Contexto
O ecossistema de Inteligência Artificial e Ciência de Dados tem o Python como sua principal linguagem base. Com a constante evolução das bibliotecas de Machine Learning, Deep Learning e LLMs (Large Language Models), aprender Python de forma isolada pode ser genérico. Este projeto utiliza o NotebookLM como um assistente de estudo inteligente para centralizar documentações, tutoriais e artigos científicos, transformando dados brutos em conhecimento estruturado e prático.

### Objetivos de Estudo
1. **Domínio de Sintaxe e Estruturas Fundamentais:** Compreender estruturas de dados, orientação a objetos e manipulação de dados focada em IA.
2. **Uso de Bibliotecas Essenciais:** Explorar bibliotecas base como `NumPy`, `Pandas`, `Scikit-Learn` e frameworks de IA (como `PyTorch` ou `Hugging Face Transformers`).
3. **Engenharia de Prompts para Estudo:** Desenvolver e catalogar estratégias eficazes de prompts para resolver dúvidas complexas de programação e debugging.
4. **Construção de um Material de Consulta Rápida:** Criar um glossário e um guia de revisão contínua.

---

## 📚 Curadoria de Fontes

Para alimentar o caderno no NotebookLM, foram selecionadas **5 fontes abertas de alta qualidade em PDF e texto**:

1. 📄 **Python Data Science Handbook (Jake VanderPlas - Capítulos de Introdução e NumPy)**
   * *Tipo:* PDF / Capítulos de livro aberto
   * *Link:* [GitHub do livro / O'Reilly Open Text](https://github.com/jakevdp/PythonDataScienceHandbook)
2. 📄 **Documentação Oficial do PyTorch (Tutorial "Learning PyTorch with Examples")**
   * *Tipo:* Texto / Documentação Oficial
   * *Link:* [PyTorch Tutorials](https://pytorch.org/tutorials/)
3. 📄 **Artigo: "A Gentle Introduction to Scikit-Learn for Machine Learning"**
   * *Tipo:* Artigo Técnico / PDF
   * *Link:* [Scikit-Learn User Guide](https://scikit-learn.org/stable/user_guide.html)
4. 📄 **Guia de Boas Práticas Python (PEP 8 - Style Guide for Python Code)**
   * *Tipo:* Documentação em Texto
   * *Link:* [Python.org - PEP 8](https://peps.python.org/pep-0008/)
5. 📄 **Tutorial Prático de Prompt Engineering para Desenvolvedores Python**
   * *Tipo:* Artigo Técnico / Guia Aberto
   * *Link:* Documentos/PDFs de referência sobre integração de LLMs via API em Python.

---

## 🛠️ Engenharia de Prompts e "Cicatrizes" (Troubleshooting)

Nesta seção estão documentadas as interações com o NotebookLM, detalhando os testes, variações de perguntas, limitações encontradas e como os prompts foram aprimorados.

### 🧪 Teste 1: Explicação de Conceitos Complexos
* **Prompt Inicial (Ingênuo):** "Me explica como funciona o PyTorch."
  * *Resultado:* Resposta muito genérica e genérica demais, cobrindo apenas a definição de alto nível sem focar no código ou na matemática.
* **Prompt Refinado (Estratégico):** "Com base nas fontes fornecidas, explique a diferença entre `Tensor` no PyTorch e `ndarray` no NumPy. Inclua exemplos conceituais de quando usar cada um no contexto de treinamento de redes neurais."
  * *Resultado:* O NotebookLM citou diretamente a documentação do PyTorch e o livro de Data Science, destacando que Tensores possuem suporte a GPU e autograd (diferenciação automática).

---

### 🧪 Teste 2: Debugging e Erros Comuns
* **Prompt Inicial:** "Por que dá erro no dimensionamento de arrays?"
  * *Resultado:* Resposta abstrata sem apontar as causas raízes.
* **Prompt Refinado:** "Quais são os erros de forma/dimensão (`shape mismatches`) mais comuns descritos no material sobre `NumPy` e `Scikit-Learn`? Crie um checklist passo a passo para debugar esses erros ao preparar dados para um modelo de Machine Learning."
  * *Resultado:* Gerou um checklist prático verificando `.shape`, `.reshape()` e alinhamento de matrizes $X$ e $y$.

---

### 🩹 "Cicatrizes" e Dificuldades Encontradas (Troubleshooting)

1. **Alucinação / Confusão de Sintaxe:**
   * *Problema:* Ao pedir exemplos de código muito específicos de versões recentes das bibliotecas, a IA misturou métodos antigos e novos.
   * *Solução:* Ajustou-se o prompt para exigir a citação direta dos trechos da documentação carregada: *"Utilize estritamente os exemplos de sintaxe contidos na fonte X para explicar o parâmetro Y"*.
2. **Contexto de PDFs Longos:**
   * *Problema:* Capítulos inteiros em PDF geravam resumos por alto sem focar nas funções Python.
   * *Solução:* Foi necessário fazer perguntas instruindo a IA a atuar como um "Instrutor de Python Senior": *"Assuma o papel de um mentora de programação e extraia apenas os métodos de manipulação de vetores apresentados no Capítulo 2"*.

---

## 🎓 Miniguia de Estudo (Entrega Final)

### 📌 Resumo Estruturado do Assunto

#### 1. Fundamentos de Vetorização e Desempenho
* O processamento em IA exige alta performance. O uso de loops tradicionais (`for` / `while`) em Python puro é ineficiente para grandes volumes de dados.
* O `NumPy` introduz o conceito de *arrays multidimensionais* e *vetorização* em C, permitindo operações elemento a elemento em escala sem a sobrecarga do interpretador Python.

#### 2. Pipeline de Dados com Scikit-Learn
* **Pré-processamento:** Limpeza, imputação de dados ausentes e normalização (`StandardScaler`).
* **Divisão de Dados:** `train_test_split` para separar dados de treino e teste e evitar o *overfitting*.
* **Treinamento e Avaliação:** Ajuste do modelo (`fit`), predição (`predict`) e métricas (`accuracy_score`, `confusion_matrix`).

#### 3. Introdução ao Deep Learning com PyTorch
* **Tensors:** Estruturas de dados fundamentais similares aos arrays do NumPy, mas otimizadas para aceleração por GPU/TPU.
* **Autograd:** Mecanismo de diferenciação automática que calcula gradientes para otimização dos pesos em redes neurais (`loss.backward()`).

---

### 📚 Glossário de Conceitos Aprendidos

| Conceito | Definição Prática |
| :--- | :--- |
| **Tensor** | Matriz multidimensional otimizada para cálculos matemáticos e aceleração via hardware (GPU/TPU). |
| **Vetorização** | Técnica de aplicar uma operação a todo um conjunto de dados de uma só vez, dispensando laços `for`. |
| **Broadcasting** | Mecanismo do NumPy/PyTorch que permite operar arrays de diferentes dimensões sob certas condições. |
| **Overfitting** | Situação em que o modelo decora os dados de treino mas falha ao generalizar para novos dados. |
| **Autograd** | Sistema de cálculo de gradientes automáticos usado no treinamento de modelos de aprendizagem profunda. |
| **Hyperparameter** | Configuração definida antes do treinamento do modelo (ex: taxa de aprendizado, número de épocas). |

---

### 🔁 Prompts Reutilizáveis para Revisões Futuras

Guarde estes prompts para usar no seu dia a dia de estudos:

* 🔍 **Explicador de Conceitos em Camadas:**
  > *"Explique o conceito de [inserir conceito, ex: Gradient Descent] em 3 níveis: 1) Para uma criança de 10 anos, 2) Para um estudante de graduação em Ciência da Computação com exemplo em Python, e 3) Em termos de caso de uso real em IA."*

* 🐛 **Assistente de Debugging:**
  > *"Estou recebendo o erro `ValueError: Found array with dim 3. Expected <= 2`. Com base na documentação do Scikit-Learn fornecida, explique por que este erro ocorre no tratamento de dados e mostre como corrigir utilizando a função `.reshape()`."*

* 📋 **Gerador de Exercícios Práticos:**
  > *"Com base nos capítulos sobre NumPy e Pandas das fontes carregadas, crie 3 exercícios práticos progressivos (Fácil, Médio, Difícil) para testar meu conhecimento em manipulação de DataFrames. Não forneça as respostas imediatamente."*

---