# BirdID — The Hague Bird Identifier

**Hackathon 7: Eyes on Earth · SDG 15: Life on Land**

[Watch the supplied demo](https://youtu.be/2BRMlEG2k7c)

## Problem and intended users

BirdID targets **HHS students in The Hague who are new to bird identification**, using a laptop with internet access for biodiversity learning. Their task: turn a photograph of an unfamiliar bird into a tentative species name they can check in a guide. This is our selected audience, not a documented classroom deployment. [Vogelbescherming’s beginner recognition resources](https://www.vogelbescherming.nl/in-mijn-tuin/tuinvogels-herkennen) establish the learning context; we have not conducted an HHS user study.

**Not intended for:** professional surveys, conservation decisions, offline fieldwork or identification of every Dutch bird species.

## Product, workflow and value

The product remains a **Python/Streamlit photo classifier**:

1. The user uploads a photograph of one bird.
2. Streamlit sends the image to our Roboflow-hosted model.
3. The model returns a category and confidence score, which the app displays.
4. The learner checks the suggestion independently; this is a user action outside the app.

Roboflow performs the necessary image-classification step. Without it, the interface cannot generate its intended suggestion. The value is an **image-first starting point for species identification**, rather than requiring a species name before searching. A field guide remains useful for verification; we do not claim superiority over existing identification tools. There are no counting, observation-log or export features.

## SDG 15 contribution

The specific issue is an entry barrier to biodiversity learning: recognising which bird species a photograph represents. BirdID aims to support species recognition and more informed engagement with terrestrial biodiversity, relevant to [SDG 15](https://sdgs.un.org/goals/goal15). This is an **indirect educational contribution**; improved learning and conservation outcomes have not been measured.

## Data, results and limitations

**DINOv3 Small**, trained in Roboflow on **502 imported images** from *Bird Species Classification* (Roboflow Universe): 351 training, 101 validation and 50 test. Eight bird categories are reported; a “placeholder” label needs auditing. Supplied Roboflow screenshots report test metrics at 17% confidence: precision 100%, recall 97.5%, F1 98.6%.

Dutch provenance and the required self-collected/self-scraped dataset are **not established**. CC BY 4.0 is reported but requires source verification. Unknown species and poor photographs may produce incorrect or absent results. Scores are not guarantees. See the [ethical reflection](BirdID-Ethical-Reflection.md).

## How to run

### 1. Open the project folder

Download or copy the project to your computer. Open a terminal in the folder containing app.py.

### 2. Create and activate a virtual environment

Create it:

```bash
python -m venv .venv
```

If your computer uses python3, use python3 for this command.

Windows PowerShell — activate:

```powershell
.\.venv\Scripts\Activate.ps1
```

macOS/Linux — activate:

```bash
source .venv/bin/activate
```

If PowerShell blocks activation, skip it and use .\.venv\Scripts\python.exe instead of python in the next install and run commands. You do not need to change your security policy.

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Add your API key privately

Inside the project folder:

Create a folder named .streamlit.
Inside it, create a file named secrets.toml.
Paste this line and insert your real API key between the empty quotes:

```toml
ROBOFLOW_API_KEY = ""
```

Keep this key at the top level of the file, not under a section heading. See the Streamlit secrets documentation.

Never share this file or commit it to GitHub. Add these entries to .gitignore:

```gitignore
.venv/
.streamlit/secrets.toml
.env
__pycache__/
```

### 5. Start and test BirdID

```bash
python -m streamlit run app.py
```

Open the address shown in the terminal, usually http://localhost:8501.

Upload a bird photograph that was not used for training. Check that the app displays a suggested category and confidence score, or a clear “no prediction” message. Verify suggestions independently.

Keep the terminal open while using the app. Press Ctrl+C to stop it. Next time, open the project folder, activate the virtual environment and run the same start command.

### Quick fixes

Python not found: check that Python 3.12 is installed; on macOS/Linux, try python3 when creating the environment.
Missing package: activate the environment and repeat the dependency installation.
Missing key or authentication error: check the secret name, API key, model configuration and model access. Restart the app after changing secrets.
Empty prediction: record it as no prediction, not a confirmed identification.

