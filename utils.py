import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from PIL import Image, ImageEnhance, ImageFilter
import io
import base64

def preprocess_image(image):
    """
    Preprocess the uploaded retinal image for better analysis.
    
    Args:
        image (PIL.Image): The uploaded retinal image
        
    Returns:
        PIL.Image: Processed image ready for analysis
    """
    # Resize image to a standard size if needed
    target_size = (512, 512)
    image = image.resize(target_size)
    
    # Convert to RGB if needed
    if image.mode != "RGB":
        image = image.convert("RGB")
    
    # Enhance contrast to make retinal features more visible
    enhancer = ImageEnhance.Contrast(image)
    enhanced_image = enhancer.enhance(1.2)
    
    # Apply slight sharpening to enhance edge details
    sharpened_image = enhanced_image.filter(ImageFilter.SHARPEN)
    
    return sharpened_image

def create_risk_gauge(risk_score, title):
    """
    Create a gauge chart to visualize risk scores.
    
    Args:
        risk_score (float): Risk score between 0-100
        title (str): Title for the gauge chart
    """
    # Ensure risk_score is within bounds
    risk_score = max(0, min(100, risk_score))
    
    # Define color based on risk level
    if risk_score < 30:
        color = "green"
    elif risk_score < 70:
        color = "orange"
    else:
        color = "red"
    
    # Create gauge chart
    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = risk_score,
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': title},
        gauge = {
            'axis': {'range': [0, 100], 'tickwidth': 1, 'tickcolor': "darkblue"},
            'bar': {'color': color},
            'bgcolor': "white",
            'borderwidth': 2,
            'bordercolor': "gray",
            'steps': [
                {'range': [0, 30], 'color': 'lightgreen'},
                {'range': [30, 70], 'color': 'lightyellow'},
                {'range': [70, 100], 'color': 'lightcoral'}
            ],
        }
    ))
    
    fig.update_layout(height=250, margin=dict(l=20, r=20, t=50, b=20))
    st.plotly_chart(fig, use_container_width=True)

def create_health_score_chart(health_score, title):
    """
    Create a chart to visualize health scores.
    
    Args:
        health_score (float): Health score between 0-100
        title (str): Title for the chart
    """
    # Ensure health_score is within bounds
    health_score = max(0, min(100, health_score))
    
    # Define categories based on score
    if health_score < 40:
        category = "Concern"
        color = "red"
    elif health_score < 70:
        category = "Moderate"
        color = "orange"
    else:
        category = "Good"
        color = "green"
    
    # Create the gauge chart
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=health_score,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': title},
        gauge={
            'axis': {'range': [0, 100], 'tickwidth': 1, 'tickcolor': "darkblue"},
            'bar': {'color': color},
            'bgcolor': "white",
            'borderwidth': 2,
            'bordercolor': "gray",
            'steps': [
                {'range': [0, 40], 'color': 'lightcoral'},
                {'range': [40, 70], 'color': 'lightyellow'},
                {'range': [70, 100], 'color': 'lightgreen'}
            ],
        }
    ))
    
    fig.update_layout(height=250, margin=dict(l=20, r=20, t=50, b=20))
    st.plotly_chart(fig, use_container_width=True)
    st.markdown(f"**Health Category**: {category}")

def display_condition_descriptions():
    """Display descriptions of the health conditions being analyzed."""
    conditions = {
        "Alzheimer's/Dementia": "Retinal changes can indicate early signs of Alzheimer's and dementia. Specific vascular patterns and thinning of retinal layers have been linked to cognitive decline.",
        
        "Neurological Health": "The retina is considered an extension of the brain and shares similar tissue. Changes in retinal blood vessels can reflect overall neurological health.",
        
        "Diabetes": "Diabetes affects blood vessels throughout the body, including those in the retina. Early changes can be detected before clinical symptoms appear.",
        
        "Blood Pressure": "Hypertension causes characteristic changes to retinal arteries and veins. The ratio of artery to vein width and arterial narrowing can indicate hypertension severity.",
        
        "Diabetic Retinopathy": "A complication of diabetes that damages retinal blood vessels, causing them to leak fluid or bleed, potentially leading to vision loss.",
        
        "Age-related Macular Degeneration": "A condition affecting the macula (central retina), causing blurred or reduced central vision. Retinal imaging can detect early signs before symptoms appear."
    }
    
    for condition, description in conditions.items():
        with st.expander(condition):
            st.markdown(description)

def get_image_download_link(img, filename, text):
    """
    Generate a download link for an image
    
    Args:
        img (PIL.Image): Image to be downloaded
        filename (str): Filename for the download
        text (str): Text to display for the download link
    
    Returns:
        str: HTML download link
    """
    buffered = io.BytesIO()
    img.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    href = f'<a href="data:file/jpg;base64,{img_str}" download="{filename}">{text}</a>'
    return href
