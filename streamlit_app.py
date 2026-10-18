import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Datheon AI Assistant",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 Datheon Autonomous AI Assistant")
st.write("Welcome to your interactive GenAI & LangChain Agent workspace powered by Streamlit.")

# Initialize Session State for Chat History
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! I am your AI assistant. How can I help you with your tasks today?"}
    ]

# Display Chat History using st.chat_message
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Handle User Input using st.chat_input
if user_query := st.chat_input("Type your query here (e.g., math calculation, capital of France)..."):
    
    # Append user message to session state
    st.session_state.messages.append({"role": "user", "content": user_query})
    
    with st.chat_message("user"):
        st.markdown(user_query)

    # Generate Agent Response
    with st.chat_message("assistant"):
        with st.spinner("Thinking and executing tools..."):
            
            # Simple logic simulating tool execution based on query
            query_lower = user_query.lower()
            if "france" in query_lower:
                ai_response = "💡 **[Tool Execution: web_search]**\n\nThe capital of France is Paris."
            elif "*" in user_query or "multiply" in query_lower or "calculat" in query_lower:
                ai_response = "🔧 **[Tool Execution: math_calculator]**\n\nThe mathematical evaluation result is **540** (calculated via 45 * 12)."
            else:
                ai_response = f"I processed your query: '{user_query}'. All systems are running smoothly!"
            
            st.markdown(ai_response)
            
        # Append assistant response to session state
        st.session_state.messages.append({"role": "assistant", "content": ai_response})