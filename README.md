🧑‍💼 HR Policy & Leave Assistant


A lightweight, offline HR Assistant that answers employee queries about leave, benefits, working hours, policies, and basic HR procedures using a simple Streamlit interface and a local text-based knowledge base.

No external APIs or AI model calls — fully private, fast, and local.

---
📌 Overview


The HR Policy & Leave Assistant is a streamlined rule-based assistant built to provide quick, friendly, and accurate responses to HR-related queries.

Instead of using complex LLMs or API calls, this project relies on:

A structured HR Knowledge Base stored in hr_agent_system_prompt.txt

A custom logic engine that detects question types

A friendly rewrite layer that returns conversational, HR-friendly answers

A lightweight Streamlit UI for interaction

This makes the system secure, offline, and suitable for internal HR usage or academic demonstration.


---
✨ Features
✔ HR Query Support

Leave policy (Sick, Casual, Earned, Maternity, Paternity, Half-Day)

Working hours, breaks, overtime, WFH rules

Benefits (Health Insurance, PF, Gratuity, Wellness programs)

Payroll basics (Payslips, attendance correction)

Office policies (Dress code, behavior, access, general conduct)

✔ Leave Calculations

Total leaves in a year

Earned leave after X months

Remaining leave if user took X casual/sick/earned days

✔ Friendly HR-Style Answers

All responses are rewritten to be warm, polite, and employee-friendly.

✔ Completely Offline

No network, no LLM calls, no sensitive data exposure.

✔ Fast Response

Uses simple rule-based matching and keyword scoring (no heavy NLP models).


---
⚠️ Limitations

Does NOT connect to real HR systems or databases

Cannot fetch personal user leave balance

Depends fully on the information in hr_agent_system_prompt.txt

Not a real chatbot — no memory of past questions

Limited NLP understanding (keyword-based logic)


---
🧱 Tech Stack
Frontend

Streamlit: Web-based UI

Backend

Python logic functions

Custom keyword routing

Friendly text rewriting engine

Knowledge Base

Plain text file: hr_agent_system_prompt.txt

APIs used

None
(Offline system — no AI endpoints, no LLM calls)

---
🛠️ Setup & Run Instructions
1. Clone or download the project
git clone https://github.com/<your-username>/hr-policy-leave-assistant.git
cd hr-policy-leave-assistant

2. Install required dependencies
pip install -r requirements.txt

requirements.txt contains:
streamlit

3. Run the Streamlit app
streamlit run app.py

4. Open in browser

If it doesn’t open automatically:

👉 Visit: http://localhost:8501

5. Ask any HR-related question

Examples:

“leave policy”

“total leaves in a year”

“working hours”

“pf policy”

“dress code”

“wfh rules”


---
📂 Project Structure
├── app.py
├── hr_agent_system_prompt.txt
├── requirements.txt
└── README.md


---
🚀 Potential Improvements

These can be future upgrades or features:

🔹 1. Integrate a real LLM

Use OpenAI, Gemini, or Claude to make answers more conversational and better at understanding natural language.

🔹 2. Add authentication

Employees can log in → Assistant shows personal leave balances.

🔹 3. Connect to HR systems

Fetch real:

Leave balance

Upcoming holidays

Payslips

Attendance logs

🔹 4. Admin Dashboard

HR team can update policies from a UI instead of editing the text file.

🔹 5. Multi-language Support

Add translations (Kannada, Hindi, regional languages).

🔹 6. Chat History

Allow multi-turn conversations.

🔹 7. Upload PDF HR policies

Automatically convert into chunks and update the knowledge base.
