# 🧑‍💼 HR Policy & Leave Assistant

A simple, friendly HR assistant that answers employee questions about leave, benefits, working hours, and basic company policies.  
The agent runs completely locally using a plain text HR policy file and a lightweight rule-based + keyword matching system (no external APIs).

---

## 🌟 Overview

This project is a **HR Assistant Agent** that:

- Answers common HR queries: **leave policy, total leaves, benefits, working hours, salary issues, WFH rules, dress code, etc.**
- Uses a simple text file `hr_agent_system_prompt.txt` as the **knowledge base**.
- Provides **friendly, human-like responses** instead of rigid policy dumps.
- Supports **basic leave calculations** (e.g., total leaves per year, earned leave after X months).
- Runs as a **Streamlit web app**, easy to demo and deploy.

The primary use case is to act as a **frontline virtual HR assistant** for answering policy, leave & benefits queries quickly and consistently.

---

## ✨ Features

- ✅ **Policy Q&A**  
  - Leave policy (sick, casual, earned, maternity, paternity, half-day)  
  - Benefits, health insurance, PF, gratuity  
  - Working hours, breaks, overtime, WFH  
  - Payroll, salary, attendance corrections  
  - General office policies, dress code, behavior, remote work, travel & reimbursements  

- ✅ **Friendly Answers**  
  - Automatically rewrites raw policy text into a **gentle, clear summary**  
  - Uses simple language and soft tone (no harsh wording)  

- ✅ **Basic Leave Calculations**  
  - Total yearly leave (sick + casual + earned)  
  - Earned leave after X months  

- ✅ **Personal Balance Awareness**  
  - If user asks: “How many leaves do I have now?” →  
    Agent responds: it **cannot see personal balance** and tells user to check HR portal.

- ✅ **Fast & Lightweight**  
  - No machine learning models at runtime  
  - No external APIs or internet calls  
  - Works only with Python + Streamlit + a text file

---

## ⚠️ Limitations

- ❌ Does **not** integrate with real HR systems (no live leave balance, no real payroll data).
- ❌ Only knows what is written in `hr_agent_system_prompt.txt`.  
  If a policy is missing there, the agent cannot answer it.
- ❌ “AI” is rule-based + keyword search. It does not generate new policies or learn automatically.
- ❌ No authentication / employee identification. This is **not** a production HR tool, just a demo assistant.

---

## 🧱 Tech Stack

- **Language:** Python 3.x  
- **Frontend / UI:** [Streamlit](https://streamlit.io/)  
- **Knowledge Base:** Local `.txt` file (`hr_agent_system_prompt.txt`)  
- **Logic:**  
  - Simple **section parser** (splits HR text into sections like "Leave Policy", "Benefits")  
  - Rule-based routing to sections  
  - Keyword matching for fallback  
  - Small “friendly rewriter” layer for responses  

> 🚫 **No external APIs** (no OpenAI, no databases). Entirely offline and self-contained.



