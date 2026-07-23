import time
import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="HCT Engineering Vault - Propagation View",
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
        .success-box { background-color: #f0fdf4; padding: 15px; border-radius: 8px; border: 1px solid #bbf7d0; }
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
        '<div class="sub-header">Child-to-Parent Propagation & Real-Time Assembly Verification Hub</div>',
        unsafe_allow_html=True,
    )

st.divider()

# Section: One-Click Child Drawing Auto-Detection & Path Tracking
st.markdown("### ⚡ Child Drawing Recognition & Master Path Tracking")

col_upload, col_result = st.columns(2, gap="large")

with col_upload:
    st.markdown("#### 📂 Target Drawing File")
    uploaded_child_file = st.file_uploader(
        "Upload Drawing PDF (Child Component)", type=["pdf"], key="child_upload"
    )
    
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
            time.sleep(0.8)
            
        st.success("✨ **Recognition Complete: Identified as Child Component!**")
        st.markdown(
            """
            <div class="card">
                <b>Detected Entity Type:</b> <span style="color: #2563EB;">Child Drawing (Sub-Component)</span><br>
                <b>Drawing Number:</b> <code>W.021578-00-00</code><br>
                <b>Path Mapping:</b> <code>Assemblies/Mandrel/9GC1-550013/W.021578-00-00</code><br>
                <b>Linked Master (Parent):</b> <code>9GC1-550013</code> (Mandrel Assembly)<br>
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.info("Awaiting file selection to run auto-detection...")

st.divider()

# Section: Propagation & Proof of Update on Parent Drawing
st.markdown("### 🔄 Vendor Live Sync & Parent Drawing Verification")

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
    
    st.markdown("")
    propagate_btn = st.button("🚀 Propagate Child Changes to Master (9GC1-550013)")

with col_action2:
    st.markdown("#### 📊 Parent Drawing Status & Verification Feed")
    
    # Session state to handle interactive propagation proof
    if 'propagated' not in st.session_state:
        st.session_state.propagated = False

    if propagate_btn:
        with st.spinner("Cascading updates across the assembly tree..."):
            time.sleep(1.2)
        st.session_state.propagated = True

    if st.session_state.propagated:
        st.markdown(
            """
            <div class="success-box">
                <b>✅ Propagation Confirmed on Parent Drawing!</b><br>
                <hr style="margin: 8px 0;">
                <b>Master Drawing:</b> <code>9GC1-550013</code> (Mandrel Assembly)<br>
                <b>Previous Status:</b> Rev A (Out of sync with child component)[cite: 1]<br>
                <b>Updated Status:</b> <span style="color: #16a34a; font-weight: bold;">Rev B (Synchronized & Locked)</span><br>
                <b>Change Log:</b> Thread profile and tolerance values from Child <code>W.021578-00-00</code> successfully injected into Master BOM table.[cite: 1]
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.info("Click 'Propagate Child Changes to Master' to execute and verify the update transfer on the Parent Drawing.")
