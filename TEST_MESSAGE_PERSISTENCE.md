# Message Persistence Testing Guide

## Test Scenario 1: Basic Message Saving

### Step 1: Start Fresh
1. Open the app: `streamlit run app.py`
2. If you see "📝 Recent Messages" in sidebar, click "🗑️ Clear History"
3. Verify sidebar shows NO recent messages section

### Step 2: Send First Message
**You type:**
```
What is artificial intelligence?
```

**Expected Result:**
- ✅ BABA responds with explanation
- ✅ Sidebar now shows "📝 Recent Messages"
- ✅ You should see: "1. What is artificial intelligence?"

### Step 3: Send Second Message
**You type:**
```
Explain machine learning
```

**Expected Result:**
- ✅ BABA responds with explanation
- ✅ Sidebar shows 2 messages:
  - "1. What is artificial intelligence?"
  - "2. Explain machine learning"

### Step 4: Send Third Message
**You type:**
```
What is deep learning?
```

**Expected Result:**
- ✅ Sidebar shows 3 messages in order
- ✅ Most recent message appears last

---

## Test Scenario 2: Session Persistence (Critical Test)

### Step 1: Send Messages
Send these 3 messages in order:
1. `What is critical thinking?`
2. `Explain sustainability`
3. `What is cloud computing?`

**Expected Result:**
- ✅ All 3 messages appear in sidebar

### Step 2: Refresh Browser
1. Press **F5** or click browser refresh button
2. Wait for app to reload

**Expected Result:**
- ✅ Sidebar still shows all 3 messages!
- ✅ Messages persist after refresh
- ❌ If messages disappear, persistence is NOT working

### Step 3: Close and Reopen Browser Tab
1. Close the browser tab completely
2. Reopen: `http://localhost:8501`

**Expected Result:**
- ✅ Messages should still be there!
- ✅ This proves localStorage is working

---

## Test Scenario 3: 5-Message Limit

### Step 1: Send 5 Messages
Send these messages one by one:
1. `What is blockchain?`
2. `Explain cryptocurrency`
3. `What is quantum computing?`
4. `Explain neural networks`
5. `What is robotics?`

**Expected Result:**
- ✅ Sidebar shows all 5 messages
- ✅ Messages numbered 1-5

### Step 2: Send 6th Message
**You type:**
```
What is cybersecurity?
```

**Expected Result:**
- ✅ Sidebar shows ONLY 5 messages
- ✅ First message ("What is blockchain?") is gone
- ✅ New message appears as #5
- ✅ Oldest message was automatically removed

### Step 3: Send 7th Message
**You type:**
```
Explain artificial neural networks
```

**Expected Result:**
- ✅ Still only 5 messages shown
- ✅ "Explain cryptocurrency" is now gone
- ✅ Only the 5 most recent messages remain

---

## Test Scenario 4: Clear History

### Step 1: Verify Messages Exist
- ✅ Sidebar shows recent messages

### Step 2: Click Clear History
1. Find "🗑️ Clear History" button in sidebar
2. Click it

**Expected Result:**
- ✅ Success message appears: "Message history cleared!"
- ✅ "📝 Recent Messages" section disappears from sidebar
- ✅ History is completely cleared

### Step 3: Verify Persistence of Clearing
1. Refresh browser (F5)

