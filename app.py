import streamlit as st
import re

def check_password_strength(password):
    # Initialize score and feedback
    score = 0
    feedback = []
    
    # Check length
    if len(password) >= 12:
        score += 2
        feedback.append("✅ Good length (12+ characters)")
    elif len(password) >= 8:
        score += 1
        feedback.append("⚠️ Decent length (8+ characters)")
    else:
        feedback.append("❌ Password too short (less than 8 characters)")
    
    # Check for numbers
    if re.search(r"\d", password):
        score += 1
        feedback.append("✅ Contains numbers")
    else:
        feedback.append("❌ No numbers")
    
    # Check for uppercase letters
    if re.search(r"[A-Z]", password):
        score += 1
        feedback.append("✅ Contains uppercase letters")
    else:
        feedback.append("❌ No uppercase letters")
    
    # Check for lowercase letters
    if re.search(r"[a-z]", password):
        score += 1
        feedback.append("✅ Contains lowercase letters")
    else:
        feedback.append("❌ No lowercase letters")
    
    # Check for special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
        feedback.append("✅ Contains special characters")
    else:
        feedback.append("❌ No special characters")
    
    return score, feedback

def main():
    st.title("Password Strength Meter")
    st.write("Check How Strong Your Password Is!")
    
    # Password input
    password = st.text_input("Enter your password", type="password")
    
    if password:
        score, feedback = check_password_strength(password)
        
        # Display strength meter
        st.write("### Password Strength")
        
        # Calculate percentage
        strength_percentage = (score / 6) * 100
        
        # Display progress bar
        st.progress(strength_percentage / 100)
        
        # Display strength level
        if score <= 2:
            st.error("Weak Password")
        elif score <= 4:
            st.warning("Moderate Password")
        else:
            st.success("Strong Password")
        
        # Display feedback
        st.write("### Detailed Feedback")
        for item in feedback:
            st.write(item)
        
        # Display score
        st.write(f"Score: {score}/6")

if __name__ == "__main__":
    main() 