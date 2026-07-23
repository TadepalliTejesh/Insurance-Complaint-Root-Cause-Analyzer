# Insurance Complaint Root Cause Analyzer using LLM Analytics

An AI-powered system for analyzing insurance grievances, grouping semantically similar complaints, identifying underlying root causes, and generating process-improvement recommendations using Large Language Models.

## Problem Statement

**Insurance Complaint Root Cause Analysis**

Create an LLM complaint analyzer that groups insurance grievances by root cause and recommends process changes.

**Domain:** Insurance  
**Business Function:** Quality  
**AI Focus:** LLM Analytics  

## Overview

Insurance organizations receive large volumes of complaints related to claim handling, coverage, settlements, policy servicing, and customer support.

Manual analysis of these complaints is time-consuming and makes it difficult to identify recurring issues.

This project combines Natural Language Processing, Machine Learning, and Large Language Models to automate complaint root-cause analysis.

## System Workflow

```text
Insurance Complaint Dataset
        ↓
Data Preprocessing
        ↓
Complaint Text Generation
        ↓
Sentence Transformer
(all-MiniLM-L6-v2)
        ↓
Semantic Embeddings
        ↓
KMeans Clustering
        ↓
Complaint Clusters
        ↓
LLM Analytics
(Llama 3.3 via OpenRouter)
        ↓
Root Cause Identification
        ↓
Business Impact & Severity
        ↓
Process Improvement Recommendations
        ↓
Streamlit Dashboard
```

## Dataset

This project uses the Texas Insurance Complaints Dataset containing
approximately 299,677 insurance complaint records.

Due to the size of the original dataset, the complete dataset is not
included in this repository. A small sample is provided for reference.

The original dataset can be obtained from the Texas Department of
Insurance public complaints dataset.

The project uses the Texas Insurance Complaints Dataset containing approximately 299,677 insurance complaint records.

Important attributes include:

- Complaint filed against
- Reason complaint filed
- Coverage type
- Coverage level
- Keywords
- Resolution information
- Received date
- Closed date

A representative sample of 20,000 complaints was used for the computationally intensive embedding and clustering pipeline during development.

## Methodology

### 1. Data Preprocessing

The raw complaint dataset is cleaned by handling missing values, selecting relevant attributes, processing dates, and preparing the data for NLP analysis.

### 2. Complaint Text Generation

Relevant complaint attributes are combined into a unified textual representation called `Complaint_Text`.

### 3. Semantic Embeddings

The Sentence Transformer model `all-MiniLM-L6-v2` converts complaint text into 384-dimensional semantic embedding vectors.

### 4. KMeans Clustering

KMeans clustering groups semantically similar complaints into 10 clusters.

### 5. LLM Analytics

Representative complaint information from each cluster is analyzed using Llama 3.3 70B Instruct through OpenRouter.

The LLM generates:

- Root Cause
- Business Impact
- Severity Level
- Process Improvement Recommendation

### 6. Streamlit Dashboard

The results are presented through an interactive dashboard containing:

- Dashboard Overview
- Complaint Analytics
- Root Cause Analysis
- AI Recommendations
- Company Insights

## Technology Stack

**Programming:** Python

**Data Processing:** Pandas, NumPy

**Machine Learning:** Scikit-learn, KMeans

**NLP:** Sentence Transformers

**Embedding Model:** all-MiniLM-L6-v2

**LLM:** Llama 3.3 70B Instruct

**LLM API:** OpenRouter

**Visualization:** Plotly

**Web Application:** Streamlit

**Development:** Google Colab, VS Code

## Installation

Clone the repository:

```bash
git clone <your-repository-url>
cd Insurance-Complaint-Root-Cause-Analyzer
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```text
OPENROUTER_API_KEY=your_api_key_here
```

Run the application:

```bash
python -m streamlit run app.py
```

## Expected Output

The system provides:

- Semantic complaint clusters
- Root-cause identification
- Business-impact analysis
- Severity assessment
- AI-generated process recommendations
- Interactive complaint analytics

## Future Scope

- Real-time complaint monitoring
- Multilingual complaint analysis
- Cloud deployment
- CRM integration
- Predictive complaint analytics
- RAG-based insurance knowledge integration

## Author

**Tejesh Tadepalli**  
B.Tech – Computer Science and Engineering
