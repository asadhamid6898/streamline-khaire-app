import streamlit as st

# Set page config
st.set_page_config(
    page_title="Privacy Policy - Khaire Health",
    page_icon="🔬",
    layout="wide"
)

# Header
st.markdown("""
<div style="text-align: center;">
    <h1>Privacy Policy</h1>
</div>
""", unsafe_allow_html=True)

# Privacy Policy Content
st.markdown("""
## Effective Date: January 1, 2023

At Khaire Health, we take your privacy and the security of your medical information very seriously. This Privacy Policy explains how we collect, use, disclose, and safeguard your information when you use our retinal analysis service.

### Information We Collect

#### 1. Retinal Images
- Retinal fundus images that you upload to our platform
- Metadata associated with these images (time, date, device information)

#### 2. Analysis Results
- Health condition predictions generated from your retinal images
- Risk scores and assessments derived from our analysis

#### 3. Technical Information
- Browser and device information
- IP address and usage data
- Cookies and similar tracking technologies

### How We Use Your Information

We use the information we collect to:

- Analyze your retinal images and provide health insights
- Improve our machine learning models and algorithms
- Enhance the functionality and user experience of our service
- Ensure the security and integrity of our platform
- Comply with applicable laws and regulations

### Data Protection

We implement a variety of security measures to maintain the safety of your personal information:

- All retinal images and health data are encrypted both in transit and at rest
- We use secure cloud infrastructure with industry-standard protections
- Access to user data is strictly limited and monitored
- Regular security audits and updates

### User Rights

You have the right to:

- Access the personal data we hold about you
- Request correction of inaccurate data
- Request deletion of your data (subject to any legal obligations)
- Download your data in a portable format
- Withdraw consent for future analysis

### Data Retention

We retain your retinal images and analysis results for a period of 90 days after your last interaction with our service, after which they are automatically deleted unless you request otherwise.

### Third-Party Sharing

We do not sell your personal information to third parties. We may share anonymized, aggregated data for research purposes only with your explicit consent.

### Changes to This Policy

We may update this Privacy Policy from time to time. We will notify you of any changes by posting the new Privacy Policy on this page and updating the effective date.

### Children's Privacy

Our service is not intended for individuals under the age of 18. We do not knowingly collect data from children.

### Disclaimer on Medical Advice

Khaire Health is designed to provide information and is not a substitute for professional medical advice, diagnosis, or treatment. Always seek the advice of your physician or other qualified health provider with any questions you may have regarding a medical condition.

### Contact Us

If you have any questions about this Privacy Policy, please contact us at:

- Email: privacy@khairehealth.com
- Address: 123 Health Avenue, Suite 456, Medical District, CA 90000

""")

# Back to home button
if st.button("Back to Home"):
    st.switch_page("app.py")
