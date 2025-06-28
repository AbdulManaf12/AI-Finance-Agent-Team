import streamlit as st
from phi.agent import Agent
from phi.model.openai import OpenAIChat
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.yfinance import YFinanceTools
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

# Define Web Agent
web_agent = Agent(
    name="Web Agent",
    role="Search the web for information",
    model=OpenAIChat(id="gpt-4o"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True,
)

# Define Finance Agent
finance_agent = Agent(
    name="Finance Agent",
    role="Get financial data",
    model=OpenAIChat(id="gpt-4o"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True)],
    instructions=["Use tables to display data"],
    show_tool_calls=True,
    markdown=True,
)

# Define Agent Team
agent_team = Agent(
    team=[web_agent, finance_agent],
    instructions=["Always include sources", "Use tables to display data"],
    show_tool_calls=True,
    markdown=True,
)

# Streamlit App UI
st.title("AI Agent Team for Web Search and Financial Data")

# Text Input for Stock Symbol or Search Query
search_query = st.text_input("Enter a search query or stock symbol:", "NVDA")

# Button to trigger agent response
if st.button("Search for Information"):
    if search_query:
        with st.spinner("Fetching data..."):
            # Query agents based on user input
            response = agent_team.run(
                f"Summarize analyst recommendations and share the latest news for {search_query}"
            )
        st.markdown(response.content)
    else:
        st.error("Please enter a valid search query.")