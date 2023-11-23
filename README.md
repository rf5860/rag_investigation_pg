# RAG Using Postgres Vector Extension

This repository is just some messing around / simple investigation into using Postgres as a vector database for RAG.

<!-- TOC -->
* [RAG Using Postgres Vector Extension](#rag-using-postgres-vector-extension)
  * [Background](#background)
      * [What is RAG?](#what-is-rag)
      * [What are popular RAG options?](#what-are-popular-rag-options)
      * [What is a vector database?](#what-is-a-vector-database)
      * [What are some popular vector databases?](#what-are-some-popular-vector-databases)
      * [Using Postgres as a vector database for RAG](#using-postgres-as-a-vector-database-for-rag)
      * [OK, But Why Do You Have Kotlin & Repo Here](#ok-but-why-do-you-have-kotlin--repo-here)
  * [Setup](#setup)
    * [Prerequisites](#prerequisites)
    * [Set-Up](#set-up)
  * [Useful Resources / Links](#useful-resources--links)
    * [RAG](#rag)
    * [Using Postgres as a vector database for RAG](#using-postgres-as-a-vector-database-for-rag-1)
<!-- TOC -->

## Background

#### What is RAG?

Retrieval-Augmented Generation (RAG) is a hybrid approach that combines information retrieval and language generation models for improved natural language understanding and generation. In RAG systems, a query is first used to retrieve relevant documents or data points, which are then used as additional context for generating responses or completing tasks. This approach is particularly useful in creating more informed and accurate language models, as it leverages both pre-existing structured data and dynamic generation capabilities.

#### What are popular RAG options?

A bunch of popular options exist for getting started with basic RAG systems. Probably one of the most common is [LangChain](https://www.langchain.com/) for low-level abstractions, backed by a vector database such as [Chroma](https://www.trychroma.com/).

#### What is a vector database?

A vector database allows for complex data to be efficiently queried by storing data as vectors. This allows for fast similarity searches, which is useful for RAG systems.

#### What are some popular vector databases?

- [facebookresearch/faiss: A library for efficient similarity search and clustering of dense vectors.](https://github.com/facebookresearch/faiss)
- [Vector Database for Vector Search | Pinecone](https://www.pinecone.io/)
- [Elasticsearch vector search - highly relevant, lightning fast search | Elastic](https://www.elastic.co/enterprise-search/vector-search)

#### Using Postgres as a vector database for RAG

Which brings us to this repository. This is basically a scratchpad for investigating using Postgres via pgvector as a vector database for RAG (Which seems like a [pretty widely explored concept](#using-postgres-as-a-vector-database-for-rag-1)).

#### OK, But Why Do You Have Kotlin & Repo Here

` "¯\_(ツ)_/¯ "`

## Setup
### Prerequisites

- [PostgreSQL](https://www.postgresql.org/) (tested with v16)

### Set-Up

1. Compile and install [pgvector/pgvector: Open-source vector similarity search for Postgres](https://github.com/pgvector/pgvector)
2. Enable the extension in your database: `CREATE EXTENSION vector;`
3. Create a tale with a 3-dimension vector colum: `CREATE TABLE items (id bigserial PRIMARY KEY, embedding vector(3));`
4. Insert some data: `INSERT INTO items (embedding) VALUES ('[1, 2, 3]'), ('[4, 5, 6]');`
5. Query the data: `SELECT * FROM items ORDER BY embedding <-> '[3, 1, 2]' LIMIT 5;`

## Useful Resources / Links

### RAG

- [RAG Documentation on HuggingFace](https://huggingface.co/docs/transformers/model_doc/rag)

### Using Postgres as a vector database for RAG

- [Turning PostgreSQL Into A Vector Store](https://www.i-programmer.info/news/84-database/16631-turn-postgresql-into-a-vector-store.html)
- [Why you don't need a specialist Vector Database](https://bionic-gpt.com/blog/you-dont-need-a-vector-database/)
- [PostgreSQL as Vector Database. Introduction](https://medium.com/@scholarly360/postgresql-as-vector-database-bae6dd7097a1)
- [PostgreSQL as a Vector Database: Create, Store, and Query OpenAI Embeddings With pgvector](https://www.timescale.com/blog/postgresql-as-a-vector-database-create-store-and-query-openai-embeddings-with-pgvector/)