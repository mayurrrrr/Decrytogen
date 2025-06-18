import streamlit as st
import joblib
import pandas as pd
import numpy as np

# Set page configuration
st.set_page_config(
    page_title="Personality Type Predictor",
    page_icon="🧠",
    layout="wide"
)

# Improved CSS for dark mode
st.markdown("""
<style>
    body, .stApp {
        background-color: #18191a !important;
    }
    .main-header {
        font-size: 3rem;
        color: #fff !important;
        text-align: center;
        margin-bottom: 2rem;
        font-weight: bold;
        letter-spacing: 1px;
        text-shadow: 0 2px 8px #2228, 0 1px 0 #0004;
    }
    .intro-section {
        background: linear-gradient(90deg, #232526 0%, #414345 100%);
        color: #fff !important;
        padding: 2rem;
        border-radius: 12px;
        margin-bottom: 2rem;
        box-shadow: 0 2px 8px #0004;
        border: 1px solid #333;
    }
    .feature-section {
        background-color: #232526;
        color: #fff !important;
        padding: 1.5rem;
        border-radius: 8px;
        box-shadow: 0 2px 4px #0002;
        margin: 1rem 0;
        border: 1px solid #333;
    }
    .prediction-box {
        background-color: #232526;
        color: #fff !important;
        padding: 2rem;
        border-radius: 10px;
        border-left: 5px solid #1f77b4;
        margin: 1rem 0;
        box-shadow: 0 2px 8px #0002;
        border: 1px solid #333;
    }
    h2, h3, h4, p, label, .st-emotion-cache-1v0mbdj, .st-emotion-cache-1c7y2kd, .stMarkdown, .stMarkdown p {
        color: #fff !important;
    }
</style>
""", unsafe_allow_html=True)

@st.cache_resource
def load_model():
    """Load the pre-trained model from joblib file"""
    try:
        model = joblib.load('model/best_logistic_regression_model.joblib')
        return model
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None

def preprocess_input(stage_fear, drained_after_socializing):
    """
    Convert user inputs to the format expected by the model
    The model expects only 4 one-hot encoded features
    """
    # Initialize features dictionary with the 4 features the model expects
    features = {
        'Drained_after_socializing_No': 0.0,
        'Drained_after_socializing_Yes': 0.0,
        'Stage_fear_No': 0.0,
        'Stage_fear_Yes': 0.0
    }
    
    # Set one-hot encoded values for categorical features
    if drained_after_socializing == 'Yes':
        features['Drained_after_socializing_Yes'] = 1.0
    else:
        features['Drained_after_socializing_No'] = 1.0
        
    if stage_fear == 'Yes':
        features['Stage_fear_Yes'] = 1.0
    else:
        features['Stage_fear_No'] = 1.0
    
    return features

def make_prediction(model, features):
    """Make prediction using the loaded model"""
    try:
        # Convert features to DataFrame
        input_df = pd.DataFrame([features])
        
        # Make prediction
        prediction = model.predict(input_df)[0]
        
        return prediction
    except Exception as e:
        st.error(f"Error making prediction: {e}")
        return None

def main():
    # Header
    st.markdown('<h1 class="main-header">🧠 Personality Type Predictor</h1>', unsafe_allow_html=True)
    
    # Introduction
    st.markdown("""
    <div class="intro-section">
        <h2>Welcome to the Personality Type Predictor!</h2>
        <p>This application uses <b>machine learning</b> to predict whether you are an <b>Introvert</b> or <b>Extrovert</b> based on your responses to two key questions about social interactions and stage presence.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Load model
    model = load_model()
    
    if model is None:
        st.error("Failed to load the model. Please check if the model file exists.")
        return
    
    # Create input form
    st.markdown('<h2>📝 Answer These Questions</h2>', unsafe_allow_html=True)
    
    with st.form("personality_form"):
        # Only show the two dropdowns, side by side, with no extra columns or empty boxes
        col1, col2 = st.columns(2)
        
        with col1:
            drained_after_socializing = st.selectbox(
                "Do you feel drained after socializing?",
                options=['Yes', 'No'],
                help="Do you typically feel tired or exhausted after social interactions?"
            )
        
        with col2:
            stage_fear = st.selectbox(
                "Do you experience stage fear?",
                options=['Yes', 'No'],
                help="Do you feel nervous or anxious about speaking in front of groups?"
            )
        
        # Submit button
        submit_button = st.form_submit_button(
            "🔮 Predict My Personality Type",
            use_container_width=True
        )
    
    # Handle form submission
    if submit_button:
        st.markdown('<h2>🎯 Prediction Results</h2>', unsafe_allow_html=True)
        
        # Show user inputs
        
        st.write("**Your Responses:**")
        st.write(f"- Feel drained after socializing: **{drained_after_socializing}**")
        st.write(f"- Experience stage fear: **{stage_fear}**")
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Preprocess input
        features = preprocess_input(stage_fear, drained_after_socializing)
        
        # Make prediction
        with st.spinner("Analyzing your personality..."):
            prediction = make_prediction(model, features)
        
        if prediction is not None:
            # Display prediction with styling
            if prediction == 'Introvert':
                st.markdown("""
                <div class="prediction-box">
                    <h3>🎭 Your Predicted Personality Type: <span style="color: #2E86AB;">Introvert</span></h3>
                    <p>You tend to prefer solitary activities and may feel more energized when spending time alone. 
                    You likely think before speaking and prefer deep, meaningful conversations over small talk.</p>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown("""
                <div class="prediction-box">
                    <h3>🎭 Your Predicted Personality Type: <span style="color: #A23B72;">Extrovert</span></h3>
                    <p>You tend to be energized by social interactions and may feel more alive when around others. 
                    You likely think out loud and enjoy being the center of attention in group settings.</p>
                </div>
                """, unsafe_allow_html=True)
            
            # Add confidence note
            st.info("💡 **Note:** This prediction is based on a machine learning model trained on specific behavioral patterns. Personality is complex and exists on a spectrum - this is just one perspective!")
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #fff;">
        <p>Built by Mayur Arvindh</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main() 