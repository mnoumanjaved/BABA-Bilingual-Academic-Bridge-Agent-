# BABA Setup Guide

## Installation Steps

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

This will install all required packages including:
- `streamlit` - Web application framework
- `openai` - OpenAI API client
- `extra-streamlit-components` - For persistent message history using browser cookies
- Other utility libraries

### 2. Configure Environment Variables

Create a `.env` file in the project root:

```bash
OPENAI_API_KEY=your_api_key_here
```

### 3. Run the Application

```bash
streamlit run app.py
```

## Message Persistence Feature

### How It Works

BABA now maintains your last **5 user messages** across browser sessions using **browser localStorage**. This means:

✅ **Persistent Across Sessions**: Your recent messages are saved even if you close the browser
✅ **User-Specific**: Each user has their own message history (stored in their browser)
✅ **Works on All Deployments**: Compatible with Streamlit Cloud, Heroku, AWS, etc.
✅ **No Database Required**: Uses browser localStorage (no external dependencies)
✅ **Privacy-Friendly**: Data stays in the user's browser
✅ **No Installation Required**: Uses native browser features via JavaScript

### What's Stored

- Only the **last 5 user messages** (text content)
- Messages persist indefinitely until manually cleared
- No assistant responses or personal data are stored
- Storage is limited only by browser localStorage quota (typically 5-10MB)

### Features

1. **Automatic Saving**: Every message you send is automatically saved
2. **Sidebar Display**: View your recent messages in the sidebar under "📝 Recent Messages"
3. **Clear History**: Use the "🗑️ Clear History" button to delete all stored messages
4. **Session State Sync**: Messages are synchronized with Streamlit session state
5. **Context Aware**: The system can use recent message history for better context (future feature)

### Technical Details

**Storage Method**: Browser localStorage via JavaScript components
**Storage Key**: `baba_recent_messages`
**Max Messages**: 5
**Expiration**: Never (persists until manually cleared)
**Format**: JSON array
**Dependencies**: None (uses Streamlit's built-in components)

### Deployment Considerations

#### Streamlit Cloud
✅ Works perfectly - cookies are browser-based

#### Heroku
✅ Works perfectly - no file system needed

#### AWS / GCP / Azure
✅ Works on all cloud platforms - independent of server storage

#### Docker
✅ Works in containerized environments - cookies are client-side

### Limitations

- **Browser-Specific**: Messages are tied to the browser/device used
- **localStorage Limits**: Browsers limit localStorage (typically 5-10MB, more than sufficient)
- **Privacy Mode**: Incognito/private browsing may not persist data
- **Browser Compatibility**: Requires modern browser with localStorage support (all browsers since 2010+)

### Privacy & Security

- ✅ Messages stored locally in user's browser
- ✅ No server-side database
- ✅ No third-party tracking
- ✅ No external dependencies required
- ✅ User can clear history anytime
- ✅ Data never leaves the user's browser

## Troubleshooting

### Messages Not Persisting

1. **Check localStorage**: Ensure localStorage is enabled in your browser
   - Open browser DevTools (F12)
   - Go to Application/Storage tab
   - Check localStorage for your app domain

2. **Private Browsing**: Use regular mode, not incognito/private
   - Private mode typically clears localStorage on exit

3. **Browser Settings**: Check if localStorage is disabled
   - Some browsers/extensions block localStorage for privacy

4. **Clear Browser Data**: Try clearing site data and reload

### Session State Issues

If messages don't appear in the sidebar:
1. Refresh the page
2. Check browser console (F12) for JavaScript errors
3. Try a different browser
4. Clear Streamlit cache: Click hamburger menu → "Clear cache"

### JavaScript Errors

If you see errors related to components:
1. Ensure JavaScript is enabled in your browser
2. Check for browser extensions blocking scripts
3. Try disabling ad blockers temporarily
4. Use a different browser to test

## Future Enhancements

Potential features for the message history:
- [ ] Use history for context-aware responses
- [ ] Export message history as JSON/CSV
- [ ] Adjustable history size (5, 10, 20 messages)
- [ ] Search through message history
- [ ] Analytics on message patterns

## Support

For issues or questions:
- Check the troubleshooting section above
- Review logs in the terminal/console
- Check browser developer console for JavaScript errors
