# Term 1 - Week 3: Lists & Dictionaries

--- https://docs.google.com/presentation/d/1snY8xMvGVIenZx-jlOGN25bZWKwUs-iX04kaqMtvkOM/edit?usp=sharing

## 1. Homework & workshop assignments -> [`homework/`](homework/) "Hackathon"

**What was the assignment?** Use an LLM API (via Python) to build a tool that reduces a specific inequality. The solution must make real API calls, handle responses, and deliver something a real person could use.

**What did I hand in?** Presentation with the webpage and demo on it and the code.py in /hackathon. 
_List the files, or link to them. Notebook exports, screenshots, scripts._
https://docs.google.com/presentation/d/1snY8xMvGVIenZx-jlOGN25bZWKwUs-iX04kaqMtvkOM/edit?usp=sharing

**What did I find difficult, and how did I solve it?** At first, I got `KeyError` when trying to look up a district or an item that was not in the dictionary. I solved this by using the `.get()` method with a default value instead of square brackets, and by using `if item in dictionary:` before accessing it. 

### Checklist
- [ ] My workshop / homework files are in `homework/`
- [ yes] Everything runs without errors, or I explained what does not and why

---


## 2. Hackathon prototype -> [`hackathon/`](hackathon/)

> Your tool and your SDG for this hackathon are announced at the **start of Friday's class**.
> Write them down here once you know them.

**Project title:**
ClearBureaucracy

**My pair partner:**
[Write your partner's name here]

**Tool we had to use:**
Google Gemini API (multimodal LLM) with Streamlit

**SDG we had to address:**
10 — Reduced Inequalities

**What problem does it solve, and for whom?**
Official letters, tax demands, and legal notices use very difficult words ("legalese"). Normal citizens—especially immigrants with language barriers, elderly people, and young adults living on their own—cannot understand them. Because of this, they get stressed, miss important deadlines, or end up paying unfair fines. ClearBureaucracy translates these complicated letters into plain, simple everyday words. (Who is not the user: lawyers or companies who already know how the legal system works).

**What did you build?**
We built a web app using Streamlit and Gemini. A user can upload a photo of a letter, upload a PDF document, or paste the confusing text directly. The app explains what the document is about in simple terms, warns about deadlines and money owed, gives a clear 3-step action list, and explains the hardest legal words.

**Link to the live thing (if any):**
https://ai4g-portfolio-joe-uk94stzydd4cc5clnwbd72.streamlit.app

**How do I run it?**
1. You can test it online right now with this live link: https://ai4g-portfolio-joe-uk94stzydd4cc5clnwbd72.streamlit.app/
2. To run it on your own computer:
   - Clone this repository.
   - Install dependencies: `pip install -r requirements.txt`
   - Create a `.env` file and add your Gemini API key: `GEMINI_API_KEY="your_api_key"`
   - Run the app: `streamlit run "Term 1/Week 3/hackathon/app.py"

**Who did what?** Joe: Created the GitHub repository, wrote the Streamlit frontend, implemented the PDF and image processing code, deployed the web app to Streamlit Cloud, and managed the API secrets.
- Partner: Designed and tested the system prompts for the Gemini model, tested sample bureaucratic letters, and prepared the presentation slides.

**Ethical reflection - what are the risks of your tool? Who could it harm?**
The biggest risk is AI error ("hallucination"): if the AI reads a deadline or a bank number wrong, the user could miss a real legal cutoff date and receive a financial penalty. There is also a privacy risk because people upload letters with their full name, home address, or ID numbers. To reduce these risks, we put a clear warning on the website saying this tool is only an informal guide and not a licensed lawyer, and we tell users not to upload sensitive personal IDs. In the future, we want to add an automatic blur tool to hide personal data before the AI reads the document.

### Checklist
- [yes ] Prototype code (or export / workflow file) is in `hackathon/`
- [yes ] This week's slides are in `hackathon/`
- [ yes if streamlit wants to] The prototype actually runs, and I wrote down how to run it
- [yes] Ethical reflection written above

---

## 3. Presentation -> [`presentation/`](presentation/)

*Only fill this in for the week your group was selected to present. You need at least **one** of these across the whole term.*

- [ ] My group presented in this week
- [ ] Slides are in `presentation/`
- [yes] Proof of the live demo is in `presentation/` (recording, screenshots, or link)

**How did it go? What would I do differently next time?** It went well, some trouble with the API working well and Streamlit also but it went pretty well. The only thing i made change is the topic because i talked with other classmates and they did the same or something similar but as i, joe, i'm new to this country and found some difficulties with understading dutch bureaucracy i did this to help myself on my own things and maybe it was a little selfish on my part. 

---

## 4. Reflection

**What is the most important thing I learned this week?** I learned how to connect Python logic to a cloud AI model and deploy it as a public website. I also learned how to handle real-world deployment bugs, like file path spaces and environment secret settings.

**Where does this connect to "AI for Good"?** Complicated institutional language creates a wall between citizens and their basic rights. Using AI to make official communication clear and accessible gives ordinary people equal access to justice, regardless of their background or education level.
_One concrete link to ethics, sustainability or social impact._
