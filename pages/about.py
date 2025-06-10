import streamlit as st
from Pillow import Image
import model

# Set page config
st.set_page_config(
    page_title="About KHAIRE Health",
    page_icon="🔬",
    layout="wide"
)

# Header with logo
st.markdown("""
<div style="text-align: center;">
    <h1>About Khaire Health</h1>
</div>
""", unsafe_allow_html=True)

# Main content
st.markdown("""
## Our Mission

Khaire Health is dedicated to making advanced health screening accessible through non-invasive retinal image analysis. Our platform uses cutting-edge machine learning algorithms to analyze retinal fundus images and identify early biomarkers of various health conditions.

## The Science Behind Retinal Analysis

The retina is a unique part of the body where blood vessels can be directly observed non-invasively. As an extension of the brain and sharing similar tissue characteristics, the retina provides a window into your overall health.

### Why Retinal Imaging?

- **Non-invasive**: No blood draws or invasive procedures required
- **Cost-effective**: More affordable than many traditional diagnostic tests
- **Early detection**: Can identify disease biomarkers before symptoms appear
- **Multi-condition screening**: A single retinal image can provide insights into multiple health conditions

## Our Technology

Our platform utilizes advanced deep learning models trained on extensive datasets of annotated retinal images.

""")

# Display the model versions
model_versions = model.get_model_versions()
st.markdown("### Current Model Versions")

# Create two columns
col1, col2 = st.columns(2)

# Distribute the model versions between the two columns
for i, (model_name, version) in enumerate(model_versions.items()):
    # Format the model name for display
    display_name = model_name.replace("_", " ").title().replace("Model", "")
    
    # Assign to column based on index
    if i % 2 == 0:
        col1.markdown(f"- **{display_name}**: {version}")
    else:
        col2.markdown(f"- **{display_name}**: {version}")

st.markdown("""
## Research Foundation

Our technology is built on peer-reviewed research demonstrating correlations between retinal biomarkers and systemic health conditions:

- **Alzheimer's Disease**: Studies have shown that retinal nerve fiber layer thinning and vascular changes can precede cognitive symptoms by several years.

- **Diabetes**: Characteristic changes in retinal blood vessels can be detected before clinical diagnosis of diabetes.

- **Cardiovascular Health**: The arrangement and condition of retinal blood vessels are strongly associated with cardiovascular health status.

- **Neurological Health**: The retina develops from the same tissue as the brain during embryonic development, making it a reliable proxy for assessing neural health.

## Our Team

Khaire Health was founded by a multidisciplinary team of ophthalmologists, neurologists, data scientists, and software engineers committed to making healthcare more accessible and preventative.

## Contact Information

For questions, partnerships, or more information:

- **Email**: contact@khairehealth.com

""")

# Back to home button
if st.button("Back to Home"):
    st.switch_page("app.py")
