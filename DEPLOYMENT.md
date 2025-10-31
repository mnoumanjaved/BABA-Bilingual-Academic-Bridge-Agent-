# BABA Deployment Guide

Complete guide for deploying BABA to various platforms.

## 🚀 Deployment Options

### Option 1: Streamlit Cloud (Recommended - Free & Easy)

#### Prerequisites
- GitHub account
- Project pushed to GitHub repository
- OpenAI API key

#### Step-by-Step Instructions

1. **Prepare Your Repository**
   ```bash
   # Initialize git (if not already done)
   git init
   git add .
   git commit -m "Initial commit: BABA project"

   # Create GitHub repository and push
   git remote add origin https://github.com/yourusername/baba.git
   git branch -M main
   git push -u origin main
   ```

2. **Deploy to Streamlit Cloud**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Sign in with GitHub
   - Click "New app"
   - Select your repository: `yourusername/baba`
   - Set main file path: `app.py`
   - Click "Deploy"

3. **Configure Secrets**
   - In Streamlit Cloud dashboard, click on your app
   - Go to "Settings" → "Secrets"
   - Add your secrets in TOML format:

   ```toml
   OPENAI_API_KEY = "sk-your-actual-openai-api-key-here"
   OPENAI_MODEL = "gpt-3.5-turbo"
   APP_TITLE = "BABA - Bilingual Academic Bridge Agent"
   DEBUG_MODE = "False"
   ```

4. **Access Your App**
   - Your app will be available at: `https://your-app-name.streamlit.app`
   - Share this URL with users

#### Streamlit Cloud Tips
- Free tier includes: 1 GB RAM, unlimited public apps
- Apps sleep after inactivity (wake up on access)
- Automatic redeployment on git push
- Custom domains available on paid plans

---

### Option 2: Railway Deployment

#### Prerequisites
- Railway account ([railway.app](https://railway.app))
- GitHub account

#### Deployment Steps

1. **Create Railway Project**
   - Go to [railway.app](https://railway.app)
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose your BABA repository

2. **Configure Environment Variables**
   - In Railway dashboard, go to "Variables"
   - Add the following:
   ```
   OPENAI_API_KEY=sk-your-actual-key-here
   OPENAI_MODEL=gpt-3.5-turbo
   PORT=8501
   ```

3. **Create Start Command**
   - Railway will auto-detect Streamlit
   - Or manually set start command:
   ```
   streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
   ```

4. **Deploy**
   - Railway automatically deploys on push
   - Get your public URL from dashboard

#### Railway Pricing
- Free tier: $5/month credit
- After free tier: Pay per usage
- Estimated cost: $5-10/month

---

### Option 3: Render Deployment

#### Prerequisites
- Render account ([render.com](https://render.com))
- GitHub repository

#### Deployment Steps

1. **Create Web Service**
   - Go to [render.com](https://render.com)
   - Click "New" → "Web Service"
   - Connect your GitHub repository

2. **Configure Service**
   - **Name**: baba-app
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `streamlit run app.py --server.port=$PORT --server.address=0.0.0.0`

3. **Add Environment Variables**
   ```
   OPENAI_API_KEY=sk-your-actual-key-here
   OPENAI_MODEL=gpt-3.5-turbo
   ```

4. **Deploy**
   - Click "Create Web Service"
   - Wait for deployment (5-10 minutes)
   - Access via provided URL

#### Render Pricing
- Free tier available (limited)
- Paid plans start at $7/month

---

### Option 4: Local Network Deployment

For deploying on a local network (e.g., university network):

#### Setup

1. **Run on Specific Port**
   ```bash
   streamlit run app.py --server.port 8501 --server.address 0.0.0.0
   ```

2. **Access from Network**
   - Find your local IP: `ipconfig` (Windows) or `ifconfig` (Mac/Linux)
   - Access from other devices: `http://YOUR_IP:8501`

3. **Keep Running**
   - Use screen/tmux for persistent sessions
   - Or run as a system service

---

## 📋 Pre-Deployment Checklist

- [ ] All code pushed to GitHub
- [ ] `.env` file NOT pushed (check `.gitignore`)
- [ ] `requirements.txt` is complete
- [ ] OpenAI API key is ready
- [ ] Tested locally successfully
- [ ] README.md is complete

## 🔒 Security Best Practices

1. **API Keys**
   - Never commit API keys to git
   - Use environment variables
   - Rotate keys periodically

2. **Access Control**
   - Consider adding authentication for production
   - Use HTTPS (automatic on most platforms)
   - Monitor API usage

3. **Rate Limiting**
   - Set up usage alerts in OpenAI dashboard
   - Implement request throttling if needed
   - Monitor costs regularly

## 📊 Monitoring & Maintenance

### Streamlit Cloud
- View logs in dashboard
- Check resource usage
- Monitor app performance

### Railway/Render
- View deployment logs
- Set up monitoring alerts
- Check resource metrics

### Cost Monitoring
- OpenAI usage dashboard
- Set spending limits
- Track API call patterns

## 🐛 Troubleshooting Deployment

### App Won't Start

**Issue**: ModuleNotFoundError
```
Solution: Ensure all packages in requirements.txt
```

**Issue**: Port already in use
```
Solution: Use different port or kill existing process
```

### API Errors

**Issue**: Invalid API key
```
Solution: Double-check environment variable spelling and value
```

**Issue**: Rate limit exceeded
```
Solution: Implement caching, reduce concurrent requests
```

### Performance Issues

**Issue**: Slow responses
```
Solutions:
- Use gpt-3.5-turbo instead of gpt-4
- Implement response caching
- Reduce max_tokens in prompts
```

**Issue**: App timeout
```
Solutions:
- Increase timeout settings
- Optimize LLM calls
- Add loading indicators
```

## 🎯 Post-Deployment Tasks

1. **Test All Features**
   - Explanation flow
   - Writing improvement flow
   - Quiz generation
   - Arabic/English display

2. **Share Access**
   - Provide URL to stakeholders
   - Create demo video
   - Prepare user guide

3. **Monitor Usage**
   - Check OpenAI API usage
   - Monitor app performance
   - Collect user feedback

## 📱 Custom Domain (Optional)

### Streamlit Cloud
- Available on Team/Enterprise plans
- Configure in dashboard settings

### Railway/Render
- Add custom domain in settings
- Update DNS records
- SSL automatic

## 🔄 Update & Redeploy

### Streamlit Cloud
```bash
git add .
git commit -m "Update feature"
git push
# Auto-redeploys
```

### Railway/Render
- Same as above
- Automatic deployment on push

### Manual Redeploy
- Use platform's redeploy button
- Or push empty commit: `git commit --allow-empty -m "Redeploy"`

---

## 📞 Support Resources

- **Streamlit Docs**: [docs.streamlit.io](https://docs.streamlit.io)
- **Railway Docs**: [docs.railway.app](https://docs.railway.app)
- **Render Docs**: [render.com/docs](https://render.com/docs)
- **OpenAI API**: [platform.openai.com/docs](https://platform.openai.com/docs)

## ✅ Deployment Success

Your BABA app is successfully deployed when:
- ✅ URL is accessible
- ✅ Interface loads correctly
- ✅ Arabic text displays properly
- ✅ API calls work
- ✅ All features functional

---

**Recommended for Quick Start**: Streamlit Cloud (free, easy, reliable)

**Recommended for Production**: Railway or Render (better performance, more control)
