# General Q&A Agent Testing Guide

## Overview
The General Q&A Agent handles questions that don't fit into the three main categories:
- ✅ NOT academic concept explanations → Use General Q&A
- ✅ NOT writing improvement → Use General Q&A
- ✅ NOT quiz generation → Use General Q&A
- ✅ Greetings, advice, how-to, general chat → Use General Q&A

---

## Test Conversations

### Test 1: Greeting / Conversational

**You type:**
```
Hello, how are you?
```

**Expected Result:**
- ✅ Classified as: "general_question"
- ✅ BABA responds with bilingual greeting
- ✅ Display shows "💬 Answer | الإجابة"
- ✅ Category shown: "💬 conversational"
- ✅ Both English and Arabic answers side by side

---

### Test 2: Study Advice

**You type:**
```
How can I improve my study habits?
```

**Expected Result:**
- ✅ Classified as: "general_question"
- ✅ Category: "💡 advice"
- ✅ Bilingual practical advice
- ✅ May include follow-up suggestions like:
  - "What's the best way to manage my time?"
  - "How do I stay motivated while studying?"

---

### Test 3: Time Management

**You type:**
```
What's the best way to manage my time as a student?
```

**Expected Result:**
- ✅ Classified as: "general_question"
- ✅ Category: "💡 advice"
- ✅ Practical tips in both languages
- ✅ Follow-up suggestions related to time management

---

### Test 4: Career Advice

**You type:**
```
Can you give me career advice for computer science majors?
```

**Expected Result:**
- ✅ Classified as: "general_question"
- ✅ Category: "💡 advice"
- ✅ Career guidance in English and Arabic
- ✅ Possibly tailored to Gulf region context

---

### Test 5: How-To Question

**You type:**
```
How do I write a good research paper?
```

**Expected Result:**
- ✅ Classified as: "general_question" (not writing_improvement)
- ✅ Category: "📋 how-to"
- ✅ Step-by-step guidance in both languages
- ✅ General advice (not specific text improvement)

---

### Test 6: Motivation / Encouragement

**You type:**
```
I'm feeling stressed about my exams
```

**Expected Result:**
- ✅ Classified as: "general_question"
- ✅ Category: "🌟 motivation"
- ✅ Encouraging response in both languages
- ✅ Supportive and positive tone

---

### Test 7: General Knowledge

**You type:**
```
What are the benefits of learning a second language?
```

**Expected Result:**
- ✅ Classified as: "general_question" (not academic explanation)
- ✅ Category: "📚 factual"
- ✅ Informative answer in both languages
- ✅ Follow-up questions about language learning

---

### Test 8: Arabic Greeting

**You type:**
```
مرحبا، كيف حالك؟
```

**Expected Result:**
- ✅ Classified as: "general_question"
- ✅ Category: "💬 conversational"
- ✅ Responds in both Arabic and English
- ✅ Friendly, welcoming tone

---

### Test 9: Arabic Study Question

**You type:**
```
كيف أنظم وقتي للدراسة؟
```
(How do I organize my time for studying?)

**Expected Result:**
- ✅ Classified as: "general_question"
- ✅ Category: "💡 advice" or "📋 how-to"
- ✅ Bilingual time management advice
- ✅ Practical tips

---

### Test 10: Thank You

**You type:**
```
Thank you for your help!
```

**Expected Result:**
- ✅ Classified as: "general_question"
- ✅ Category: "💬 conversational"
- ✅ Polite bilingual response
- ✅ May ask if user needs more help

---

## What Should NOT Be General Q&A

### ❌ Test: Academic Concept (Should be Explanation)

**You type:**
```
What is artificial intelligence?
```

**Expected:**
- ✅ Classified as: "explanation" (NOT general_question)
- ✅ Uses Explainer Agent
- ✅ Shows "📚 Academic Explanation"
- ✅ Includes Gulf region example

---

### ❌ Test: Writing Text (Should be Writing Improvement)

**You type:**
```
Can you check this paragraph: The student study hard for test.
```

**Expected:**
- ✅ Classified as: "writing_improvement" (NOT general_question)
- ✅ Uses Writer Agent
- ✅ Shows "✍️ Writing Improvement"
- ✅ Corrects grammar errors

---

### ❌ Test: Quiz Request (Should be Quiz Generation)

**You type:**
```
Give me a quiz on critical thinking
```

**Expected:**
- ✅ Classified as: "quiz_generation" (NOT general_question)
- ✅ Uses Quiz Agent
- ✅ Shows "🎯 Quiz Time!"
- ✅ Generates bilingual quiz

---

## Display Verification

### Check These Elements:

1. **Header:**
   - ✅ "💬 Answer | الإجابة"

