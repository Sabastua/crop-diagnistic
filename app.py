import streamlit as st
from google import genai
import PIL.Image
import os
import time
import base64
from io import BytesIO
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini API
api_key = os.getenv("GOOGLE_API_KEY") or st.secrets.get("GOOGLE_API_KEY", "")
if not api_key:
    st.error("Please set your GOOGLE_API_KEY in a .env file or Streamlit secrets.")
    st.stop()

# Initialize GenAI Client
client = genai.Client(api_key=api_key)

# Initialize Session State
if "history" not in st.session_state:
    st.session_state.history = []
if "page" not in st.session_state:
    st.session_state.page = "onboarding"
if "onboarding_step" not in st.session_state:
    st.session_state.onboarding_step = 0

# Page config
st.set_page_config(
    page_title="Smart Crop Doctor",
    page_icon="🌿",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Custom CSS for Stunning Glassmorphism Green & Orange Theme
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Outfit', sans-serif;
    }
    
    .stApp {
        background: radial-gradient(circle at top left, #064e3b, #022c22);
        color: #ffffff;
    }
    
    /* Center the app content */
    .block-container {
        padding-top: 2rem;
        max-width: 800px;
    }

    /* GLASS CARD STYLE */
    .premium-card {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 28px;
        padding: 40px;
        box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
        margin-bottom: 30px;
    }
    
    .history-card {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 20px;
        padding: 24px;
        margin-bottom: 16px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        transition: all 0.3s ease;
    }
    
    .history-card:hover {
        background: rgba(255, 255, 255, 0.08);
        transform: scale(1.02);
    }

    /* BUTTONS - DIMMED PILL STYLE */
    .stButton>button {
        background: linear-gradient(90deg, #16a34a 0%, #15803d 100%);
        color: white !important;
        border-radius: 999px;
        padding: 1rem 2.5rem;
        border: none;
        font-weight: 700;
        font-size: 18px;
        letter-spacing: 0.5px;
        transition: all 0.4s ease;
        width: auto;
        min-width: 220px;
        display: block;
        margin: 1.5rem auto;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 15px rgba(0, 0, 0, 0.3);
        background: linear-gradient(90deg, #15803d 0%, #16a34a 100%);
    }
    
    .orange-button > div > button {
        background: linear-gradient(90deg, #ea580c 0%, #c2410c 100%) !important;
        color: white !important;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2) !important;
    }
    
    .orange-button > div > button:hover {
        box-shadow: 0 10px 15px rgba(0, 0, 0, 0.3) !important;
    }

    /* NAVIGATION / SIDEBAR */
    [data-testid="stSidebar"] {
        background: rgba(2, 44, 34, 0.9);
        backdrop-filter: blur(15px);
        border-right: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    [data-testid="stSidebarNav"] {
        background: transparent;
    }

    /* ONBOARDING */
    .onboarding-slide {
        text-align: center;
        padding: 60px 40px;
    }
    
    .slide-icon {
        font-size: 110px;
        margin-bottom: 30px;
        display: block;
        filter: drop-shadow(0 0 15px rgba(255, 255, 255, 0.3));
    }
    
    h1, h2, h3 {
        color: #ffffff;
        font-weight: 700;
        letter-spacing: -1.5px;
    }
    
    p {
        color: #9ca3af;
        line-height: 1.7;
        font-size: 1.15rem;
    }

    /* INPUTS */
    .stFileUploader {
        background: rgba(255, 255, 255, 0.02);
        border-radius: 20px;
        padding: 30px;
        border: 2px dashed rgba(255, 255, 255, 0.15);
        transition: all 0.3s ease;
    }
    
    .stFileUploader:hover {
        border-color: #22c55e;
        background: rgba(34, 197, 94, 0.02);
    }
</style>
""", unsafe_allow_html=True)

# Helper: Convert PIL to Base64
def img_to_base64(img):
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()

# UI LOGIC: ONBOARDING
if st.session_state.page == "onboarding":
    slides = [
        {"icon": "🌱", "title": "Welcome to Crop Doctor", "text": "The most advanced plant pathology tool for Kenyan farmers. Let's get your crops healthy!"},
        {"icon": "📸", "title": "Snap a Photo", "text": "Simply take a clear photo of the infected leaf or stem. Our AI will analyze the visual symptoms instantly."},
        {"icon": "📝", "title": "Get Expert Advice", "text": "Receive a professional diagnosis, organic treatments, and local chemical solutions tailored for Kenya."},
        {"icon": "🇰🇪", "title": "Available in Swahili", "text": "Break the language barrier. Translate any diagnosis to Swahili with a single click."}
    ]
    
    step = st.session_state.onboarding_step
    
    st.markdown(f"""
    <div class="onboarding-slide">
        <div class="slide-icon">{slides[step]["icon"]}</div>
        <h1>{slides[step]["title"]}</h1>
        <p>{slides[step]["text"]}</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if step < len(slides) - 1:
            if st.button("Next →"):
                st.session_state.onboarding_step += 1
                st.rerun()
        else:
            st.markdown('<div class="orange-button">', unsafe_allow_html=True)
            if st.button("Start Diagnosing 🌿"):
                st.session_state.page = "diagnosis"
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)
    
    # Progress indicator
    st.markdown(f"""
    <div style="text-align: center; margin-top: 20px; color: #9ca3af;">
        {' '.join(['●' if i == step else '○' for i in range(len(slides))])}
    </div>
    """, unsafe_allow_html=True)

# UI LOGIC: DIAGNOSIS
elif st.session_state.page == "diagnosis":
    st.title("🌿 Smart Crop Doctor")
    st.subheader("Fast. Accurate. Localized.")
    
    # Reset/Refresh function in Sidebar
    if st.sidebar.button("🔄 Reset / New Diagnosis"):
        if "diagnosis" in st.session_state:
            del st.session_state.diagnosis
        st.session_state.page = "diagnosis"
        st.rerun()

    uploaded_file = st.file_uploader("Upload or Capture Image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = PIL.Image.open(uploaded_file)
        st.image(image, caption="Current Plant Sample", use_column_width=True)
        
        st.markdown('<div class="orange-button">', unsafe_allow_html=True)
        identify_btn = st.button("🚀 Analyze Plant Health")
        st.markdown('</div>', unsafe_allow_html=True)
        
        if identify_btn:
            with st.spinner("Analyzing plant health... Please wait."):
                try:
                    prompt = """
                    You are a Senior Plant Pathologist specializing in East African agriculture. Analyze the provided image.
                    First, identify the crop species.
                    Second, perform a visual audit of the leaves/stems (look for chlorosis, necrosis, or pest eggs).
                    Third, provide a diagnosis. If unsure, give the top 2 possibilities.
                    Fourth, provide actionable advice using locally available solutions in Kenya.
                    
                    Keep the tone supportive and professional.
                    
                    Output Formatting:
                    Please structure your response exactly as follows:
                    # Diagnosis: [Crop Name] - [Disease/Pest]
                    [Short summary]
                    
                    ## Severity
                    [Low/Medium/High] - [Short justification]
                    
                    ## Recommended Actions (Organic)
                    [List natural or cultural control methods]
                    
                    ## Recommended Actions (Chemical)
                    [Suggest active ingredients common in Kenyan agricultural stores, e.g., Copper-based fungicides]
                    
                    ## Preventative Measures
                    [Crop rotation or specific fertilizer needs]
                    """
                    
                    response = client.models.generate_content(
                        model='gemini-flash-latest',
                        contents=[prompt, image]
                    )
                    
                    st.session_state.diagnosis = response.text
                    st.session_state.translated = False
                    
                    # Save to History
                    st.session_state.history.append({
                        "timestamp": time.strftime("%Y-%m-%d %H:%M"),
                        "image": img_to_base64(image),
                        "diagnosis": response.text
                    })
                    
                except Exception as e:
                    st.error(f"Error during diagnosis: {str(e)}")

    # Display results
    if 'diagnosis' in st.session_state:
        st.markdown("---")
        
        # Translation Toggle
        col1, col2 = st.columns([0.7, 0.3])
        with col1:
            st.subheader("Pathologist Results")
        with col2:
            if st.button("Translate to Swahili 🇰🇪"):
                with st.spinner("Translating..."):
                    translate_prompt = f"Translate the following agricultural diagnosis into Swahili, maintaining the professional and supportive tone: \n\n{st.session_state.diagnosis}"
                    trans_response = client.models.generate_content(
                        model='gemini-flash-latest',
                        contents=translate_prompt
                    )
                    st.session_state.swahili_diagnosis = trans_response.text
                    st.session_state.translated = True
        
        # Show diagnosis
        display_text = st.session_state.swahili_diagnosis if st.session_state.get('translated', False) else st.session_state.diagnosis
        st.markdown(f'<div class="premium-card">{display_text}</div>', unsafe_allow_html=True)
        
        if st.session_state.get('translated', False):
            if st.button("← Back to English"):
                st.session_state.translated = False
                st.rerun()

# UI LOGIC: HISTORY
elif st.session_state.page == "history":
    st.title("📜 Diagnosis History")
    st.markdown("Review your past crop health checks below.")
    
    if not st.session_state.history:
        st.info("No history yet. Start diagnosing your crops to see them here!")
    else:
        for idx, item in enumerate(reversed(st.session_state.history)):
            timestamp = item["timestamp"]
            diagnosis = item["diagnosis"]
            
            # Extract title from diagnosis if possible
            title = diagnosis.split('\n')[0].replace('# ', '').replace('Diagnosis: ', '')
            
            with st.expander(f"📌 {timestamp} | {title}"):
                col1, col2 = st.columns([0.3, 0.7])
                with col1:
                    # Display saved base64 image
                    img_data = base64.b64decode(item["image"])
                    st.image(img_data)
                with col2:
                    st.markdown(diagnosis)

# SIDEBAR NAVIGATION
st.sidebar.title("Doctor's Menu")
if st.sidebar.button("🩺 New Diagnosis"):
    st.session_state.page = "diagnosis"
    st.rerun()

if st.sidebar.button("📜 View History"):
    st.session_state.page = "history"
    st.rerun()

if st.sidebar.button("💡 How to Use"):
    st.session_state.page = "onboarding"
    st.session_state.onboarding_step = 0
    st.rerun()

st.sidebar.markdown("---")
st.sidebar.info("Tip: Use high-resolution photos in bright sunlight for the best diagnosis.")
