import streamlit as st
import re

# Title and subtitle
st.title("🔐 Cyber Safety Bot")
st.subheader("Stay safe online — I'm here to help you detect suspicious links and give safety tips.")

# Function to detect phishing patterns
def detect_phishing_link(message):
    phishing_patterns = [
        r"http[s]?://[0-9]{1,3}(\.[0-9]{1,3}){3}",   # IP address in URL
        r"http[s]?://.*free.*",                     # suspicious 'free' offer links
        r"http[s]?://.*login.*",                    # fake login pages
        r"http[s]?://.*\.ru",                       # risky domains
        r"http[s]?://bit\.ly",                      # URL shortener often used in phishing
    ]
    for pattern in phishing_patterns:
        if re.search(pattern, message.lower()):
            return True
    return False

# Function to extract URLs from user input
def extract_links(text):
    url_pattern = r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+'
    links = re.findall(url_pattern, text)
    return links

# Bot response logic
def chatbot_response(user_input):
    # Extracting links from the user input
    links = extract_links(user_input)

    if re.search(r'\b(hi|hello|hey)\b', user_input.lower()):
        return "👋 Hello! I'm your Cyber Safety Bot. Ask me about online safety or share a link to check."

    elif links:
        # If links are found, check if any are phishing
        phishing_links = [link for link in links if detect_phishing_link(link)]
        
        if phishing_links:
            return f"⚠️ The following link(s) seem suspicious: {', '.join(phishing_links)}. Avoid clicking on unknown or shortened links."
        else:
            return f"✅ The following link(s) appear safe: {', '.join(links)}. Always ensure you're visiting trusted websites."

    elif "safe" in user_input or "protect" in user_input:
        return "🔐 Tip: Use strong passwords, enable 2FA, avoid public Wi-Fi for banking, and don’t reuse passwords."

    elif "help" in user_input:
        return "🛡️ You can ask me to check a link or get tips on staying safe online."

    else:
        return "🤖 I'm still learning. Please ask me about cyber safety or paste a link you'd like me to check."

# Streamlit Input
user_input = st.text_input("You:", placeholder="Type your message or paste a link here")

if user_input:
    response = chatbot_response(user_input)
    st.markdown(f"**Bot:** {response}")
