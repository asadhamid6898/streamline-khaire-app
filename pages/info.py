import streamlit as st
import model

# Set page config
st.set_page_config(
    page_title="Health Information - Khaire Health",
    page_icon="🔬",
    layout="wide"
)

# Header
st.markdown("""
<div style="text-align: center;">
    <h1>Health Information</h1>
    <h3>Understanding Conditions Detected by Retinal Analysis</h3>
</div>
""", unsafe_allow_html=True)

# Tabs for different conditions
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "Alzheimer's/Dementia", 
    "Neurological Health", 
    "Diabetes", 
    "Blood Pressure",
    "Diabetic Retinopathy",
    "AMD"
])

# Alzheimer's/Dementia Tab
with tab1:
    alzheimers_info = model.get_condition_info("alzheimers")
    
    st.markdown(f"## {alzheimers_info['name']}")
    
    st.markdown(f"### Overview")
    st.markdown(alzheimers_info['description'])
    
    st.markdown("### Retinal Biomarkers")
    for indicator in alzheimers_info['retinal_indicators']:
        st.markdown(f"- {indicator}")
    
    st.markdown("### Connection to Retinal Health")
    st.markdown("""
    Recent research has established a strong connection between retinal changes and Alzheimer's disease. The retina is considered an extension of the central nervous system and shares many similarities with brain tissue.
    
    Studies have shown that:
    
    - Thinning of the retinal nerve fiber layer (RNFL) correlates with cognitive decline
    - Changes in retinal blood vessel patterns can predict onset of Alzheimer's years before symptoms appear
    - Specific protein deposits similar to those found in the brain can sometimes be detected in the retina
    
    ### Early Detection
    
    Detecting these changes early can help with:
    
    - Earlier intervention with lifestyle modifications
    - Monitoring disease progression
    - Potential enrollment in clinical trials
    - Development of treatment plans
    """)
    
    st.markdown(f"### Current Research Status")
    st.markdown(alzheimers_info['research_status'])

# Neurological Health Tab
with tab2:
    st.markdown("## Neurological Health")
    
    st.markdown("### Overview")
    st.markdown("""
    Neurological health encompasses the well-being of the brain, spinal cord, and the complex network of nerves throughout the body. The retina serves as a unique window into the central nervous system.
    """)
    
    st.markdown("### Retinal Biomarkers")
    st.markdown("""
    - Retinal nerve fiber layer thickness
    - Ganglion cell complex integrity
    - Vascular network complexity and health
    - Presence of microhemorrhages
    """)
    
    st.markdown("### Connection to Retinal Health")
    st.markdown("""
    The retina is embryologically derived from the diencephalon and is considered part of the central nervous system. This makes it uniquely positioned as a biomarker for neurological conditions:
    
    - Changes in retinal neurons often mirror changes in brain neurons
    - Vascular health in the retina correlates with cerebrovascular health
    - Neurodegenerative processes can be observed in retinal tissue
    
    ### Conditions Reflected in Retinal Health
    
    - Multiple sclerosis
    - Parkinson's disease
    - Stroke risk assessment
    - Traumatic brain injury effects
    - General cognitive function
    """)
    
    st.markdown("### Current Research Status")
    st.markdown("""
    Research increasingly supports the use of retinal imaging as a non-invasive method to assess neurological health. Longitudinal studies are currently tracking how retinal changes predict neurological outcomes over time.
    """)

# Diabetes Tab
with tab3:
    diabetes_info = model.get_condition_info("diabetes")
    
    st.markdown(f"## {diabetes_info['name']}")
    
    st.markdown("### Overview")
    st.markdown(diabetes_info['description'])
    
    st.markdown("### Retinal Biomarkers")
    for indicator in diabetes_info['retinal_indicators']:
        st.markdown(f"- {indicator}")
    
    st.markdown("### Connection to Retinal Health")
    st.markdown("""
    Diabetes affects small blood vessels throughout the body, with the retina being particularly vulnerable. Changes in retinal vascular health can be detected before other clinical signs of diabetes appear.
    
    Key connections include:
    
    - Elevated blood glucose damages retinal blood vessels
    - Microaneurysms are often the earliest detectable sign of diabetic retinopathy
    - Changes in vessel caliber and tortuosity correlate with diabetes progression
    - Retinal capillary dropout indicates microvascular damage
    
    ### Importance of Screening
    
    - Early detection of diabetes before clinical diagnosis
    - Monitoring of diabetes control through retinal health
    - Prevention of vision-threatening complications
    """)
    
    st.markdown(f"### Current Research Status")
    st.markdown(diabetes_info['research_status'])

