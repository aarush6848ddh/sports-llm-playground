# Sports LLM Playground

A project I built to learn LLM fundamentals from scratch. Each script isolates one core concept so I could see exactly how it works before building on it.

I used the Groq API (free tier) with `llama-3.3-70b-versatile`. Sports is the domain, good for testing because facts are concrete, time-sensitive, and easy to verify.

---

## What I learned

### 1. Basic API call - `01_basic_chat.py`
My first LLM request. I learned the message format (roles: `system`, `user`, `assistant`), what a system prompt is, and how to extract the response from `choices[0].message.content`.

**Key finding:** Every request is just a list of messages. The system prompt is the model's briefing, the user never sees it.

---

### 2. Temperature - `02_temperature.py`
I ran the same prompt at temperatures `0.0`, `0.7`, and `1.5` to see how randomness affects output.

**Key finding:** Temperature only adds meaningful variety when the model is uncertain. On factual, well-known topics (like LeBron's legacy) the outputs barely differ. The model's distribution is already narrow.

---

### 3. Token counting - `03_token_counting.py`
Three prompts of increasing complexity. I printed `prompt_tokens`, `completion_tokens`, and `total_tokens` per call, then accumulated a grand total.

**Key finding:** Completion tokens grow with question complexity. Prompt tokens stay flat when the system prompt is constant. `response.usage` is how you track this.

---

### 4. Multi-turn conversations - `04_conversations.py`
A `while` loop that maintains a running `messages` list, appending each user message and assistant reply before the next call.

**Key finding:** The API is completely stateless. "Memory" is an illusion I create by passing the full message history on every single request. The model has no idea what it said before unless I tell it.

---

### 5. Hallucination test - `05_hallucination.py`
I asked the model about recent game results, current standings, and player injury status, things it cannot know due to its training cutoff.

**Key finding:** The model answers confidently and incorrectly. It knows the *format* of a correct sports answer, so it generates plausible-sounding but fabricated data. This is why RAG exists. For time-sensitive facts, you can't rely on the model's internal knowledge. You need to fetch real data and inject it into the prompt yourself.

---

## Setup

```bash
pip install groq python-dotenv
```

Create a `.env` file:
```
GROQ_API_KEY=your_api_key
```

Get a free API key at [console.groq.com](https://console.groq.com).

---

## Stack
- Python
- [Groq API](https://console.groq.com) (free tier)
- Model: `llama-3.3-70b-versatile`
- Libraries: `groq`, `python-dotenv`
