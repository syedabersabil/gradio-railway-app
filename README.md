# 🚀 Gradio Railway App

A simple Gradio web application deployed on Railway.

## Features

- **Greeter**: Enter your name and excitement level to get a personalized greeting
- **Text Processor**: Convert text to uppercase
- **Calculator**: Perform basic arithmetic operations

## Local Development

1. Clone the repository:
```bash
git clone https://github.com/syedabersabil/gradio-railway-app.git
cd gradio-railway-app
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the app:
```bash
python app.py
```

4. Open your browser at `http://localhost:7860`

## Deploy to Railway

### Method 1: Deploy from GitHub

1. Go to [Railway.app](https://railway.app/)
2. Sign up or log in with your GitHub account
3. Click "New Project"
4. Select "Deploy from GitHub repo"
5. Choose `syedabersabil/gradio-railway-app`
6. Railway will automatically detect and deploy your app
7. Once deployed, click on the deployment to get your public URL

### Method 2: Using Railway CLI

1. Install Railway CLI:
```bash
npm i -g @railway/cli
```

2. Login:
```bash
railway login
```

3. Initialize and deploy:
```bash
railway init
railway up
```

## Configuration

- The app runs on port 7860 by default
- Railway automatically assigns a public URL
- No environment variables required for basic functionality

## Technologies

- **Gradio**: Web UI framework for Python
- **Railway**: Cloud deployment platform

## License

MIT
