# Between Us — Enhanced Prototype

An educational proof-of-concept Streamlit app featuring 15 questions, five domain scores, a **suggested strengths-based relationship archetype**, an explanation of that archetype, alternative pathways for near-tied scores, and three concrete activities per archetype.

## Deploy to GitHub and Streamlit

1. **Replace `app.py` and `logic.py`** in the root of your existing GitHub repository with the two files provided here. Keep `requirements.txt` in the same folder.
2. Commit the changes. Streamlit Community Cloud should redeploy from the GitHub repository automatically; if not, select Reboot app from the app manager.
3. Keep `app.py` as the Streamlit entrypoint.

The app imports `logic.py`, so both files must be in the same folder.

## Local test

```bash
pip install -r requirements.txt
python -m unittest discover
streamlit run app.py
```

## Important limitations

- The archetypes are original educational learning pathways, **not validated psychological typologies**.
- The questionnaire is not validated and is worded from the daughter's perspective in both demo modes.
- Use only fictional responses. No real children's information.
- No AI, blockchain, database, or outcome evidence is included.
- A real pilot requires safeguarding, privacy and research/measurement review.
