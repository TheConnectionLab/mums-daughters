"""Between Us: early educational demonstration, using demo responses only."""
import streamlit as st
from logic import DOMAINS, PATHWAYS, score_answers, suggest

st.set_page_config(page_title='Between Us · Prototype', page_icon='🌱', layout='centered')
st.title('🌱 Between Us')
st.caption('Mother–daughter connection · Early interactive demonstration')
st.warning('**Demo only.** Not a validated assessment or mental-health tool. Do not enter real children’s information or personal disclosures. Responses are not saved by this app.')

st.write('Explore five everyday relationship skills. This prototype shows how a questionnaire can connect families with positive learning activities.')
perspective = st.radio('Choose a demo perspective', ['Daughter', 'Mother / caregiver'], horizontal=True)
if perspective == 'Mother / caregiver':
    st.info('For demonstration, the statements describe the relationship from a daughter’s perspective. A separate caregiver questionnaire would need to be developed and reviewed before piloting.')

with st.form('survey'):
    responses=[]
    for i,(domain,questions) in enumerate(DOMAINS):
        st.subheader(f'{i+1}. {domain}')
        for j,q in enumerate(questions):
            choice=st.radio(q, options=[1,2,3,4], index=None, horizontal=True, key=f'{i}-{j}', format_func=lambda x: {1:'Not true',2:'A little',3:'Mostly',4:'Very true'}[x])
            responses.append(choice)
    submitted=st.form_submit_button('Show my demo profile', type='primary')

if submitted:
    if any(x is None for x in responses):
        st.error('Please answer all 15 questions to see the demo profile.')
    else:
        scores=score_answers(responses)
        st.subheader('Your connection snapshot')
        st.caption('A snapshot of responses, not a label, diagnosis or measure of parenting quality.')
        for (name,_),value in zip(DOMAINS,scores):
            st.write(f'**{name}** · {value:.1f} / 4')
            st.progress(value/4)
        idx=suggest(scores)
        st.subheader('Suggested learning activity')
        st.success(f'**{PATHWAYS[idx][0]}** — {PATHWAYS[idx][1]}')
        st.caption('This illustrative recommendation uses the lowest-scoring domain. This simple rule has not been validated and should not be used for real family decisions.')

st.divider()
st.write('**Technical demonstration:** questionnaire → deterministic scoring → skills-based recommendation. No AI or blockchain is implemented in this version.')
st.caption('No database, account registration, external analytics or submission of responses to an AI service. This is not ready for live use with children.')
