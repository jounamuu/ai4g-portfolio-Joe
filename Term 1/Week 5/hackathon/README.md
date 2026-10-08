# Credit Risk Assessment Model

## 1. The Problem and Source

### The Problem

When banks give out loans, some people are unable to pay the money back. This is called a loan default. When borrowers default, banks lose large amounts of money.

To solve this, we built a computer model that checks a loan application before the bank approves it. The model predicts whether an applicant is safe or risky so the bank can avoid losing money while still giving loans to trustworthy people.

### Why This Is a Real Problem (Data & Impact)

* **Huge Financial Losses:** Across the global banking system, unpaid loans (known as non-performing loans, or NPLs) amount to trillions of dollars globally. Even a small increase in default rates can cause banks to fail or require government bailouts.
* **High Cost of Mistakes:** In credit scoring, making a mistake on a risky applicant is much worse than making a mistake on a safe one:

  * **Missing a risky borrower (False Negative):** The bank loses 100% of the money it lent out.
  * **Rejecting a good borrower (False Positive):** The bank only loses out on the small interest fee it would have earned.
* **Access to Credit:** When banks lose too much money from bad loans, they stop lending money to everyone. This hurts small businesses and regular people who need loans to buy homes, go to school, or grow businesses.

### Main Goal

Because losing the loan money hurts the bank much more than missing out on interest, our model focuses on **recall**. This metric measures how good the model is at catching as many risky borrowers as possible before the bank gives them money.

---

## 2. The User and Decision

### Who Uses the Model? (Intended User)

* **Frontline Credit Assessment Officers:** The bank staff who review loan applications and talk directly with customers.
* **Risk Analysts & Management:** The team responsible for keeping the bank's overall lending safe and profitable.

### What Does the Model Decide?

When a customer submits a loan application, the model looks at their information and automatically gives two outputs:

1. **A Risk Label:**

   * **0 (Good / Creditworthy):** The applicant looks safe and is very likely to pay the money back on time.
   * **1 (High Risk / Default Risk):** The applicant shows signs that they might struggle to pay back the loan.

2. **A Probability Score:** A clear percentage showing the exact chance of default (for example, "This applicant has an 80.8% chance of defaulting").

### How Is the Decision Used in Practice? (Human-in-the-Loop)

The model does not make the final decision alone. Instead, it acts as a smart assistant for the bank officer.

* **If the score is LOW RISK (0):**

  * **Action:** Fast-Track Approval.
  * **Why:** The officer can quickly approve the loan, saving time for both the bank and the customer.

* **If the score is HIGH RISK (1):**

  * **Action:** Flag for Manual Review.
  * **Options for the Officer:**

    1. **Extra Support or Stricter Terms:** Instead of a flat refusal, offer a smaller loan amount, require a guarantor, or set up a clearer repayment schedule.
    2. **Detailed Check:** Ask the applicant for more document proof (like extra paystubs or bank statements) before deciding.
    3. **Rejection:** Decline the application if the risk is too high and cannot be safely managed.

---

## 3. Sustainable Development Goal (SDG) Alignment

### Which SDG?

* **Goal:** SDG 8 — Decent Work and Economic Growth.
* **Specific Target:** Target 8.10, which aims to "strengthen the capacity of domestic financial institutions to encourage and expand access to banking, insurance, and financial services for all."

### How?

1. **Replaces Subjective Bias with Objective Scoring:** Traditional credit scoring can rely heavily on human judgment, which often introduces personal biases against certain demographic groups. Machine learning evaluates applicants based on objective data patterns, making lending decisions fairer.

2. **Automates Risk Evaluation:** By automating the initial risk assessment, financial institutions can process credit applications much faster and cheaper. This efficiency lowers operational costs, enabling banks to offer micro-loans that were previously too expensive or labor-intensive to evaluate.

3. **Improves Early Risk Detection:** The model accurately identifies high-risk applications before loans are issued, giving officers the opportunity to offer modified payment plans or require additional security rather than issuing flat rejections.

