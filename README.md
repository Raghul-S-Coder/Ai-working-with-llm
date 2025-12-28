# LLM Prompt Injection

## 📌 Overview

**LLM Prompt Injection** is a demonstration project designed to show how user queries can be validated and safeguarded before being sent to a Large Language Model (LLM).  
The project uses a **two-step LLM call flow**:

1. **User Query Classification** – Validates whether the user input is safe and allowed.
2. **Main LLM Invocation** – Executes the actual LLM request only if the query passes validation.

This architecture helps mitigate **prompt injection risks** and improves the reliability and security of LLM-based applications.

---

## 🗂 Project Structure

```text
root/
├── llm.py
│   └── Contains base LLM configurations and provider-specific setups
│       (OpenAI, Groq, Google Gemini, etc.)
│
├── llm_prompt_injection.py
│   └── Main application logic:
│       - User query classification (LLM-based)
│       - Conditional execution of the main LLM endpoint
│
├── requirements.txt
│
├── .env-example
│   └── Sample environment variable configuration
│
└── README.md
````

---

## 🔍 How It Works

### 1️⃣ User Query Classifier (First LLM Call)

* The user input is first sent to a **classifier LLM**.
* This classifier determines whether the query is:

  * Safe
  * Allowed
  * Free from prompt injection attempts

### 2️⃣ Main LLM Call (Second LLM Call)

* Only queries that **pass classification** are forwarded.
* The actual LLM endpoint is triggered to generate a response.
* If the query fails validation, the request is blocked or handled safely.

This layered approach significantly reduces the risk of malicious or manipulative prompts.

---

## ⚙️ Environment Configuration

Create a `.env` file in the project root using the format below
(copy from `.env-example`):

```env
# OpenAI API Configuration
OPENAI_API_KEY=your_openai_api_key_here
OPENAI_MODEL=gpt-4o-mini

# Groq API Configuration (alternative to OpenAI)
GROQ_API_KEY=your_groq_api_key_here
GROQ_MODEL=llama-3.1-8b-instant

# Google Gemini API Configuration (alternative to OpenAI/Groq)
GOOGLE_API_KEY=your_google_api_key_here
GOOGLE_MODEL=gemini-pro
```

> 💡 You can switch between providers by updating the active configuration in `llm.py`.

---

## ▶️ How to Run the Project

### 1. Create a Virtual Environment

```bash
python -m venv .venv
```

### 2. Activate the Virtual Environment

**Windows**

```bash
.\.venv\Scripts\activate
```

**Linux / macOS**

```bash
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install --no-cache-dir --trusted-host pypi.python.org --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt
```

### 4. Run the Application

```bash
python llm_prompt_injection.py
```

---

## 🖼 Output Screenshot

![img.png](img.png)

* User query input
* Classification decision
* Final LLM response (if allowed)

---

## 🚀 Key Features

* 🔐 LLM-based prompt injection validation
* 🔄 Multi-provider LLM support (OpenAI, Groq, Gemini)
* 🧩 Modular configuration design
* 🛡 Safer LLM request handling

---

## 📄 License

This project is provided for educational and experimental purposes.
You are free to modify and extend it as needed.

---

## 🙌 Contributions

Contributions, improvements, and security enhancements are welcome.
Feel free to open a pull request or issue.

---

**Happy Coding & Stay Secure with LLMs!** 🚀

