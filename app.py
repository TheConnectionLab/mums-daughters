"""Kirilli — an educational Streamlit demonstration.

Run with: streamlit run app.py
No data persistence, database, analytics or external API calls.
"""
from pathlib import Path

import streamlit as st

from kirilli_logic import (
    ARCHETYPES,
    DOMAINS,
    LIKERT_LABELS,
    demo_answers,
    score_answers,
    strongest_dimensions,
    suggest_pathways,
)

ROOT = Path(__file__).resolve().parent


def load_example(perspective, keybase):
    """Button callback executes before widgets are instantiated on rerun."""
    for answer_key, value in demo_answers(perspective).items():
        st.session_state[keybase + answer_key] = value
    st.session_state.pop(f"{keybase}show_results", None)


def clear_example(keybase):
    """Clear only answers for selected perspective."""
    for domain in DOMAINS:
        for idx in range(3):
            st.session_state.pop(keybase + f"{domain['key']}_{idx}", None)
    st.session_state.pop(f"{keybase}show_results", None)
st.set_page_config(page_title="Kirilli | Rooted in connection. Free to fly.", page_icon="🪽", layout="centered")
st.markdown("""
<style>
:root {--kirilli-terracotta:#c97d65;--kirilli-sage:#84946f;--kirilli-ink:#493e38;}
.stApp {background: #fcfaf5; color:#493e38;}
h1, h2, h3 {color: #594338 !important;}
[data-testid="stButton"] button[kind="primary"] {background:#a95e4e; border-color:#a95e4e; color:white;}
[data-testid="stMetric"] {background: #fffaf4; border:1px solid #eadfd4; border-radius:12px; padding:12px;}
.kirilli-eyebrow {font-size:.76rem; text-transform:uppercase; letter-spacing:.14em; color:#876a5e; font-weight:650;}
.kirilli-card {border:1px solid #e7dbce; border-radius:14px; background:#fffdf9; padding:17px 20px; margin:14px 0;}
.kirilli-note {color:#6d615b;font-size:.89rem;}
</style>
""", unsafe_allow_html=True)

st.image(str(ROOT / "assets" / "kirilli-logo-web.png"), use_container_width=True)
st.markdown('<p class="kirilli-eyebrow">Mother–daughter connection and wellbeing</p>', unsafe_allow_html=True)
st.markdown("### Growing up shouldn't mean growing apart.")
st.write("Kirilli helps girls aged 10–12 and their mothers or caregivers explore everyday relationship skills through reflection, playful activities and meaningful conversation.")
st.info("**Educational demo only.** This is not a validated assessment or mental-health tool. Please use fictional answers. Do not enter real children's personal information or disclosures. Responses are not intentionally saved in a database; they remain in the active Streamlit session until it ends or is reset.")

tab_intro, tab_survey, tab_activities = st.tabs(["🌱 About Kirilli", "🪺 Explore the questionnaire", "✨ Activity library"])

with tab_intro:
    st.subheader("A place to belong. The freedom to fly.")
    st.write("*Kirilli* (කිරිල්ලී) means **female bird** in Sinhala. A nest offers safety and belonging; learning to fly brings individuality and growing independence. We believe both can exist together.")
    st.markdown("**Discover → Understand → Practise → Grow**")
    cols = st.columns(2)
    with cols[0]:
        st.markdown("**Discover**")
        st.write("Reflect on 15 everyday experiences across five relationship skills.")
        st.markdown("**Practise**")
        st.write("Try short activities and conversation starters in everyday life.")
    with cols[1]:
        st.markdown("**Understand**")
        st.write("Explore a strengths-based *learning pathway*, not a fixed type or diagnosis.")
        st.markdown("**Grow**")
        st.write("Notice what helps you feel connected as needs change.")
    st.caption("An early-stage concept by Antonella Montes de Oca and Anushka Fernando, developed through El Impulso. Proposed pilots: Uruguay and Sri Lanka.")