### Why?

* **Expanding Capital Access for the Underserved:** Millions of individuals, gig workers, and micro-enterprises struggle to secure loans because they lack traditional credit histories or large assets. Objective risk models allow banks to safely assess these "unbanked" or underserved groups, giving them the capital needed to start businesses, pay for education, or manage emergencies.
* **Protecting Bank Stability:** For financial institutions to continuously offer loans to the community, they must keep their default rates low. Uncontrolled non-performing loans can cause banks to fail or restrict credit for everyone. By catching default risks early, banks stay financially healthy and can keep lending safely.
* **Fostering Broader Economic Growth:** When micro-enterprises and individuals gain reliable access to financial services, it drives local business growth, creates new jobs, and reduces poverty—directly fulfilling the broader mission of SDG 8.

---

## 4. About the Dataset

* **Source & Link:** UCI Machine Learning Repository — Statlog (German Credit Data) Dataset.
* **Data Collector & Date:** Contributed by Professor Dr. Hans Hofmann at the University of Hamburg in 1994.
* **Dimensions:** 1,000 rows and 20 feature columns (7 numerical, 13 categorical) plus 1 binary target.
* **Target & Class Balance:** The target variable, where original coding 1 (Good) and 2 (Bad) was re-mapped to standard binary labels:

  * **0 (Creditworthy / Negative Class):** 700 cases (70%).
  * **1 (High Risk / Positive Class):** 300 cases (30%).
* **Known Limitations:** The dataset is relatively small (1,000 records) and reflects demographic and financial conditions in Germany prior to 1994. Consequently, it lacks modern credit indicators (e.g., digital payment trails) and contains historical biases.

---

## 5. Recommended Model and Justification

**Recommended Model:** Logistic Regression (`C = 0.1`, `class_weight = 'balanced'`)

### Justification

Logistic Regression achieved the highest test recall (**76.7%**), correctly identifying 46 out of 60 default cases in the held-out test set while outperforming Random Forest (71.7%) and KNN (35.0%).

Furthermore, Logistic Regression maintains full mathematical interpretability, making it fully compliant with regulatory requirements for credit risk modeling (such as "Right to Explanation" laws).

---

## 6. How to Run the Notebook

1. Open Google Colab.
2. Execute cells sequentially from top to bottom. The dataset will be fetched automatically via URL from the UCI Repository.

---

## 7. Ethical Reflection

### Who Is in the Data (and Who Is Missing)?

The dataset includes records from 1,000 bank loan applicants in 1990s Germany, aged 19 to 75. Missing from this data are non-German residents, modern gig-economy workers, and people with digital credit footprints.

### Hidden Sensitive Information

Even though sensitive information like exact personal identity was removed, other columns act as hidden proxies. For example, loan duration and savings amount strongly reflect an applicant's age, while housing status and job title closely track socioeconomic background and time living in the country.

### Cost of Errors

* **False Negative (missing a default):** The bank loses the money it lent out.
* **False Positive (wrongly flagging a good applicant):** A trustworthy person is denied a loan, harming their business or personal financial progress.

### Actions Taken to Fix These Risks

To make the model fairer, we trained it using balanced class weights (`class_weight='balanced'`) and prioritized catching defaults (recall) over overall accuracy.

Most importantly, we added a strict operational rule: **the model must never automatically reject an applicant.** High-risk predictions only flag the file so a human credit officer can review it carefully before making a final decision.

---

## 8. Extra Information

### Who Did What?

* **Together:** Code
* **Jou:** Presentation slides
* **Ana:** README

### Links

* **Presentation Slides:** [View the presentation](https://docs.google.com/presentation/d/1-ZqOBPOfk5VjM7kng-6-JhNPoIO7-giy71MD-jfox7M/edit?usp=sharing)
* **Code:** [Open the Google Colab notebook](https://colab.research.google.com/drive/1HHNoqH3-iuB7OIuCjeWTo25XaXVeNXWY?usp=sharing)

