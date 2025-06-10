import streamlit as st
import pandas as pd
import numpy as np
import io
from Pillow import Image
import time
import utils
import model
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

@st.cache_resource
def load_fundus_model():
    model = load_model("fundus_verifier.h5")  # or "models/fundus_verifier.h5"
    return model

fundus_model = load_fundus_model()

def verify_fundus(img):
    img = img.resize((224, 224)).convert('RGB')
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0
    pred = fundus_model.predict(img_array)[0][0]
    return pred >= 0.5

# Set page configuration
st.set_page_config(
    page_title="Khaire Health - Retinal Analyzer",
    page_icon="🧠",
    layout="centered",
)

# Initialize session state variables if they don't exist
if 'uploaded_image' not in st.session_state:
    st.session_state.uploaded_image = None
if 'processed_image' not in st.session_state:
    st.session_state.processed_image = None
if 'analysis_results' not in st.session_state:
    st.session_state.analysis_results = None
if 'show_results' not in st.session_state:
    st.session_state.show_results = False

# Main application header
st.markdown("""
    <div style='text-align: center'>
        <h1 style='color:#4CAF50;'>Khaire Health</h1>
        <h4>Your AI Assistant for Retinal and Neurological Analysis</h4>
    </div>
""", unsafe_allow_html=True)

st.markdown("---")

# Main layout
col1, col2 = st.columns([1, 2])

with col1:
    st.markdown("### Upload Retinal Image")
    
    # Image upload area
    uploaded_file = st.file_uploader(
        "Upload a retinal fundus image",
        type=["jpg", "jpeg", "png"],
        help="Upload a clear image of the retinal fundus taken with a smartphone camera or retinal imaging device."
    )
    
    # If an image is uploaded
    if uploaded_file is not None:
        try:
            # Read and display the image
            img = Image.open(uploaded_file)

            if not verify_fundus(img):
                st.error("❌ Not a valid fundus photo. Please upload a clear image.")
                st.stop()
            
            st.success("✔️ Fundus image verified. Proceeding with diagnosis...")
                    image = Image.open(uploaded_file)
                    st.session_state.uploaded_image = image
                    st.image(image, caption="Uploaded Image", use_column_width=True)
                    
            # Process image button
            if st.button("Analyze Image"):
                with st.spinner("Processing image..."):
                    # Preprocess the image
                    processed_img = utils.preprocess_image(image)
                    st.session_state.processed_image = processed_img
                    
                    # Get predictions from model
                    results = model.predict_health_conditions(processed_img)
                    st.session_state.analysis_results = results
                    st.session_state.show_results = True
                    st.success("Analysis complete!")
                    st.rerun()
        
        except Exception as e:
            st.error(f"Error processing image: {e}")
            st.session_state.uploaded_image = None

    # Display guidelines
    with st.expander("Image Guidelines"):
        st.markdown("""
        - Upload a clear, well-focused image of the retina
        - The image should capture the entire retinal fundus area
        - Avoid blurry or poorly lit images for accurate results
        - Images should be taken in a well-lit environment
        """)

