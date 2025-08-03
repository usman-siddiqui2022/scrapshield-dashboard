# 🏭 ScrapShield - Manufacturing Scrap Monitoring Dashboard

A comprehensive manufacturing scrap monitoring dashboard built with Streamlit that provides real-time monitoring, predictive analytics, and alert management for manufacturing operations.

## 🌟 Features

- **Real-time Monitoring**: Live KPIs, machine status indicators, and streaming data visualization
- **Predictive Analytics**: ML-powered forecasting with confidence intervals and feature importance analysis
- **Alert Management**: Configurable thresholds, notification settings, and escalation workflows
- **Historical Analysis**: Deep-dive analytics with various grouping options and trend analysis
- **Role-based Access**: Different views for Operators, Engineers, and Management

## 🚀 Quick Start

### Local Development
```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

### Global Deployment Options

#### 1. Streamlit Cloud (Recommended - Free)
1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repository
4. Deploy with one click!

#### 2. Heroku
```bash
# Install Heroku CLI
heroku create your-app-name
git add .
git commit -m "Initial deployment"
git push heroku main
```

#### 3. Railway
1. Connect your GitHub repository to Railway
2. Railway will automatically detect and deploy your Streamlit app
3. Get a public URL instantly

#### 4. Render
1. Create a new Web Service on Render
2. Connect your GitHub repository
3. Set build command: `pip install -r requirements.txt`
4. Set start command: `streamlit run app.py --server.port=$PORT --server.address=0.0.0.0`

## 📁 Project Structure

```
ScrapShield/
├── app.py                 # Main dashboard application
├── pages/                 # Multi-page navigation
│   ├── 01_Real_Time_Monitoring.py
│   ├── 2_Predictive_Analytics.py
│   ├── 3_Alerts_Management.py
│   └── 4_Historical_Analysis.py
├── utils/                 # Utility modules
│   ├── data_generator.py  # Simulated data generation
│   ├── alert_system.py    # Alert management
│   └── ml_models.py       # Machine learning models
├── .streamlit/            # Streamlit configuration
├── requirements.txt       # Python dependencies
├── Procfile              # Heroku deployment
└── runtime.txt           # Python version specification
```

## 🔧 Configuration

The app is configured for global deployment with:
- **Server**: `0.0.0.0:8501` (accessible from any network)
- **Headless mode**: Enabled for server deployment
- **Theme**: Custom orange theme matching manufacturing aesthetics

## 🌐 Global Access

Once deployed, your app will be accessible globally via:
- **Streamlit Cloud**: `https://your-app-name.streamlit.app`
- **Heroku**: `https://your-app-name.herokuapp.com`
- **Railway**: `https://your-app-name.railway.app`
- **Render**: `https://your-app-name.onrender.com`

## 🔒 Security Considerations

For production deployment:
1. Add authentication (Streamlit-Authenticator)
2. Configure HTTPS/SSL certificates
3. Set up proper environment variables for sensitive data
4. Implement rate limiting
5. Add logging and monitoring

## 📊 Data Sources

Currently uses simulated manufacturing data including:
- Machine metrics (scrap rates, production rates, temperatures)
- Process parameters (pressure, humidity, vibration)
- Operator information and shift data
- Historical trends and patterns

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📄 License

This project is open source and available under the MIT License.

---

**Built with ❤️ using Streamlit, Pandas, Plotly, and Scikit-learn** 