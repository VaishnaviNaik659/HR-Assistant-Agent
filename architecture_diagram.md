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
