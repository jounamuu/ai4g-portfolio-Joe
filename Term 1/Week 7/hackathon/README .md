# BirdID — The Hague Bird Identifier

**Hackathon 7: Eyes on Earth · SDG 15: Life on Land**

## Purpose and status

BirdID is for students and beginner birdwatchers curious about Dutch biodiversity. Its intended Streamlit app uploads a photograph to a trained Roboflow model and displays a suggested bird category and confidence score.

It supports **SDG 15** through biodiversity education, not verified wildlife monitoring. “The Hague” describes the intended audience, not validated local coverage.

## Dataset and results

We reused **Bird Species Classification** from Roboflow Universe: **502 labelled images**, split into **351 training, 101 validation and 50 test images**. The summary reports eight bird categories; screenshots also show a “placeholder” label requiring an audit. The model is **DINOv3 Small**.

Roboflow reports **100% precision, 97.5% recall and 98.6% F1** on the test split at a **17% confidence threshold**. Median server-side API latency is **11.8 ms**, excluding network time. These results do not guarantee accuracy on new Dutch photographs. Source: supplied Roboflow dataset-version and model-evaluation screenshots, 27 October 2026.

## How to run

## 1. Open the project folder

Download or copy the project to your computer. Open a terminal in the folder containing `app.py`.

## 2. Create and activate a virtual environment

Create it:

```bash
python -m venv .venv
```

If your computer uses `python3`, use `python3` for this command.

**Windows PowerShell — activate:**

```powershell
.\.venv\Scripts\Activate.ps1
```

**macOS/Linux — activate:**

```bash
source .venv/bin/activate
```

If PowerShell blocks activation, skip it and use `.\.venv\Scripts\python.exe` instead of `python` in the next install and run commands. You do not need to change your security policy.

## 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

## 4. Add your API key privately

Inside the project folder:

1. Create a folder named `.streamlit`.
2. Inside it, create a file named `secrets.toml`.
3. Paste this line and insert your real API key between the empty quotes:

```toml
ROBOFLOW_API_KEY = ""
```

Keep this key at the top level of the file, not under a section heading. See the [Streamlit secrets documentation](https://docs.streamlit.io/develop/concepts/connections/secrets-management).

Never share this file or commit it to GitHub. Add these entries to `.gitignore`:

```gitignore
.venv/
.streamlit/secrets.toml
.env
__pycache__/
```

## 5. Start and test BirdID

```bash
python -m streamlit run app.py
```

Open the address shown in the terminal, usually [**http://localhost:8501**](http://localhost:8501).

Upload a bird photograph that was not used for training. Check that the app displays a suggested category and confidence score, or a clear **“no prediction”** message. Verify suggestions independently.

Keep the terminal open while using the app. Press **Ctrl+C** to stop it. Next time, open the project folder, activate the virtual environment and run the same start command.

## Quick fixes

- **Python not found:** check that Python 3.12 is installed; on macOS/Linux, try `python3` when creating the environment.
- **Missing package:** activate the environment and repeat the dependency installation.
- **Missing key or authentication error:** check the secret name, API key, model configuration and model access. Restart the app after changing secrets.
- **Empty prediction:** record it as no prediction, not a confirmed identification.



&nbsp;