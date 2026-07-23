import time
import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="HCT Engineering Vault - Auto-Detect Hub",
    page_icon="🛡️",
    layout="wide",
)

# Custom CSS Styles
st.markdown(
    """
    <style>
        .main-header { font-size: 26px; font-weight: 700; color: #1E3A8A; margin-bottom: 0px; }
        .sub-header { font-size: 14px; color: #64748B; margin-bottom: 20px; }
        .card { background-color: #f8fafc; padding: 20px; border-radius: 10px; border: 1px solid #e2e8f0; }
    </style>
""",
    unsafe_allow_html=True,
)

# Header Section with Halliburton Logo
col_logo, col_title = st.columns([1, 6])
with col_logo:
    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/1/18/Halliburton_Logo.svg",
        width=90,
    )
with col_title:
    st.markdown(
        '<div class="main-header">HCT Engineering Vault</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="sub-header">Automated Child Drawing Recognition & Path Tracking Hub</div>',
        unsafe_allow_html=True,
    )

st.divider()

# Section: One-Click Auto-Detection for Child Drawings
st.markdown("### ⚡ One-Click Child Drawing Auto-Detection & Path Tracking")
st.write(
    "Upload or select a drawing file to let the system instantly recognize it as a Child Component and trace its Master Assembly."
)

col_upload, col_result = st.columns(2, gap="large")

with col_upload:
    st.markdown("#### 📂 Target Drawing File")
    uploaded_child_file = st.file_uploader(
        "Upload Drawing PDF (e.g., Child Component)", type=["pdf"], key="child_upload"
    )
    
    # Quick select simulation for demonstration
    selected_preset = st.selectbox(
        "Or Select from Active Session:",
        [
            "Select Drawing...",
            "W.021578-00-00 (Profile Drawing, 3/8 FMJ Hydraulic, Female Connection)",
        ]
    )
    
    detect_button = st.button("🔍 Auto-Detect Drawing Type & Path")

with col_result:
    st.markdown("#### ⚙️ System Recognition & Path Tracking Result")
    
    if detect_button or selected_preset != "Select Drawing...":
        with st.spinner("Analyzing drawing metadata and tracking path..."):
            time.sleep(1.0)
            
        st.success("✨ **Recognition Complete: Identified as Child Component!**")
        
        # Displaying the auto-detected intelligence
        st.markdown(
            """
            <div class="card">
                <b>Detected Entity Type:</b> <span style="color: #2563EB;">Child Drawing (Sub-Component)</span><br>
                <b>Drawing Number:</b> <code>W.021578-00-00</code><br>
                <b>Extracted Feature:</b> 3/8 FMJ Hydraulic, Female Connection<br>
                <b>Path Mapping:</b> <code>Assemblies/Mandrel/9GC1-550013/W.021578-00-00</code><br>
                <b>Linked Master (Parent):</b> <code>9GC1-550013</code> (Mandrel Assembly)<br>
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.info("Awaiting file upload or selection to run auto-detection...")

st.divider()

# Section: Vendor Sync & Propagation Actions
st.markdown("### 🔄 Vendor Live Sync & Bulk Propagation Hub")
col_action1, col_action2 = st.columns(2, gap="large")

with col_action1:
    st.markdown("#### External Vendor Portals")
    st.markdown(
        '<a href="https://dcp.tenaris.com/" target="_blank">🔗 Open Tenaris DCP Portal</a>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<a href="https://www.vamservices.com/product/configurator" target="_blank">🔗 Open VAM Services Configurator</a>',
        unsafe_allow_html=True,
    )

with col_action2:
    st.markdown("#### Cascade Actions")
    if st.button("Propagate Recognized Child Changes to Master (9GC1-550013)"):
        with st.spinner("Cascading updates to parent assembly..."):
            time.sleep(1)
        st.success("✅ Successfully propagated child updates to the Master Drawing tree!")