with col2:
    if st.session_state.show_results and st.session_state.analysis_results is not None:
        st.markdown("## Analysis Results")
        
        # Display the processed image if available
        if st.session_state.processed_image is not None:
            st.image(
                st.session_state.processed_image, 
                caption="Processed Retinal Image", 
                use_column_width=True
            )
        
        results = st.session_state.analysis_results
        
        # Create tabs for different categories of results
        tab1, tab2, tab3 = st.tabs(["Health Risks", "Ocular Conditions", "Demographics"])
        
        with tab1:
            st.markdown("### Health Risk Assessment")
            
            # Alzheimer's/Dementia risk
            st.markdown("#### Alzheimer's/Dementia Risk")
            alzheimer_risk = results.get("alzheimer_risk", {})
            risk_level = alzheimer_risk.get("risk_level", "N/A")
            risk_score = alzheimer_risk.get("risk_score", 0)
            
            # Create a gauge chart for the risk
            utils.create_risk_gauge(risk_score, "Alzheimer's Risk Score")
            st.markdown(f"**Risk Level**: {risk_level}")
            
            # Neurological health score
            st.markdown("#### Neurological Health")
            neuro_health = results.get("neurological_health", {})
            neuro_score = neuro_health.get("score", 0)
            neuro_status = neuro_health.get("status", "N/A")
            
            utils.create_health_score_chart(neuro_score, "Neurological Health Score")
            st.markdown(f"**Status**: {neuro_status}")
            
            # Diabetes
            st.markdown("#### Diabetes Indicators")
            diabetes = results.get("diabetes", {})
            diabetes_risk = diabetes.get("risk_level", "N/A")
            diabetes_confidence = diabetes.get("confidence", 0)
            
            # Use proper float value for progress bar (0.0 to 1.0)
            st.progress(float(diabetes_confidence)/100.0, text=f"Confidence: {diabetes_confidence:.1f}%")
            st.markdown(f"**Risk Level**: {diabetes_risk}")
            
            # Blood pressure
            st.markdown("#### Blood Pressure Indicators")
            bp = results.get("blood_pressure", {})
            bp_status = bp.get("status", "N/A")
            bp_systolic = bp.get("systolic_estimate", "N/A")
            bp_diastolic = bp.get("diastolic_estimate", "N/A")
            
            st.markdown(f"**Status**: {bp_status}")
            st.markdown(f"**Estimated Range**: {bp_systolic}/{bp_diastolic} mmHg")
        
        with tab2:
            st.markdown("### Ocular Conditions")
            
            # Glaucoma Assessment
            st.markdown("#### Glaucoma")
            glaucoma = results.get("glaucoma", {})
            glaucoma_status = glaucoma.get("status", "N/A")
            glaucoma_confidence = glaucoma.get("confidence", 0)
            glaucoma_ratio = glaucoma.get("cup_to_disc_ratio", "N/A")
            
            # Display the glaucoma-processed image with optic cup detection
            if "processed_image" in glaucoma and glaucoma["processed_image"] is not None:
                st.image(
                    glaucoma["processed_image"], 
                    caption="Optic Cup Detection", 
                    use_container_width=True
                )
            
            # Use proper float value for progress bar (0.0 to 1.0)
            st.progress(float(glaucoma_confidence)/100.0, text=f"Confidence: {glaucoma_confidence:.1f}%")
            st.markdown(f"**Risk Level**: {glaucoma_status}")
            
            if glaucoma_ratio != "N/A":
                st.markdown(f"**Cup-to-Disc Ratio**: {glaucoma_ratio}")
                st.markdown("""
                *Cup-to-disc ratio is an important indicator for glaucoma. A higher ratio may 
                indicate increased risk of glaucoma.*
                """)
            
            # Diabetic Retinopathy
            st.markdown("#### Diabetic Retinopathy")
            dr = results.get("diabetic_retinopathy", {})
            dr_stage = dr.get("stage", "N/A")
            dr_confidence = dr.get("confidence", 0)
            
            # Use proper float value for progress bar (0.0 to 1.0)
            st.progress(float(dr_confidence)/100.0, text=f"Confidence: {dr_confidence:.1f}%")
            st.markdown(f"**Stage**: {dr_stage}")
            
            # Age-related Macular Degeneration
            st.markdown("#### Age-related Macular Degeneration (AMD)")
            amd = results.get("amd", {})
            amd_status = amd.get("status", "N/A")
            amd_confidence = amd.get("confidence", 0)
            
            # Use proper float value for progress bar (0.0 to 1.0)
            st.progress(float(amd_confidence)/100.0, text=f"Confidence: {amd_confidence:.1f}%")
            st.markdown(f"**Status**: {amd_status}")
            
            # Other retinal conditions
            if "other_conditions" in results:
                st.markdown("#### Other Detected Conditions")
                other = results.get("other_conditions", [])
                if other:
                    for condition in other:
                        st.markdown(f"- {condition}")
                else:
                    st.markdown("No other conditions detected")
        
        with tab3:
            st.markdown("### Demographic Predictions")
            demographics = results.get("demographics", {})
            
            # Predicted age
            age = demographics.get("age", "N/A")
            age_range = demographics.get("age_range", "N/A")
            st.markdown(f"**Estimated Age**: {age} years (Range: {age_range})")
            
            # Gender
            gender = demographics.get("gender", "N/A")
            gender_confidence = demographics.get("gender_confidence", 0)
            st.markdown(f"**Predicted Gender**: {gender} (Confidence: {gender_confidence:.1f}%)")
            
            # Ethnicity
            ethnicity = demographics.get("ethnicity", "N/A")
            ethnicity_confidence = demographics.get("ethnicity_confidence", 0)
            st.markdown(f"**Predicted Ethnicity**: {ethnicity} (Confidence: {ethnicity_confidence:.1f}%)")
        
        # Important disclaimer
        st.markdown("---")
        st.markdown("""
        **IMPORTANT DISCLAIMER**: These results are preliminary and for informational purposes only. 
        They are not a substitute for professional medical advice, diagnosis, or treatment. 
        Always seek the advice of your physician or other qualified health provider with any 
        questions you may have regarding a medical condition.
        """)
        
        # Option to download results
        if st.button("Download Results as PDF"):
            with st.spinner("Generating PDF..."):
                # Simulate PDF generation
                time.sleep(2)
                st.success("PDF report generated!")
                # In a real implementation, generate a PDF and provide download link
    
    else:
        # Show introductory content when no analysis is being displayed
        st.markdown("""
        ## Welcome to Khaire Health
        
        Our advanced retinal analysis platform uses machine learning to detect early signs of various health conditions from retinal fundus images.
        
        ### How it works:
        1. Upload a clear image of your retinal fundus (taken with a smartphone camera or retinal imaging device)
        2. Our AI analyzes the image for biomarkers associated with various health conditions
        3. View your personalized health insights based on retinal analysis
        
        ### What we can detect:
        - Glaucoma
        - Early signs of Alzheimer's/Dementia risk
        - Diabetic Retinopathy
        - Age-related Macular Degeneration (AMD)
        
        Upload an image to get started!
        """)
        
        # Display a sample analysis visualization
        st.markdown("### Key Features in Fundus Photos")
        st.image("https://pub.mdpi-res.com/diagnostics/diagnostics-13-02180/article_deploy/html/images/diagnostics-13-02180-g001.png?1687787357", 
                 caption="Sample visualization (for illustration only)")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center;">
    <p>© 2023 Khaire Health | <a href="/privacy">Privacy Policy</a> | <a href="/about">About</a> | <a href="/info">Health Information</a></p>
</div>
""", unsafe_allow_html=True)
