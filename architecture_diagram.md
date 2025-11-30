User (Browser)
   
Streamlit UI (app.py)

   
   -- On startup:
   
   |     - Loads hr_agent_system_prompt.txt
   
   |     - Parses it into sections (Leave Policy, Benefits, Working Hours, etc.)
   |
   
   |- On each question:
   
         1. Check if it's a personal leave balance question
              -> Respond with "check HR portal" message
         2. Else, check if it's a numeric leave calculation (total leave, EL after X months)
              -> Compute using fixed rules and reply
         3. Else, route to the correct section
              -> e.g., "leave" -> Leave Policy section
              -> "benefits" -> Benefits section
              -> "working hours" -> Working Hours section
         4. Apply friendly rewriter to make answer conversational

         5. Display answer in the UI




                   ┌──────────────────────┐
                   │        User          │
                   │  (Browser / Client)  │
                   └──────────┬───────────┘
                              │
                              ▼
                ┌──────────────────────────┐
                │ Streamlit UI (Frontend) │
                │ • Text input box        │
                │ • Displays answer       │
                └──────────┬──────────────┘
                              │ User question
                              ▼
              ┌──────────────────────────────────┐
              │ HR Agent Logic (app.py Backend) │
              │----------------------------------│
              │ 1. Detect type of question       │
              │    • Leave                       │
              │    • Benefits                    │
              │    • Working hours               │
              │    • Salary / Payslip            │
              │    • WFH / Dress code / etc.     │
              │                                  │
              │ 2. Routing rules                 │
              │    • Handle leave balance        │
              │    • Handle leave calculations   │
              │    • Match best policy section   │
              │                                  │
              │ 3. Friendly rewrite layer        │
              │    • Makes answers conversational│
              └──────────┬───────────────────────┘
                              │
                 Looks up required info
                              │
                              ▼
           ┌────────────────────────────────────────┐
           │ HR Knowledge Base (Local Text File)    │
           │        hr_agent_system_prompt.txt       │
           │----------------------------------------│
           │ Contains:                               │
           │  • Leave Policy                         │
           │  • Benefits & Insurance                 │
           │  • Working Hours / Breaks / WFH         │
           │  • Payroll / Attendance                 │
           │  • Office Policies                      │
           │  • Assistant behaviour rules            │
           └───────────────────┬────────────────────┘
                               │
                          Returns matching policy
                               │
                               ▼
              ┌──────────────────────────────────┐
              │ HR Agent Logic                   │
              │ • Formats the text               │
              │ • Applies friendly tone          │
              │ • Adds helpful context           │
              └──────────┬──────────────────────┘
                               │
                        Final Response
                               │
                               ▼
            ┌────────────────────────────────────┐
            │ Streamlit UI (Frontend)            │
            │ • Shows answer in nice formatting  │
            └────────────────────────────────────┘
