import os
import re
import streamlit as st


# =============== LOAD HR NOTES FILE =============== #

def load_hr_notes(path: str = "hr_agent_system_prompt.txt") -> str:
    """Load the HR notes file as a single string."""
    if not os.path.exists(path):
        return ""
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


# =============== PARSE INTO SECTIONS =============== #

def parse_sections(text: str):
    """
    Parse the HR notes into sections based on lines starting with '### '.
    Returns a list of dicts: {"title": str, "text": str}
    """
    sections = []
    current_title = "general"
    current_lines = []

    for line in text.splitlines():
        if line.strip().startswith("### "):
            # Save previous section
            if current_lines:
                sections.append(
                    {
                        "title": current_title.lower(),
                        "text": "\n".join(current_lines).strip()
                    }
                )
                current_lines = []
            current_title = line.strip()[4:].strip()  # remove "### "
        else:
            current_lines.append(line)

    # Save last section
    if current_lines:
        sections.append(
            {
                "title": current_title.lower(),
                "text": "\n".join(current_lines).strip()
            }
        )

    return sections


def clean_text_block(text: str) -> str:
    """
    Clean a section text for display:
    - remove '###' headings if any
    - convert '- ' to '• '
    """
    lines = text.splitlines()
    friendly = []

    for line in lines:
        s = line.strip()

        if s.startswith("### "):
            continue

        if s.startswith("- "):
            s = "• " + s[2:]

        if s:
            friendly.append(s)

    return "\n".join(friendly)


# =============== LEAVE CALCULATION =============== #

def calculate_leave(question: str):
    """
    Simple numeric leave calculations based on static rules.
    """
    q = question.lower()

    sick = 12
    casual = 10
    earned_per_month = 1.5
    earned_year = earned_per_month * 12

    # Total leaves in a year
    if "total leave" in q or ("how many" in q and "leave" in q):
        total = sick + casual + earned_year
        return (
            f"You usually get:\n\n"
            f"• Sick Leave: {sick} days per year\n"
            f"• Casual Leave: {casual} days per year\n"
            f"• Earned Leave: about {earned_year:.1f} days per year\n\n"
            f"So overall, that is around **{total:.1f} days of leave** in a year. 💚"
        )

    # Earned leave after X months
    m = re.search(r"after (\d+) month", q)
    if m:
        months = int(m.group(1))
        earned = months * earned_per_month
        return (
            f"After **{months} months**, you will earn around "
            f"**{earned:.1f} days of earned leave**. 🙂"
        )

    return None


# =============== PERSONAL BALANCE HANDLING =============== #

def is_personal_balance_question(q: str) -> bool:
    q = q.lower()
    if "leave balance" in q:
        return True
    if "pending leave" in q:
        return True
    if "my" in q and "leave" in q and any(
        w in q for w in ["left", "remaining", "now", "pending", "total"]
    ):
        return True
    if "how many leaves do i have" in q:
        return True
    return False


def personal_balance_answer() -> str:
    return (
        "I’m not able to see your personal leave balance here. 💚\n\n"
        "Please check it in the **HR Portal → Leave → Leave Balance**, "
        "or you can ask the HR team for the exact number. 🙂"
    )


# =============== SECTION-BASED ANSWERING =============== #

def find_section_by_keywords(sections, keywords):
    """
    Return the first section whose title contains any of the given keywords.
    """
    for sec in sections:
        title = sec["title"]
        if any(k in title for k in keywords):
            return sec
    return None


def score_text(question: str, text: str) -> int:
    """
    Very simple scoring: count keyword overlaps.
    """
    q_words = [w for w in re.findall(r"\w+", question.lower()) if len(w) > 2]
    t = text.lower()
    return sum(1 for w in q_words if w in t)


def fallback_best_section(question: str, sections):
    """
    Choose the best section by simple keyword score.
    """
    best_sec = None
    best_score = 0

    for sec in sections:
        s = score_text(question, sec["text"])
        if s > best_score:
            best_score = s
            best_sec = sec

    if best_sec and best_score > 0:
        return best_sec

    return None


def make_friendly(text: str) -> str:
    """
    Rewrite the selected HR text into a warm, clear, friendly explanation.
    """
    # Basic friendly tone adjustments
    text = text.replace("Employees", "You").replace("employee", "you")
    text = text.replace("• ", "• ")  # Keep bullets
    text = text.replace("cannot", "can't")
    text = text.replace("cannot be", "can't be")
    text = text.replace("are required", "you may need to")
    text = text.replace("must", "should")
    
    # Add a soft intro & ending
    intro = "Here’s a quick and gentle summary for you 😊:\n\n"
    outro = "\n\nIf you want help applying for it or understanding which leave fits your situation, feel free to ask me anytime. 💚"

    return intro + text + outro


def answer_question(question: str, sections):
    """
    Main routing logic to pick the right section or message.
    Now includes a friendly rewrite layer.
    """
    q = question.lower().strip()

    # 1) Personal leave balance
    if is_personal_balance_question(q):
        return personal_balance_answer()

    # 2) Numeric leave calculations
    calc_reply = calculate_leave(question)
    if calc_reply:
        return calc_reply

    # 3) Route to correct sections
    if "leave" in q:
        sec = find_section_by_keywords(sections, ["leave policy"])
        if sec:
            return make_friendly(clean_text_block(sec["text"]))

    if any(k in q for k in ["benefit", "insurance", "pf", "gratuity"]):
        sec = find_section_by_keywords(sections, ["benefits", "insurance"])
        if sec:
            return make_friendly(clean_text_block(sec["text"]))

    if any(k in q for k in ["working hours", "timing", "break", "overtime", "shift"]):
        sec = find_section_by_keywords(sections, ["working hours"])
        if sec:
            return make_friendly(clean_text_block(sec["text"]))

    if any(k in q for k in ["salary", "payslip", "attendance"]):
        sec = find_section_by_keywords(sections, ["payroll", "salary", "attendance"])
        if sec:
            return make_friendly(clean_text_block(sec["text"]))

    if any(k in q for k in ["wfh", "work from home", "remote", "hybrid"]):
        sec = find_section_by_keywords(sections, ["working hours"])
        if sec:
            return make_friendly(clean_text_block(sec["text"]))

    if any(k in q for k in ["dress", "conduct", "behavior", "office policy"]):
        sec = find_section_by_keywords(sections, ["general office policies", "workplace culture"])
        if sec:
            return make_friendly(clean_text_block(sec["text"]))

    # 4) Fallback chunk search
    sec = fallback_best_section(question, sections)
    if sec:
        return make_friendly(clean_text_block(sec["text"]))

    # 5) Final fallback
    return (
        "Hmm, I’m not able to find anything clear about that in my HR notes. "
        "You can try rephrasing, or I can guide you to the right HR contact. 🙂"
    )



# =============== STREAMLIT APP =============== #

st.set_page_config(page_title="HR Policy Assistant", page_icon="🧑‍💼", layout="centered")
st.title("🧑‍💼 HR Policy & Leave Assistant")

st.caption("Ask about leave, benefits, working hours, or simple HR queries. I’ll reply in a kind and clear way.")

hr_text = load_hr_notes()

if not hr_text:
    st.error("`hr_agent_system_prompt.txt` not found or empty. Put it in the same folder as `app.py`.")
else:
    sections = parse_sections(hr_text)

    user_q = st.text_input("Type your question here:")

    if user_q:
        reply = answer_question(user_q, sections)

        # Convert normal newlines into Markdown line breaks
        formatted = reply.replace("\n", "  \n")

        st.markdown("### Answer")
        st.markdown(formatted)