# Blood Pressure Tab
with tab4:
    hypertension_info = model.get_condition_info("hypertension")
    
    st.markdown(f"## {hypertension_info['name']}")
    
    st.markdown("### Overview")
    st.markdown(hypertension_info['description'])
    
    st.markdown("### Retinal Biomarkers")
    for indicator in hypertension_info['retinal_indicators']:
        st.markdown(f"- {indicator}")
    
    st.markdown("### Connection to Retinal Health")
    st.markdown("""
    The retina contains the only blood vessels that can be directly visualized non-invasively, making it an excellent window into cardiovascular health.
    
    The retinal vascular changes in hypertension include:
    
    - Narrowing of arterioles (small arteries)
    - Changes in the arteriole-to-venule ratio (AVR)
    - Arteriovenous nicking where arteries cross over veins
    - In severe cases, flame-shaped hemorrhages and cotton wool spots
    
    ### Classification of Hypertensive Retinopathy
    
    1. **Mild**: Arteriolar narrowing
    2. **Moderate**: Arteriovenous nicking and opacity of arteriolar walls
    3. **Severe**: Retinal hemorrhages, exudates, and cotton wool spots
    4. **Malignant**: Severe plus papilledema (swelling of the optic nerve)
    """)
    
    st.markdown(f"### Current Research Status")
    st.markdown(hypertension_info['research_status'])

# Diabetic Retinopathy Tab
with tab5:
    dr_info = model.get_condition_info("dr")
    
    st.markdown(f"## {dr_info['name']}")
    
    st.markdown("### Overview")
    st.markdown(dr_info['description'])
    
    st.markdown("### Retinal Biomarkers")
    for indicator in dr_info['retinal_indicators']:
        st.markdown(f"- {indicator}")
    
    st.markdown("### Stages of Diabetic Retinopathy")
    st.markdown("""
    1. **Mild Nonproliferative Retinopathy**: At least one microaneurysm
    
    2. **Moderate Nonproliferative Retinopathy**: Microaneurysms, intraretinal hemorrhages, hard exudates, and cotton wool spots
    
    3. **Severe Nonproliferative Retinopathy**: More extensive hemorrhages, venous beading, and intraretinal microvascular abnormalities
    
    4. **Proliferative Diabetic Retinopathy**: Growth of new, abnormal blood vessels on the retina and vitreous, potential for vitreous hemorrhage and retinal detachment
    
    ### Diabetic Macular Edema
    
    Can occur at any stage of diabetic retinopathy and involves swelling in the macula (central retina), which can cause significant vision impairment.
    """)
    
    st.markdown("### Prevention and Management")
    st.markdown("""
    - Regular eye examinations for early detection
    - Tight blood glucose control
    - Blood pressure management
    - Treatment options include laser therapy, anti-VEGF injections, and surgery for advanced cases
    """)
    
    st.markdown(f"### Current Research Status")
    st.markdown(dr_info['research_status'])

# Age-related Macular Degeneration Tab
with tab6:
    amd_info = model.get_condition_info("amd")
    
    st.markdown(f"## {amd_info['name']}")
    
    st.markdown("### Overview")
    st.markdown(amd_info['description'])
    
    st.markdown("### Retinal Biomarkers")
    for indicator in amd_info['retinal_indicators']:
        st.markdown(f"- {indicator}")
    
    st.markdown("### Types of AMD")
    st.markdown("""
    1. **Dry AMD (Non-neovascular)**: The most common form (85-90% of cases)
       - Characterized by drusen (yellow deposits) under the retina
       - Gradual thinning of the macula
       - Slow, progressive vision loss
       
    2. **Wet AMD (Neovascular)**: Less common but more severe
       - Abnormal blood vessels grow under the retina
       - These vessels can leak fluid and blood
       - Causes more rapid and severe vision loss
    
    ### Stages of AMD
    
    - **Early AMD**: Medium-sized drusen, no vision loss
    - **Intermediate AMD**: Large drusen, possible pigment changes, possible mild vision loss
    - **Late AMD**: Vision loss from damage to the macula (either from geographic atrophy in dry AMD or leaking blood vessels in wet AMD)
    """)
    
    st.markdown("### Risk Factors")
    st.markdown("""
    - Age (primary risk factor)
    - Family history and genetics
    - Smoking
    - Cardiovascular disease
    - High blood pressure
    - Obesity
    - Diet low in antioxidants
    """)
    
    st.markdown(f"### Current Research Status")
    st.markdown(amd_info['research_status'])

# Resources section
st.markdown("## Additional Resources")

st.markdown("""
### Organizations
- [Alzheimer's Association](https://www.alz.org/)
- [American Diabetes Association](https://www.diabetes.org/)
- [American Heart Association](https://www.heart.org/)
- [National Eye Institute](https://www.nei.nih.gov/)
- [American Academy of Ophthalmology](https://www.aao.org/)

### Educational Resources
- [Understanding Retinal Health (NIH)](https://www.nih.gov/)
- [Diabetes and Your Eyes (CDC)](https://www.cdc.gov/)
- [Age-Related Eye Disease Studies (AREDS)](https://www.nei.nih.gov/research/clinical-trials/age-related-eye-disease-studies-aredsareds2)
""")

# Disclaimer
st.markdown("---")
st.markdown("""
**Disclaimer**: The information provided on this page is for educational purposes only and is not intended as medical advice, diagnosis, or treatment. Always seek the advice of your physician or other qualified health provider with any questions you may have regarding a medical condition.
""")

# Back to home button
if st.button("Back to Home"):
    st.switch_page("app.py")
