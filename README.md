# 💰 AI Finance Agent Team

> **Advanced financial intelligence powered by GPT-4, Yahoo Finance, and web search capabilities**

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.3+-red.svg)](https://flask.palletsprojects.com)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.0+-red.svg)](https://streamlit.io)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4-green.svg)](https://openai.com)
[![Yahoo Finance](https://img.shields.io/badge/Yahoo-Finance-purple.svg)](https://finance.yahoo.com)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🌐 Live Demo

**🚀 Try the AI Finance Agent Team:** [https://manafai.pythonanywhere.com/finance_agent](https://manafai.pythonanywhere.com/finance_agent)

## 🚀 What is this?

A sophisticated **AI Agent Team** that combines multiple specialized agents to provide comprehensive financial analysis. The system integrates **real-time financial data** from Yahoo Finance with **web search capabilities** to deliver complete market intelligence powered by OpenAI's GPT-4.

**Available in multiple formats:**

- 🌐 **Flask Web Application**: Professional web interface with responsive design
- 📱 **Streamlit Dashboard**: Interactive data science interface
- 💻 **CLI Tool**: Command-line interface for quick analysis

## ✨ Features

- 🤖 **Multi-Agent Architecture**: Specialized Web and Finance agents working together
- 📊 **Real-time Financial Data**: Stock prices, analyst recommendations, and company information via YFinance
- 🔍 **Intelligent Web Search**: Latest financial news and market updates via DuckDuckGo
- 📈 **Analyst Recommendations**: Professional investment insights and ratings
- 📋 **Structured Data Display**: Beautiful tables and formatted financial reports
- 🎨 **Interactive Web Interface**: Professional Flask web app with responsive design
- 📱 **Streamlit Dashboard**: Alternative data science interface
- 🔄 **Team Coordination**: Agents collaborate to provide comprehensive analysis
- 📚 **Source Attribution**: All information includes reliable sources
- 🌐 **Live Demo**: Deployed and accessible at https://manafai.pythonanywhere.com/finance_agent

## 🎯 Use Cases

- **Investment Research**: Complete analysis of stocks with recommendations and news
- **Portfolio Management**: Track multiple securities with real-time data
- **Market Intelligence**: Stay updated with latest financial trends and news
- **Financial Planning**: Access comprehensive company and market information
- **Risk Assessment**: Analyst recommendations and market sentiment analysis
- **Trading Support**: Real-time price data and technical analysis

## 🛠️ Installation

1. **Clone the repository**

   ```bash
   git clone <repository-url>
   cd "Finance Agent"
   ```

2. **Install dependencies**

   ```bash
   # For Flask Web Application
   pip install -r requirements.txt

   # Or individual packages
   pip install flask phidata openai python-dotenv yfinance duckduckgo-search

   # For Streamlit (optional)
   pip install streamlit
   ```

3. **Set up environment variables**
   Create a `.env` file in the project root:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   ```

## 🚀 Quick Start

### Option 1: Flask Web Application (Recommended)

```bash
python app.py
```

Then open: http://localhost:5000

**Live Demo:** [https://manafai.pythonanywhere.com/finance_agent](https://manafai.pythonanywhere.com/finance_agent)

### Option 2: Streamlit Dashboard

```bash
streamlit run streamlit_finance_web_agent.py
```

### Option 3: Command Line Interface

```bash
python finance_web_agent.py
```

## 📝 Example Usage

```python
from phi.agent import Agent
from phi.model.openai import OpenAIChat
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.yfinance import YFinanceTools

# Create specialized agents
web_agent = Agent(
    name="Web Agent",
    role="Search the web for information",
    model=OpenAIChat(id="gpt-4o"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"]
)

finance_agent = Agent(
    name="Finance Agent",
    role="Get financial data",
    model=OpenAIChat(id="gpt-4o"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True)],
    instructions=["Use tables to display data"]
)

# Create agent team
agent_team = Agent(
    team=[web_agent, finance_agent],
    instructions=["Always include sources", "Use tables to display data"]
)

# Get comprehensive analysis
response = agent_team.run("Summarize analyst recommendations and share the latest news for NVDA")
print(response.content)
```

## 📸 Screenshots

![Finance Dashboard](Output-1.png)
_Professional Streamlit interface for financial queries_

![Agent Analysis](Output-2.png)
_Comprehensive financial analysis with data tables_

![Market Intelligence](Output-3.png)
_Real-time market data and news integration_

## 🏗️ Architecture

```
🏛️ Agent Team Architecture
├── 🔍 Web Agent
│   ├── DuckDuckGo Search
│   ├── Latest News Retrieval
│   └── Market Sentiment Analysis
├── 💹 Finance Agent
│   ├── Yahoo Finance Integration
│   ├── Stock Price Data
│   ├── Analyst Recommendations
│   └── Company Information
└── 🤝 Team Coordination
    ├── Data Synthesis
    ├── Source Attribution
    └── Formatted Reporting
```

## 📁 Project Structure

```
📦 AI-Finance-Agent-Team/
├── 🌐 app.py                       # Flask web application (Main)
├── � templates/
│   └── index.html                  # Web interface template
├── 🎨 static/
│   ├── css/styles.css              # Modern responsive styling
│   └── js/script.js                # Interactive frontend logic
├── �💰 finance_web_agent.py         # Command-line multi-agent system
├── 🎨 streamlit_finance_web_agent.py # Streamlit dashboard (Alternative)
├── 📦 requirements.txt             # Python dependencies
├── ⚙️ .env.example                 # Environment configuration template
├── 🖼️ Output-1.png                 # Dashboard screenshot
├── 🖼️ Output-2.png                 # Analysis example
├── 🖼️ Output-3.png                 # Market data display
├── 📖 README.md                    # This file
└── 📖 README_FLASK.md              # Detailed Flask documentation
```

## 🌐 Web Application Features

### 🎨 **Modern Interface**

- Responsive design for all devices
- Interactive agent cards and animations
- Professional gradient themes
- Font Awesome icons
- Smooth scrolling navigation

### 🚀 **Flask Backend**

- RESTful API endpoints
- Real-time AI agent integration
- Error handling and validation
- Static file optimization
- Production-ready deployment

### 📱 **User Experience**

- One-click example queries
- Real-time processing indicators
- Formatted AI responses
- Mobile-friendly interface
- Accessible design patterns

## 🎛️ Agent Capabilities

### 🔍 **Web Agent**

- Real-time news search
- Market sentiment analysis
- Company press releases
- Financial blog monitoring
- Social media trends

### 💹 **Finance Agent**

- Current stock prices
- Historical price data
- Analyst recommendations
- Company fundamentals
- Financial ratios
- Earnings reports

### 🤝 **Team Coordination**

- Intelligent query routing
- Data cross-referencing
- Comprehensive reporting
- Source validation
- Conflict resolution

## 🔧 Configuration Options

Customize the agents for specific needs:

```python
# Enhanced Finance Agent
finance_agent = Agent(
    tools=[YFinanceTools(
        stock_price=True,
        analyst_recommendations=True,
        company_info=True,
        stock_fundamentals=True,
        income_statements=True
    )]
)

# Specialized instructions
agent_team = Agent(
    team=[web_agent, finance_agent],
    instructions=[
        "Always include sources and timestamps",
        "Use tables for numerical data",
        "Highlight key insights",
        "Include risk factors"
    ]
)
```

## 📊 Sample Queries

**Try these examples on the live demo: [https://manafai.pythonanywhere.com/finance_agent](https://manafai.pythonanywhere.com/finance_agent)**

- "Analyze AAPL stock performance and latest news"
- "Compare MSFT vs GOOGL analyst recommendations"
- "NVDA vs AAPL comparison"
- "What's the market sentiment for Tesla this week?"
- "META latest news and financials"
- "Get financial summary for SPY ETF"
- "Latest earnings report for Amazon"
- "TSLA analyst recommendations"

## 🌐 Deployment

### Production Deployment

The Flask application is live at: **[https://manafai.pythonanywhere.com/finance_agent](https://manafai.pythonanywhere.com/finance_agent)**

### Local Development

```bash
# Clone and setup
git clone <repository-url>
cd AI-Finance-Agent-Team

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Add your OpenAI API key to .env

# Run Flask app
python app.py
```

Visit: http://localhost:5000

## 🤝 Contributing

We welcome contributions! Areas for enhancement:

- 📈 Additional financial data sources
- 🔮 Predictive analytics features
- 📱 Enhanced mobile responsiveness
- 🔔 Alert and notification systems
- 📊 Advanced charting capabilities
- 🌐 Multi-language support

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- [Phi Framework](https://github.com/phidatahq/phidata) - Multi-agent AI framework
- [OpenAI](https://openai.com) - GPT-4 language model
- [Yahoo Finance](https://finance.yahoo.com) - Financial data provider
- [Flask](https://flask.palletsprojects.com) - Web application framework
- [PythonAnywhere](https://pythonanywhere.com) - Hosting platform
- [DuckDuckGo](https://duckduckgo.com) - Privacy-focused search
- [Streamlit](https://streamlit.io) - Interactive web applications

---

⭐ **Star this repository if you found it helpful!**

📈 **Ready to revolutionize your financial analysis?** Get started now!
