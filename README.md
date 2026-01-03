# Telecom Data AI – Phase 0

## 📌 Project Overview
This repository contains my structured learning path and hands-on exercises for building strong foundations in **Python-based data analysis**, **SQL analytics**, and **professional Git/GitHub workflow**, with a long-term focus on **AI-driven telecom and network analytics**.

The project is designed and executed in a disciplined, mentor-reviewed format, emphasizing **clean code**, **data-oriented thinking**, and **real-world problem modeling**.

---

## 🎯 Objectives of Phase 0
The main goals of this phase are:

- Transition from general-purpose Python scripting to **data-oriented programming**
- Strengthen analytical thinking using native Python data structures
- Apply SQL for analytical and reporting tasks
- Establish professional GitHub habits (repository structure, commits, documentation)
- Prepare a solid base for Machine Learning and Data Engineering phases

---

## 🧠 Key Skills Practiced
- Python data structures (list, dict, tuple, generator)
- Algorithmic thinking for data analysis
- Clean and readable Python code
- Basic performance considerations
- Git & GitHub professional workflow
- Technical documentation (README-driven development)

---

## 📂 Repository Structure


---

## 🛠️ Environment & Requirements
- Python >= 3.9
- No external libraries used in Day 1 (pure Python)
- Git (CLI)
- GitHub account

Optional (later phases):
- NumPy
- Pandas
- PostgreSQL / SQL Server

---

## 📘 Day 1 – Python Data-Oriented Basics

### 🔹 Problem Description
Given a small dataset representing **network traffic logs**, the task is to analyze traffic behavior using **pure Python**, without relying on external data libraries.

The dataset models:
- Timestamped traffic data
- Multiple network links
- Detection of abnormal or suspicious values

---

### 🔹 Tasks Performed
- Computation of:
  - Average traffic per link
  - Maximum observed traffic
- Logical definition and detection of suspicious traffic values
- Structured and readable output formatting
- Avoidance of unnecessary loops and inefficient constructs

---

### 🔹 Conceptual Quiz – Answers

**1. Difference between `list` and `generator` in terms of memory usage**  
A list stores all elements in memory at once, while a generator produces values on demand, making it more memory-efficient for large datasets.

**2. Why is `dict` suitable for network data modeling?**  
Because network data is naturally key-based (e.g., time, link, traffic), and dictionaries allow fast lookup and clear semantic mapping.

**3. Mutable vs Immutable data types (with examples)**  
Mutable objects (e.g., list, dict) can be modified after creation, while immutable objects (e.g., tuple, string) cannot, which impacts performance and safety in data processing.

**4. Which data structure becomes problematic with millions of records and why?**  
Plain Python lists may become inefficient due to memory overhead and slow element-wise operations compared to vectorized or streaming approaches.

---

## 📈 Results Summary
- Successfully analyzed simulated network traffic data
- Identified peak and suspicious traffic values
- Produced clean, interpretable output without external libraries

---

## 🧪 How to Run
```bash
python phase0/day01_python_basics.py
