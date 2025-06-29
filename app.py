from flask import Flask, render_template, request, jsonify
import os
import json
import random
from datetime import datetime
from phi.agent import Agent
from phi.model.openai import OpenAIChat
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.yfinance import YFinanceTools
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Check if OpenAI API key is available
openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    print("Warning: OPENAI_API_KEY not found in environment variables")
    print("Please set your OpenAI API key in the .env file")

os.environ["OPENAI_API_KEY"] = openai_api_key

app = Flask(__name__)

# Initialize AI Agents
try:
    web_agent = Agent(
        name="Web Agent",
        role="Search the web for information",
        model=OpenAIChat(id="gpt-4o"),
        tools=[DuckDuckGo()],
        instructions=[
            "Always include sources", 
            "Focus on recent financial news and market sentiment",
            "Provide factual and up-to-date information",
            "Include publication dates when available"
        ],
        show_tool_calls=False,
        markdown=True,
    )

    finance_agent = Agent(
        name="Finance Agent",
        role="Get financial data",
        model=OpenAIChat(id="gpt-4o"),
        tools=[YFinanceTools(
            stock_price=True, 
            analyst_recommendations=True, 
            company_info=True,
            stock_fundamentals=True,
            historical_prices=True
        )],
        instructions=[
            "Use tables to display data when appropriate", 
            "Provide comprehensive financial metrics",
            "Include current market data and historical context",
            "Explain financial ratios and their significance"
        ],
        show_tool_calls=False,
        markdown=True,
    )

    agent_team = Agent(
        team=[web_agent, finance_agent],
        instructions=[
            "Always include sources for all information", 
            "Use tables to display data when appropriate", 
            "Provide comprehensive analysis combining both web research and financial data",
            "Structure the response clearly with headers and sections",
            "Include both quantitative data and qualitative insights",
            "Provide actionable investment insights based on the analysis"
        ],
        show_tool_calls=False,
        markdown=True,
    )
    
    print("AI Agents initialized successfully")
    
except Exception as e:
    print(f"Error initializing AI agents: {e}")
    agent_team = None

def extract_stock_symbols(query):
    """Extract stock symbols from query"""
    common_stocks = ['NVDA', 'AAPL', 'TSLA', 'META', 'GOOGL', 'AMZN', 'MSFT', 'NFLX', 'AMD', 'INTC', 'IBM', 'ORCL', 'CRM', 'ADBE']
    symbols = []
    
    for symbol in common_stocks:
        if symbol in query.upper():
            symbols.append(symbol)
    
    return symbols

def get_agent_analysis(query):
    """Get analysis from AI agent team"""
    if not agent_team:
        return {
            'success': False,
            'error': 'AI agents are not properly initialized. Please check your OpenAI API key.',
            'content': None
        }
    
    try:
        print(f"Processing query: {query}")
        
        # Run the agent team with the query
        response = agent_team.run(query)
        
        if response and hasattr(response, 'content'):
            print("Agent analysis completed successfully")
            return {
                'success': True,
                'content': response.content,
                'raw_response': str(response)
            }
        else:
            return {
                'success': False,
                'error': 'No response received from AI agents',
                'content': None
            }
            
    except Exception as e:
        print(f"Error in agent analysis: {e}")
        return {
            'success': False,
            'error': str(e),
            'content': None
        }

def parse_agent_response(content, query, stock_symbols):
    """Parse agent response and structure it for the frontend"""
    is_comparison = ('vs' in query.lower() or 'comparison' in query.lower() or len(stock_symbols) > 1)
    
    # Basic structure based on query type
    if is_comparison and len(stock_symbols) >= 2:
        return {
            'type': 'comparison',
            'stock1': stock_symbols[0],
            'stock2': stock_symbols[1],
            'agent_content': content,
            'query': query
        }
    elif len(stock_symbols) == 1:
        return {
            'type': 'single',
            'symbol': stock_symbols[0],
            'agent_content': content,
            'query': query
        }
    else:
        return {
            'type': 'general',
            'agent_content': content,
            'query': query
        }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze_stock():
    try:
        data = request.get_json()
        query = data.get('query', '').strip()
        
        if not query:
            return jsonify({'error': 'Please enter a stock symbol or query'}), 400
        
        # Extract stock symbols from query
        stock_symbols = extract_stock_symbols(query)
        
        # Create appropriate query for the agents
        if len(stock_symbols) >= 2 and ('vs' in query.lower() or 'comparison' in query.lower()):
            agent_query = f"Compare {stock_symbols[0]} and {stock_symbols[1]}. Provide detailed financial analysis, recent news, analyst recommendations, and investment comparison."
        elif len(stock_symbols) == 1:
            agent_query = f"Provide comprehensive analysis for {stock_symbols[0]} including current stock price, financial metrics, analyst recommendations, recent news, and investment outlook."
        else:
            agent_query = f"Analyze the following financial query: {query}. Provide market insights, relevant financial data, and investment recommendations."
        
        # Get analysis from AI agents
        agent_result = get_agent_analysis(agent_query)
        
        if not agent_result['success']:
            return jsonify({'error': f"AI Agent Error: {agent_result['error']}"}), 500
        
        # Parse and structure the response
        result = parse_agent_response(agent_result['content'], query, stock_symbols)
        
        return jsonify({'success': True, 'data': result})
        
    except Exception as e:
        return jsonify({'error': f"Server Error: {str(e)}"}), 500

if __name__ == '__main__':
    if not agent_team:
        print("\n" + "="*50)
        print("WARNING: AI agents failed to initialize!")
        print("Please ensure you have:")
        print("1. Set OPENAI_API_KEY in your .env file")
        print("2. Installed all required packages: pip install -r requirements.txt")
        print("3. A valid OpenAI API key with sufficient credits")
        print("="*50 + "\n")
    else:
        print("\n" + "="*50)
        print("AI Finance Agent Team Flask App")
        print("AI Agents: ✓ Initialized")
        print("OpenAI API: ✓ Connected")
        print("Server starting at: http://localhost:5000")
        print("="*50 + "\n")
    
    app.run(debug=True)