**Expected Result:**
- ✅ Messages still cleared (don't reappear)
- ✅ Sidebar has no recent messages section

---

## Test Scenario 5: Long Messages Truncation

### Send a Long Message
**You type:**
```
Can you explain the concept of distributed systems and how they work in modern cloud computing environments with multiple servers?
```

**Expected Result:**
- ✅ BABA responds normally
- ✅ Sidebar shows truncated version: "Can you explain the concept of distributed sys..."
- ✅ Message is cut off at ~50 characters with "..."

---

## Test Scenario 6: Bilingual Messages

### Send Arabic and English Messages
**Message 1:**
```
ما هو التفكير النقدي؟
```

**Message 2:**
```
What is sustainability?
```

**Message 3:**
```
Explain الذكاء الاصطناعي
```

**Expected Result:**
- ✅ All messages appear in sidebar
- ✅ Arabic text displays correctly (RTL)
- ✅ Mixed English/Arabic messages work

---

## Test Scenario 7: Different Browsers (Advanced)

### Step 1: Chrome Browser
1. Open app in Chrome
2. Send: `Test message in Chrome`
3. Verify it appears in sidebar

### Step 2: Firefox Browser
1. Open app in Firefox (same URL)
2. Check sidebar

**Expected Result:**
- ✅ Chrome message does NOT appear in Firefox
- ✅ Each browser has its own localStorage
- ✅ Messages are browser-specific

### Step 3: Return to Chrome
1. Go back to Chrome tab
2. Check sidebar

**Expected Result:**
- ✅ Chrome message still there
- ✅ Persistence is browser-specific

---

## Test Scenario 8: Quiz Generation with History

### Full Workflow Test
**Message 1:**
```
What is LangGraph?
```

**Expected:**
- ✅ BABA explains LangGraph
- ✅ Message saved to history

**Message 2:**
```
yes
```

**Expected:**
- ✅ BABA generates quiz on LangGraph (using session context)
- ✅ Both messages appear in sidebar

**Verify:**
- ✅ 2 messages in sidebar:
  1. "What is LangGraph?"
  2. "yes"

---

## Common Issues & Solutions

### ❌ Issue 1: Messages Don't Appear in Sidebar

**Check:**
1. Look for JavaScript errors in browser console (F12)
2. Verify `message_history.add_message()` is called in app.py:550
3. Check if session state is working: `st.session_state.message_history_cache`

**Solution:**
```python
# In Python console/debug:
import streamlit as st
print(st.session_state.message_history_cache)
```

### ❌ Issue 2: Messages Disappear After Refresh

**Cause:** localStorage not working

**Check:**
1. Open browser DevTools (F12)
2. Go to: Application → Storage → Local Storage
3. Look for key: `baba_recent_messages`

**Solution:**
- Enable localStorage in browser settings
- Don't use Incognito/Private mode
- Try a different browser

### ❌ Issue 3: JavaScript Component Errors

**Symptoms:**
- Errors mentioning `components.html`
- Messages save but localStorage doesn't work

**Solution:**
1. Restart Streamlit: Ctrl+C and rerun
2. Clear browser cache
3. Update Streamlit: `pip install --upgrade streamlit`

---

## Quick Test Summary

**Minimum Tests to Run:**

1. ✅ **Send 3 messages** → Should appear in sidebar
2. ✅ **Refresh browser** → Messages should persist
3. ✅ **Send 6 messages** → Only last 5 should show
4. ✅ **Clear history** → Messages should disappear
5. ✅ **Refresh after clear** → Should stay cleared

---

## Expected Terminal Output

When messages are saved, you might see:
```
(No errors should appear)
```

If you see errors like:
```
Error saving message history: ...
```

This means localStorage is failing silently (which is OK - feature degrades gracefully).

---

## Success Criteria

✅ **Feature is working if:**
- Messages appear in sidebar immediately after sending
- Messages persist after browser refresh
- Only 5 most recent messages are kept
- Clear history removes all messages
- No errors in browser console

❌ **Feature is NOT working if:**
- Messages don't appear in sidebar
- Messages disappear after refresh
- More than 5 messages are shown
- JavaScript errors in console

---

## Browser Developer Tools Check

### Verify localStorage Directly

1. Open browser DevTools: **F12**
2. Go to: **Application** tab (Chrome) or **Storage** tab (Firefox)
3. Expand: **Local Storage** → `http://localhost:8501`
4. Look for key: `baba_recent_messages`

**Expected Value:**
```json
["What is artificial intelligence?","Explain machine learning","What is deep learning?"]
```

**This confirms:**
- ✅ Messages are being saved to localStorage
- ✅ Format is correct (JSON array)
- ✅ Data persists in browser

---

## Deployment Test (Streamlit Cloud)

If deploying to Streamlit Cloud:

1. Deploy the app
2. Send 3 test messages
3. Note the deployment URL
4. Close browser completely
5. Reopen browser and visit same URL
6. **Expected:** Messages should still be there!

---

## Performance Test

### Test with Rapid Messages

Send these messages quickly (1 per second):
1. `Message 1`
2. `Message 2`
3. `Message 3`
4. `Message 4`
5. `Message 5`

**Expected:**
- ✅ All messages appear correctly
- ✅ No lag or delay
- ✅ No race conditions
- ✅ Correct order maintained

---

## Need Help?

If tests fail:
1. Check browser console (F12) for errors
2. Verify Python version: `python --version` (3.8+)
3. Verify Streamlit version: `streamlit version` (1.28.0+)
4. Try different browser
5. Check `message_history_cache` in session state
