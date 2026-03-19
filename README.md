# 🌿 Smart Crop Doctor

**Smart Crop Doctor** is a high-impact, AI-driven plant pathology tool designed specifically for East African agriculture, with a focus on Kenyan farmers. By combining the multimodal reasoning of Google's Gemini API with a modern, glassmorphism-inspired web interface, this app empowers farmers to diagnose crop diseases instantly and receive localized treatment plans.

---

## ✨ Features

- **🚀 AI Multimodal Diagnosis**: Upload or capture an image of a plant leaf/stem for near-instant diagnosis using `gemini-flash-latest`.
- **🧪 Expert Pathology Persona**: The AI acts as a Senior Plant Pathologist specializing in East African crops (Maize, Wheat, Coffee, etc.).
- **🇰🇪 Localized Prescriptions**: Treatment plans include both Organic/Cultural controls and Chemical active ingredients available in Kenyan agricultural stores.
- **🗣️ Swahili Translation**: One-click translation ensures accessibility for all farmers.
- **📜 Diagnosis History**: A dedicated history page to track and review past plant health checks.
- **💎 Premium UX**: A stunning **Glassmorphism** dark-themed UI built for high visual impact and smooth interaction.

---

## 🛠️ How It's Built

- **Frontend**: [Streamlit](https://streamlit.io/) — A mobile-first, responsive web framework.
- **AI Core**: [Google GenAI SDK](https://github.com/google-gemini/generative-ai-python) — Leveraging Gemini 1.5/2.0 Flash models for multimodal inference.
- **Styling**: Custom CSS for high-end Glassmorphism (blur effects, gradients, and soft shadows).
- **Environment**: Python-based with `python-dotenv` for secure API key management.

---

## 🚀 Getting Started

### 1. Prerequisites
Ensure you have Python 3.9+ installed.

### 2. Clone the Repository
```bash
git clone https://github.com/Sabastua/crop-diagnistic.git
cd crop-diagnistic
```

### 3. Install Dependencies
```bash
pip3 install -r requirements.txt
```

### 4. Configure API Key
Create a `.env` file in the root directory and add your Google AI Studio API key:
```bash
GOOGLE_API_KEY=your_actual_api_key_here
```
*Get your free API key at [Google AI Studio](https://aistudio.google.com/).*

### 5. Run the Application
```bash
python3 -m streamlit run app.py
```

---

## 📸 Screenshots & Usage
1. **Onboarding**: Start with a quick interactive guide on how to use the app.
2. **Diagnosis**: Upload an image, click "Analyze", and wait for the AI Pathologist to provide a structured result.
3. **Translation**: Toggle Swahili if you prefer localized instructions.
4. **History**: Revisit any previous diagnosis from the sidebar menu.

---

## ⚠️ Disclaimer
*The diagnosis provided by this AI tool is for informational purposes only. Farmers are encouraged to consult with local agricultural extension officers or certified pathologists for critical decision-making.*

---
Built with ❤️ for Kenyan Agriculture.
