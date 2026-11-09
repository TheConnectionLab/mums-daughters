"""Between Us: educational proof of concept using fictional responses only."""
import streamlit as st
from logic import DOMAINS, ARCHETYPES, score_answers, profile

st.set_page_config(page_title="Between Us | Connection Profile", page_icon="🌱", layout="centered")
st.title("🌱 Between Us")
st.caption("Mother–daughter connection | Interactive proof of concept")
st.warning("**Demonstration only.** This is not a validated assessment, psychological test, or mental-health tool. Use fictional answers only; do not enter real children's personal information or disclosures. The app does not intentionally store survey results in a database.")
st.write("Discover five everyday relationship skills, explore a **suggested learning archetype**, and try practical activities. Archetypes describe a possible learning focus, **not the kind of mother or daughter someone is**.")
perspective = st.radio("Choose a demo perspective", ["Daughter", "Mother / caregiver"], horizontal=True)
if perspective == "Mother / caregiver":
    st.info("This demonstration currently uses daughter's-perspective statements for both views. A distinct caregiver questionnaire is planned and must be reviewed before real-world use.")

with st.form("survey"):
    responses = []
    for i, (domain, questions) in enumerate(DOMAINS):
        st.subheader(f"{i+1}. {domain}")
        for j, question in enumerate(questions):
            choice = st.radio(question, options=[1, 2, 3, 4], index=None, horizontal=True,
                              key=f"q_{i}_{j}", format_func=lambda x: {1:"Not true", 2:"A little", 3:"Mostly", 4:"Very true"}[x])
            responses.append(choice)
    submitted = st.form_submit_button("Reveal my demo connection profile", type="primary")

if submitted:
    if any(x is None for x in responses):
        st.error("Please answer all 15 questions to see the demo profile.")
    else:
        scores = score_answers(responses)
        result = profile(scores)
        archetype = result["archetype"]
        st.divider()
        st.header("Your connection profile")
        st.caption("A strengths-based snapshot of these fictional responses; not an assessment of relationship quality.")
        st.subheader("Your suggested archetype")
        st.markdown(f"### ✨ {archetype['name']}")
        st.write(f"*{archetype['tagline']}*")
        st.write(f"**What this pattern can mean:** {archetype['pattern']}")
        st.write(f"**A strength to build on:** {archetype['strength']}")
        st.write(f"**A skill to practise:** {archetype['skill']}")
        if result["close_scores"]:
            st.info("Several areas have similarly low scores. This archetype is only a starting suggestion; the other growth areas below are equally worth exploring.")

        st.subheader("Your five connection dimensions")
        for (name, _), value in zip(DOMAINS, scores):
            st.write(f"**{name}** · {value:.1f} / 4")
            st.progress(value / 4)
        strengths = ", ".join(DOMAINS[i][0] for i in result["strength_indices"])
        growth = ", ".join(DOMAINS[i][0] for i in result["growth_indices"])
        st.success(f"**Areas to celebrate:** {strengths}. These scored highest in this demo profile.")
        st.info(f"**Areas to explore:** {growth}. These scored lowest in this demo profile; a lower score is not a diagnosis.")

        st.subheader("Your personalised activity toolkit")
        st.write("Try one activity this week. It is fine to choose a different activity if it feels more relevant.")
        for number, (name, instructions) in enumerate(archetype["activities"], 1):
            with st.expander(f"{number}. {name}", expanded=(number == 1)):
                st.write(instructions)
                st.caption("Keep the conversation low-pressure. Either person may pass on personal sharing.")

        if len(result["growth_indices"]) > 1:
            st.subheader("Another pathway you could explore")
            for index in result["growth_indices"]:
                if index != result["primary_index"]:
                    alternative = ARCHETYPES[index]
                    st.write(f"**{alternative['name']}** — {alternative['skill']}")

        st.subheader("Reflect together (optional)")
        st.markdown("- What is something we already do well together?\n- What is one small change we would both like to try?\n- When shall we check in again?")
        st.caption("These questions are optional; do not pressure a child to disclose private experiences.")
        st.caption("**How was the archetype chosen?** The prototype assigns a learning pathway based on the lowest average of three responses in each domain. When scores tie, it uses questionnaire order and displays other equally low areas. This rule is illustrative and has not been scientifically validated.")

st.divider()
st.write("**Technology demonstration:** structured questionnaire → transparent deterministic scoring → strengths-based pathway → practical learning toolkit.")
st.caption("No AI, blockchain, database, external analytics, or clinical classification is implemented here. Not ready for deployment with real children; safeguarding, privacy, accessibility and psychometric review are required first.")
