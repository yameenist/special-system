import re
import random
import string
import streamlit as st

# Function to generate a strong password
def generate_strong_password(length):
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    return "".join(random.choice(characters) for _ in range(length))

# Function to check password strength and provide feedback
def check_password_strength(password):
    score = 0
    feedback = []
    common_passwords = ["password123", "12345678", "qwerty", "letmein", "admin", "welcome"]

    if password in common_passwords:
        return "❌ This password is too common. Choose a more unique one.", "Weak"

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("🔹 Password should be at least 8 characters long.")
    
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("🔹 Include both uppercase and lowercase letters.")
    
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("🔹 Add at least one number (0-9).")
    
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("🔹 Include at least one special character (!@#$%^&*).")

    if score == 4:
        return "✅ Strong Password!", "Strong"
    elif score == 3:
        return "⚠️ Moderate Password - Consider adding more security features.", "Moderate"
    else:
        return "\n".join(feedback), "Weak"

# Streamlit UI setup
st.set_page_config(page_title="Password Strength Meter", page_icon="🔐", layout="centered")

# Sidebar for password history
st.sidebar.title("🔑 Password History")
if 'password_history' not in st.session_state:
    st.session_state.password_history = []

# Display the last 5 passwords entered
for i, past_password in enumerate(st.session_state.password_history[-5:], 1):  
    st.sidebar.write(f"{i}. {past_password}")

# Main styling with custom CSS
st.markdown("""
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: #f0f2f6;
            color: #333;
        }
        .title {
            color: #2E86C1;
            text-align: center;
            font-size: 40px;
            font-weight: bold;
            margin-top: 30px;
        }
        .stTextInput>div>div>input {
            text-align: center;
            font-size: 18px;
            padding: 10px;
            border-radius: 8px;
            border: 1px solid #ccc;
        }
        .stButton>button {
            background-color: #2E86C1;
            color: white;
            width: 100%;
            padding: 12px;
            border-radius: 10px;
            font-size: 16px;
            cursor: pointer;
            transition: background-color 0.3s;
        }
        .stButton>button:hover {
            background-color: #1C5988;
        }
        .feedback {
            font-size: 18px;
            color: #555;
            margin-top: 20px;
        }
        .feedback strong {
            color: #D9534F;
        }
    </style>
""", unsafe_allow_html=True)

# Main title
st.markdown('<div class="title">🔐 Password Strength Meter</div>', unsafe_allow_html=True)

st.write("Enter your password below to check its strength:")

# Input for password
password = st.text_input("Enter your password:", type="password", placeholder="Your password here...")

# Button to check the password strength
if st.button("Check Password Strength"):
    if password:
        st.session_state.password_history.append(password)
        result, strength = check_password_strength(password)

        # Display feedback based on strength
        if strength == "Strong":
            st.success(result)
            st.balloons()  # Show balloons for celebration
        elif strength == "Moderate":
            st.warning(result)
        else:
            st.error("Weak Password - Improve it using these tips:")
            for tip in result.split("\n"):
                st.write(tip)
    else:
        st.warning("⚠️ Please enter a password to check.")

# Password generation feature
password_length = st.number_input("Choose password length:", min_value=8, max_value=20, value=12)
if st.button("Generate Strong Password"):
    strong_password = generate_strong_password(password_length)
    st.success(f"Suggested Strong Password: **{strong_password}**")

# ✅ Footer
st.markdown("<hr style='border: 1px solid #ddd;'>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 14px; color: #555;'>🚀 This application is created by <b>Muhammad Yameen Saleem</b></p>", unsafe_allow_html=True)
