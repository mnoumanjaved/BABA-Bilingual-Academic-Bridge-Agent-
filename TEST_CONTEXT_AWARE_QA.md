# Context-Aware General Q&A Testing Guide

## Overview
The General Q&A Agent is now **context-aware** - it remembers your recent messages and provides personalized responses based on conversation history!

---

## How Context Works

### What's Stored:
- ✅ Last **4 previous user messages** (before current question)
- ✅ Messages up to 150 characters each (truncated if longer)
- ✅ Automatically retrieved from message_history

### What Context Includes:
```
Previous user messages:
1. [First message]
2. [Second message]
3. [Third message]
4. [Fourth message]
```

---

## Test Scenario 1: Study Topic Context

### Step 1: Set Context - Mention a Topic
**You type:**
```
What is artificial intelligence?
```

**Expected:**
- ✅ Uses Explainer agent (academic concept)
- ✅ Provides AI explanation
- ✅ Message saved to history

### Step 2: Ask Related General Question
**You type:**
```
How can I learn more about this?
```

**Expected:**
- ✅ Uses General Q&A agent
- ✅ **Refers to AI from previous message**
- ✅ Provides learning tips specifically for AI
- ✅ Response mentions "artificial intelligence" or "this topic"

**Example Response:**
```
English: "To learn more about artificial intelligence, I recommend..."
Arabic: "لتعلم المزيد عن الذكاء الاصطناعي، أوصي..."
```

---

## Test Scenario 2: Career Context

### Step 1: Discuss Career
**You type:**
```
I'm studying computer science
```

**Expected:**
- ✅ Uses General Q&A agent
- ✅ Responds about CS studies

### Step 2: Ask Career Advice
**You type:**
```
What jobs can I get?
```

**Expected:**
- ✅ Uses General Q&A agent
- ✅ **References computer science from Step 1**
- ✅ Provides CS-specific career advice
- ✅ Mentions "in computer science" or "as a CS student"

---

## Test Scenario 3: Study Habits Context

### Conversation Flow:
```
Message 1: "I have trouble focusing while studying"
→ General Q&A responds with focus tips

Message 2: "I also get distracted by my phone"
→ General Q&A responds with phone distraction tips

Message 3: "What else can help me?"
→ General Q&A refers to focusing and phone issues
→ Provides additional personalized tips
```

**Expected in Message 3:**
- ✅ References both focus and phone issues
- ✅ Provides cohesive advice building on previous tips
- ✅ Doesn't repeat what was already said

---

## Test Scenario 4: Multi-Topic Context

### Step 1-3: Build Context
```
1. "What is machine learning?"
2. "How do I write a research paper?"
3. "What's the best time management technique?"
```

### Step 4: Ask General Question
**You type:**
```
Can you help me organize my week?
```

**Expected:**
- ✅ Acknowledges you're learning about ML
- ✅ Knows you're writing a research paper
- ✅ Considers time management interest
- ✅ Provides schedule advice tailored to these activities

---

## Test Scenario 5: Arabic Context