with tab_survey:
    st.subheader("Your connection check-in")
    st.write("Think of a **fictional mother–daughter pair** and answer the statements from one person's perspective. There are no right or wrong answers.")
    perspective = st.radio("Choose a demo perspective", ["Daughter", "Mother / caregiver"], horizontal=True)
    st.caption("The wording changes with your selection. For a real programme, questionnaires and reporting would require expert review and safeguarding validation.")
    prefix = "daughter" if perspective == "Daughter" else "mother"
    keybase = f"kirilli_{prefix}_"
    completed = 0
    answers = {}
    for section_idx, domain in enumerate(DOMAINS, start=1):
        st.markdown(f"#### {section_idx}. {domain['icon']} {domain['name']}")
        for idx, statement in enumerate(domain[prefix]):
            widget_key = keybase + domain["key"] + "_" + str(idx)
            choice = st.radio(statement, options=[1, 2, 3, 4], format_func=lambda v: LIKERT_LABELS[v-1],
                              index=None, key=widget_key, horizontal=True)
            if choice is not None:
                completed += 1
                answers[f"{domain['key']}_{idx}"] = int(choice)
    st.progress(completed / 15, text=f"{completed} of 15 questions answered")
    col_a, col_b = st.columns(2)
    with col_a:
        st.button("Use fictional example", use_container_width=True,
                  on_click=load_example, args=(perspective, keybase))
    with col_b:
        st.button("Clear this questionnaire", use_container_width=True,
                  on_click=clear_example, args=(keybase,))

    if st.button("Reveal my learning pathway", type="primary", disabled=(completed != 15), use_container_width=True):
        st.session_state[f"{keybase}show_results"] = True
    if completed != 15:
        st.session_state.pop(f"{keybase}show_results", None)
    if completed == 15 and st.session_state.get(f"{keybase}show_results", False):
        scores = score_answers(answers)
        pathways = suggest_pathways(scores)
        strong = strongest_dimensions(scores)
        st.divider()
        st.subheader("Your connection snapshot")
        st.caption("A learning prompt based on selected fictional responses—not a label of a person or a measure of parenting quality.")
        for domain in DOMAINS:
            key = domain["key"]
            st.write(f"**{domain['name']}** · {scores[key]:.1f} / 4")
            st.progress(scores[key] / 4)
        st.success("**Strengths to celebrate:** " + ", ".join(next(d["name"] for d in DOMAINS if d["key"] == k) for k in strong) + ".")
        st.markdown("### A suggested relationship pathway")
        if len(pathways) > 1:
            st.write("Several skills have similar scores. You can explore **any** of these pathways; there is no single definitive archetype.")
        else:
            st.write("This pathway is suggested because that skill received the lowest score in this example. A lower score means a possible topic to practise—not a judgement.")
        for p_key in pathways:
            p = ARCHETYPES[p_key]
            with st.container(border=True):
                st.markdown(f"### {p['name']}")
                st.markdown(f"*{p['subtitle']}*")
                st.markdown("**What you can build on**")
                st.write(p["strength"])
                st.markdown("**An opportunity to grow**")
                st.write(p["insight"])
                st.markdown(f"**Skill focus:** {p['skill']}")
                st.markdown("#### Three activities to try")
                for number, act in enumerate(p["activities"], start=1):
                    with st.expander(f"{number}. {act['title']} · {act['time']}", expanded=(number == 1)):
                        st.caption(f"What you'll need: {act['supplies']}")
                        for step_idx, step in enumerate(act["steps"], start=1):
                            st.markdown(f"{step_idx}. {step}")
                        st.markdown(f"**Talk about it:** {act['prompt']}")
        st.info("**Try this in everyday life:** Pick one small activity, invite both people to take part, and reflect on how it felt. Participation and sharing should always be optional.")
        st.caption("Important: this prototype's questions, scoring and archetypes have not been psychometrically validated. It does not assess whether a relationship is safe. If someone feels unsafe, a trusted professional or local safeguarding service is more appropriate than this demo.")

with tab_activities:
    st.subheader("The Kirilli activity library")
    st.write("Browse the activities without completing a questionnaire. Every family can try any pathway.")
    for domain in DOMAINS:
        p = ARCHETYPES[domain["key"]]
        with st.expander(f"{domain['icon']} {p['name']} — {p['subtitle']}"):
            st.write(p["insight"])
            for a in p["activities"]:
                st.markdown(f"**{a['title']}** · {a['time']}")
                for n, step in enumerate(a["steps"], 1):
                    st.markdown(f"{n}. {step}")
                st.markdown(f"*Conversation starter:* {a['prompt']}")
                st.divider()

st.divider()
st.caption("KIRILLI · Rooted in connection. Free to fly. · An educational proof of concept · No account, tracking, database, or external AI service is used in this demo.")
