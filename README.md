# Kirilli — Mother–daughter connection demo

**Rooted in connection. Free to fly.**

A small Streamlit proof of concept for **Kirilli** (කිරිල්ලී, Sinhala for *female bird*), a proposed mother–daughter connection and wellbeing programme for girls aged 10–12 and their mothers or primary female caregivers. Co-founded by Antonella Montes de Oca and Anushka Fernando; developed through El Impulso.

## What the demonstration includes

- Kirilli branding and the supplied birds-in-flight logo
- A 15-item questionnaire with separate **illustrative mother and daughter wording** across five relationship skills
- A scoring breakdown and strength highlights
- Five strengths-based **learning pathways** (archetypes) with an explanation of the suggested pathway
- **15 guided activities**, three per pathway, with steps, timings and conversation prompts
- Fictional example responses so funders can see the results quickly
- No database, cookies added by this code, external API calls, accounts or AI model

**Important:** The questionnaire, dimensions and archetypes are **not validated psychological measures** and must not be presented as diagnostic or therapeutic. This demo is for fictional data only. It is not suitable for collecting children's information or evaluating child safety. Additional privacy, safeguarding, accessibility and research review are required before any pilot with real families.

## Upload to your existing GitHub repository

1. Download and **unzip** the package.
2. In your existing GitHub repository, upload **all files and folders from inside** `Kirilli_GitHub_Demo` to the repository root. Keep `assets/` and `.streamlit/` as folders.
3. Replace the old `app.py` and old logic file with these new files. The new `app.py` imports **`kirilli_logic.py`**. `logic.py` from the previous Between Us version is not needed.
4. Commit changes. Streamlit Community Cloud should redeploy automatically.
5. In Streamlit Community Cloud make sure **Main file path** is `app.py`.

Your GitHub root should look like:

```text
app.py
kirilli_logic.py
requirements.txt
README.md
test_kirilli_logic.py
assets/
  kirilli-logo.png
  kirilli-logo-web.png
  birds-mark.png
.streamlit/
  config.toml
```

If GitHub's browser uploader omits the hidden `.streamlit` folder, the application will still work, but the custom theme will be absent. You can create `.streamlit/config.toml` through GitHub's **Add file → Create new file** option.

## Run locally

```bash
python -m pip install -r requirements.txt
streamlit run app.py
```

## Test scoring logic

```bash
python -m unittest discover -v
```

## How to demonstrate

1. Open the **Explore the questionnaire** tab.
2. Select **Daughter**.
3. Click **Use fictional example**.
4. Click **Reveal my learning pathway**.
5. Show the five dimension scores, the suggested **Loving Guides** pathway, and expand three activities.
6. Switch to **Mother / caregiver** to see the wording change, or open **Activity library** to show all five pathways.

This is not evidence of a completed field pilot or validated effectiveness. Report prototype status accurately in funding applications.