### Step 1: Arabic Question
**You type:**
```
أنا أدرس في الجامعة
```
(I'm studying at university)

### Step 2: Follow-up in English
**You type:**
```
How can I improve my grades?
```

**Expected:**
- ✅ Understands university context from Arabic message
- ✅ Provides university-specific grade improvement tips
- ✅ Seamless language switching

---

## Test Scenario 6: Context Limit (5 Messages)

### Send 6 Messages:
```
1. "I like programming"
2. "I study mathematics"
3. "I enjoy reading"
4. "I play sports"
5. "I'm interested in AI"
6. "What should I focus on?" ← Current question
```

**Expected Context Used:**
- ✅ Messages 2-5 (last 4 before current)
- ❌ Message 1 is excluded (too old)
- ✅ Response references: math, reading, sports, AI
- ❌ Response doesn't mention: programming

---

## Test Scenario 7: No Context (First Message)

### First Interaction
**You type:**
```
How can I study better?
```

**Expected:**
- ✅ No previous context available
- ✅ Provides general study tips
- ✅ No reference to previous topics
- ✅ Generic but helpful advice

---

## Test Scenario 8: Context After Clear History

### Step 1: Have a Conversation
```
Message 1: "I'm learning Python"
Message 2: "It's challenging"
```

### Step 2: Clear History
- Click "🗑️ Clear History" button

### Step 3: Ask Question
**You type:**
```
Can you help me?
```

**Expected:**
- ✅ No context from Python conversation
- ✅ Asks "What do you need help with?"
- ✅ No mention of Python or programming

---

## Verification: Check Autonomous Actions

When General Q&A uses context, you should see in "🤖 See How BABA Thinks":

```
Step 1: Orchestrator
Action: Gathered conversation context
Decision: Using X previous messages for context-aware response

Step 2: General Q&A
Action: Generated context-aware bilingual answer
Decision: Provided [category] response with conversation awareness
```

---

## Expected Context-Aware Behaviors

### ✅ Good Context Usage:

1. **Pronoun Resolution:**
   ```
   User: "What is Python?"
   User: "How do I learn it?"
   → Agent knows "it" = Python
   ```

2. **Topic Continuity:**
   ```
   User: "I'm interested in data science"
   User: "What skills do I need?"
   → Agent provides data science skills
   ```

3. **Personalization:**
   ```
   User: "I'm a beginner"
   User: "What should I study?"
   → Agent provides beginner-level suggestions
   ```

4. **Avoiding Repetition:**
   ```
   User: "How do I focus?"
   Agent: [Gives 3 tips]
   User: "What else?"
   → Agent gives NEW tips, not repeated ones
   ```

---

## Testing Checklist

Use this checklist to verify context awareness:

- [ ] **Test 1:** Agent references specific topic from previous message
- [ ] **Test 2:** Agent uses context with pronoun "this" or "it"
- [ ] **Test 3:** Agent maintains conversation thread across 3+ messages
- [ ] **Test 4:** Agent personalizes advice based on previous statements
- [ ] **Test 5:** Agent works correctly with NO context (first message)
- [ ] **Test 6:** Only last 4 messages used (5th excluded)
- [ ] **Test 7:** Context cleared after "Clear History"
- [ ] **Test 8:** Autonomous actions show "Gathered conversation context"

---

## Example: Full Context-Aware Conversation

```
User: "What is critical thinking?"
BABA: [Explanation agent - provides definition]

User: "How can I develop this skill?"
BABA: [General Q&A - provides tips for critical thinking]
      "To develop critical thinking skills..." ✅ References CT

User: "What about in my daily life?"
BABA: [General Q&A - context aware]
      "You can apply critical thinking in daily life by..." ✅ Continues CT topic

User: "Thanks! How do I stay motivated?"
BABA: [General Q&A - new topic but remembers CT context]
      "While developing skills like critical thinking..." ✅ Subtle reference

User: "What's a good study schedule?"
BABA: [General Q&A - considers all previous context]
      "A good schedule could include time for critical thinking practice..." ✅ Integrated
```

---

## Troubleshooting

### Issue: Agent Doesn't Use Context

**Check:**
1. Message history is enabled
2. Messages are being saved (check sidebar)
3. Autonomous actions show "Gathered conversation context"
4. At least 1 previous message exists

**Debug:**
- Check browser console (F12) for errors
- Verify `message_history.get_recent_messages()` returns messages
- Check if context is empty or None

---

### Issue: Agent Uses Wrong Context

**Check:**
1. Only last 4 messages should be used
2. Current message should be excluded from context
3. Messages truncated at 150 characters

**Fix:**
- Clear history and start fresh
- Verify message numbering in context

---

### Issue: No Context After Refresh

**This is expected behavior:**
- Context uses session state (not localStorage)
- After refresh, session state is cleared
- **But** message history (sidebar) persists via localStorage
- First message after refresh has no context

---

## Performance Expectations

- ✅ Response time: 3-7 seconds (with context)
- ✅ Context gathering: <100ms
- ✅ No errors with empty context
- ✅ Handles long messages (truncated)

---

## Success Criteria

✅ **Feature is working if:**

1. **Basic Context:**
   - Agent references previous topics
   - Pronouns are resolved correctly
   - Conversation feels continuous

2. **Autonomous Actions:**
   - Shows "Gathered conversation context" step
   - Shows number of messages used

3. **Edge Cases:**
   - Works with no context (first message)
   - Uses only last 4 messages
   - Clears after "Clear History"

4. **Quality:**
   - Context is relevant to current question
   - No hallucinated context
   - Bilingual responses maintain context in both languages

---

## Advanced Test: Context Across Different Task Types

```
1. User: "What is machine learning?" → Explanation agent
2. User: "That's interesting!" → General Q&A (references ML)
3. User: "Quiz me on it" → Quiz agent (generates ML quiz)
4. User: "That was hard!" → General Q&A (knows about ML quiz)
5. User: "How can I learn ML better?" → General Q&A (remembers all)
```

**Expected:**
- ✅ General Q&A in step 2 references machine learning
- ✅ General Q&A in step 4 acknowledges quiz difficulty
- ✅ General Q&A in step 5 provides ML-specific learning tips

---

## Quick 2-Minute Test

1. `"I'm studying computer science"`
2. `"How can I prepare for exams?"`
   - Should mention CS or programming

3. `"What about time management?"`
   - Should still remember CS context

If step 2 and 3 reference CS, context is working! ✅
