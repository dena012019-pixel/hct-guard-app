import time
import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="HCT Engineering Vault",
    page_icon="🛡️",
    layout="wide",
)

# Custom CSS Styles
st.markdown(
    """
    <style>
        .main-header { font-size: 26px; font-weight: 700; color: #1E3A8A; margin-bottom: 0px; }
        .sub-header { font-size: 14px; color: #64748B; margin-bottom: 20px; }
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
        '<div class="sub-header">Child-to-Parent Automated Propagation & Vendor Sync Hub</div>',
        unsafe_allow_html=True,
    )

st.divider()

# Section for Child-to-Parent Bulk Propagation (The core requirement)
st.markdown("### ⚡ Child-to-Parent Bulk Propagation Engine")
st.write(
    "Modify a Child Component feature once and automatically cascade the update across all linked Parent Drawings (e.g., 20+ assemblies) instantly."
)

col_sel, col_action = st.columns([2, 2])
with col_sel:
    child_component = st.selectbox(
        "Select Modified Child Drawing / Component:",
        [
            (
                "Thread Tolerance Adjustment - TSH Blue Pin (Child ID:"
                " CH-807)"
            ),
            "O-Ring Groove Dimension Update (Child ID: CH-402)",
        ],
    )

with col_action:
    st.write("")  # Spacing
    st.write("")
    propagate_btn = st.button(
        "🚀 Push Update to All Linked Parent Drawings (Bulk Sync)"
    )

if propagate_btn:
    with st.spinner(
        "Cascading child modification to all linked parent assemblies..."
    ):
        time.sleep(1.5)  # Simulate bulk database update processing

    st.success(
        "✨ **Propagation Successful!** The modification from the child drawing was successfully synchronized and applied to **38 Parent Drawings** simultaneously, eliminating manual updates."
    )
    st.info(
        "💡 **Impact Summary:** All 38 parent assemblies (including D02567361)[cite: 1] are now updated and locked with the latest manufacturing specs."
    )

st.divider()

# Main Application Layout: Central Database & Vendor Links
col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("### 🗂️ Central Design Database (Drawing D02567361)")
    st.info(
        "Synced with Halliburton Engineering Database & External Vendor Portals."
    )

    selected_drawing = st.selectbox(
        "Select Component Drawing:",
        [
            "Splice Sub - 5 1/2-23.00# TSH Blue (D02567361)[cite: 1]",
            "Revision Drawing B - Connector Hub",
        ],
    )

    st.success(
        "Status: Synced & Verified - Child modifications automatically cascaded"
    )

    with st.container():
        st.markdown("**Drawing Number:** D02567361[cite: 1]")
        st.markdown("**Drawing Revision:** Rev A (Auto-Updated)[cite: 1]")
        st.markdown(
            "**Top Connection (BOX):** 5 1/2-23.00# TENARISHYDRIL BLUE BOX (BOM #806)[cite: 1]"
        )
        st.markdown(
            "**Bottom Connection (PIN):** 5 1/2-23.00# TENARISHYDRIL BLUE PIN (BOM #807 - Modified & Cascaded)[cite: 1]"
        )
        st.markdown(
            "**Envelope & Dimensions:** OD: 5.850 in | Length: 36.0 in | Blanking Length: 11.50 in[cite: 1]"
        )

with col2:
    st.markdown("### 📤 Upload New Revision PDF & Vendor Portals")
    st.write(
        "Check external vendor configurations or upload new revisions."
    )

    st.markdown(
        '<a href="https://dcp.tenaris.com/" target="_blank">🔗 Open Tenaris DCP Portal</a>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<a href="https://www.vamservices.com/product/configurator" target="_blank">🔗 Open VAM Services Configurator</a>',
        unsafe_allow_html=True,
    )

    uploaded_file = st.file_uploader(
        "Choose PDF drawing", type=["pdf"], accept_multiple_files=False
    )

    if uploaded_file is not None:
        st.success(f"File '{uploaded_file.name}' uploaded successfully!")
        if st.button("Run Compliance Check"):
            with st.spinner("Analyzing drawing parameters against constraints..."):
                time.sleep(1)
                st.info(
                    "Verification complete: Passed all structural clearance constraints."
                )