2. **Bilingual Display:**
   - ✅ Two columns: English (left) and Arabic (right)
   - ✅ Proper RTL display for Arabic
   - ✅ Both answers complete and relevant

3. **Category Badge:**
   - ✅ Shows category with appropriate emoji:
     - 💡 advice
     - 📋 how-to
     - 📚 factual
     - 💬 conversational
     - 🌟 motivation

4. **Follow-up Suggestions:**
   - ✅ "🔍 Related Questions You Might Ask:"
   - ✅ 2-3 relevant follow-up questions
   - ✅ Questions make sense in context

5. **Autonomous Actions:**
   - ✅ Shows "General Q&A" agent in actions
   - ✅ Decision mentions category type

---

## Edge Cases

### Test: Ambiguous Question

**You type:**
```
What is the best approach?
```

**Expected:**
- ✅ May classify as either "general_question" or "explanation"
- ✅ System makes reasonable decision
- ✅ Response is helpful regardless

---

### Test: Mixed Request

**You type:**
```
Hello! Can you explain what critical thinking is?
```

**Expected:**
- ✅ Should classify as "explanation" (primary intent)
- ✅ Greeting is acknowledged but explanation takes priority
- ✅ Uses Explainer Agent

---

### Test: Very Short Input

**You type:**
```
Help
```

**Expected:**
- ✅ Classified as: "general_question"
- ✅ Asks what user needs help with
- ✅ Bilingual response

---

## Comparison Test: General vs Academic

### Pair 1: General Question

**You type:**
```
How do I become a better writer?
```

**Expected:**
- ✅ "general_question" - General advice

### Pair 1: Academic Question

**You type:**
```
What is academic writing?
```

**Expected:**
- ✅ "explanation" - Academic concept

---

### Pair 2: General Question

**You type:**
```
What should I study to get a good job?
```

**Expected:**
- ✅ "general_question" - Career advice

### Pair 2: Academic Question

**You type:**
```
What is computer science?
```

**Expected:**
- ✅ "explanation" - Academic concept

---

## Success Criteria

✅ **Feature is working if:**

1. **Correct Classification:**
   - Greetings → general_question
   - Study advice → general_question
   - How-to questions → general_question
   - Academic concepts → explanation (NOT general_question)

2. **Proper Display:**
   - Bilingual answers shown side by side
   - Category badge displays correctly
   - Follow-up suggestions appear when appropriate

3. **Response Quality:**
   - Answers are helpful and relevant
   - Tone is supportive and encouraging
   - Both languages have complete answers (not just translations)

4. **Agent Routing:**
   - "General Q&A" appears in autonomous actions
   - Correct category is identified
   - No errors in console

---

## Quick 3-Minute Test

1. **Greeting:** `Hello!`
   - Should use General Q&A agent

2. **Advice:** `How can I study better?`
   - Should use General Q&A agent

3. **Academic:** `What is critical thinking?`
   - Should use Explainer agent (NOT General Q&A)

4. **Writing:** `Check this: I goes to school`
   - Should use Writer agent (NOT General Q&A)

5. **Quiz:** `Give me a quiz`
   - Should use Quiz agent (NOT General Q&A)

If all 5 work correctly, the General Q&A agent is properly integrated! ✅

---

## Troubleshooting

### Issue: Everything Goes to General Q&A

**Problem:** Even academic concepts use General Q&A

**Check:**
- Classifier prompt has clear distinction
- "what is" patterns trigger explanation, not general_question
- Fallback logic prioritizes correctly

---

### Issue: Nothing Uses General Q&A

**Problem:** Greetings use Explainer agent

**Check:**
- Task classifier recognizes "general_question" type
- Orchestrator has _handle_general_qa_flow method
- app.py has display_general_qa function

---

### Issue: Display Errors

**Problem:** TypeError or missing data

**Check:**
- Validator accepts general_qa results
- Required fields: english_answer, arabic_answer
- Optional fields have defaults

---

## Test with Real Scenarios

### Scenario 1: New Student

```
User: Hi, I'm a new student. Can you help me?
BABA: [General Q&A response, welcoming and helpful]

User: How should I prepare for my first exam?
BABA: [General Q&A response with study tips]

User: What is the scientific method?
BABA: [Explanation response - academic concept]
```

### Scenario 2: Study Session

```
User: I need to improve my focus while studying
BABA: [General Q&A - motivation/advice]

User: What are some good study techniques?
BABA: [General Q&A - how-to advice]

User: Can you quiz me on time management?
BABA: [Quiz generation]
```

---

## Performance Check

After testing, verify:
- ✅ Response time <5 seconds
- ✅ No errors in console
- ✅ Bilingual answers are complete
- ✅ Follow-up suggestions are relevant
- ✅ Category classification makes sense
