# Term 1 - Week 2: Loops & Functions

---

## 1. Homework & workshop assignments -> [`homework/`](homework/)

**What was the assignment?** Build an automated workflow that improves someone's health or well-being.

**What did I hand in?** the json of n8n, a presentation an a video demonstration attached to the first slide in the presentation. all in /hackaton
_List the files, or link to them. Notebook exports, screenshots, scripts._

**What did I find difficult, and how did I solve it?** the difficult part was the conecction between telegram and n8n and i solve it thanks to the AI

### Checklist
- [ ] My workshop / homework files are in `homework/`
- [yes] Everything runs without errors, or I explained what does not and why

---


## 2. Hackathon prototype -> [`hackathon/`](hackathon/)

> Your tool and your SDG for this hackathon are announced at the **start of Friday's class**.
> Write them down here once you know them.

**Project title:** GYMTRACK

**My pair partner:** DYLAN

**Tool we had to use:** N8N

**SDG we had to address:** SDG 3

**What problem does it solve, and for whom?** it solves the problem of tracking your workouts and it's for people who train seriously
_Name a real, specific user. "Everyone" is not a user._

**What did you build?** a telegram chat that simualtes a personal trainer with the help of AI, answering  your questions, making you recomendations and helping you with your trainings and healt 

_Two or three sentences. What can a user actually do with it?_ they can use it as a personal trainer 

**Link to the live thing (if any):** json and demo (presentation) on /hackaton
_Deployed URL, workflow export, video demo - whatever proves it works._

**How do I run it?** you need to execute worflow manually inside n8n and then you need to have the telegram bot we created: https://t.me/PersonalTrainer63919_bot
_Short instructions so someone else can start it._

**Who did what?** Dylan and I worken in n8n. He begin working on it and i finished it. ALso i did the telegram and excel part and Dylan the presentation. 
_Be honest about the split of work between you and your partner._

**Ethical reflection - what are the risks of your tool? Who could it harm?** Building this bot was really cool, but it definitely comes with real risks. The biggest danger is physical injury: because the AI can’t actually see someone's form or lifting technique, it might push a user to add weight when their posture is terrible, leading to serious muscle tears or joint damage. There’s also the problem of bad advice, since AI models sometimes sound totally confident while hallucinating incorrect training tips, and a beginner might blindly trust it over common sense. On top of that, handling personal fitness logs and Telegram IDs in a spreadsheet means privacy is a major concern if the database isn't isolated properly. Finally, constantly chasing progressive overload could push vulnerable people into obsessive habits or burnout. At the end of the day, this is a student project, and users need to know it can never replace a certified coach or a real doctor.
_Every hackathon requires this. One honest paragraph beats three vague ones._

### Checklist
- [ yes] Prototype code (or export / workflow file) is in `hackathon/`
- [yes ] This week's slides are in `hackathon/`
- [yes ] The prototype actually runs, and I wrote down how to run it
- [yes ] Ethical reflection written above

---

## 3. Presentation -> [`presentation/`](presentation/)

*Only fill this in for the week your group was selected to present. You need at least **one** of these across the whole term.*

- [ ] My group presented in this week
- [ ] Slides are in `presentation/`
- [ ] Proof of the live demo is in `presentation/` (recording, screenshots, or link)

**How did it go? What would I do differently next time?**

---

## 4. Reflection

**What is the most important thing I learned this week?** how n8n works because i've tried months ago alone in home with youtube tutorials and i didn't figure it out at all 

**Where does this connect to "AI for Good"?** Where this really connects to "AI for Good" is making healthy habits accessible to everyday people who can't afford a private gym coach.

Personal trainers are expensive, so a lot of students or people on a tight budget end up working out with zero guidance and getting hurt. By putting this on Telegram, anyone with a phone gets free, basic support to stay active, track their workouts safely, and learn how to train without burning out. It is a simple way to take tech and use it to help people build long-term healthy routines, which directly supports UN Sustainable Development Goal 3: Good Health and Well-being.
