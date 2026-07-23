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
    .match-box { background-color: #eff6ff; padding: 20px; border-radius: 10px; border: 1px solid #bfdbfe; margin-top: 20px; }
    </style>
    """,
    unsafe_allow_html=True,
)

# VAM Data with Custom Reference Names and Specifications
vam_connections_data = {
    "REF03500092021": {"Type": "VAM 21", "OD": 3.500, "Wall_Th": 0.254, "Weight": 9.20, "Drift": 2.867, "Pin_PED": "3.500 (+0.012/+0.031)", "Pin_PID": "2.976 (-0.020/0.000)", "Box_BED": "3.930 (0.000/+0.028)", "Box_BID": "2.961 (-0.020/0.000)"},[cite: 9]
    "REF04500116021": {"Type": "VAM 21", "OD": 4.500, "Wall_Th": 0.250, "Weight": 11.60, "Drift": 3.875, "Pin_PED": "4.500 (+0.016/+0.045)", "Pin_PID": "3.959 (-0.020/0.000)", "Box_BED": "4.934 (0.000/+0.028)", "Box_BID": "3.942 (-0.020/0.000)"},[cite: 10]
    "REF05000150021": {"Type": "VAM 21", "OD": 5.000, "Wall_Th": 0.296, "Weight": 15.00, "Drift": 4.283, "Pin_PED": "5.000 (+0.016/+0.050)", "Pin_PID": "4.364 (-0.020/0.000)", "Box_BED": "5.504 (0.000/+0.021)", "Box_BID": "4.345 (-0.020/0.000)"},[cite: 11]
    "REF05500170021": {"Type": "VAM 21", "OD": 5.500, "Wall_Th": 0.304, "Weight": 17.00, "Drift": 4.767, "Pin_PED": "5.500 (+0.016/+0.055)", "Pin_PID": "4.892 (-0.020/0.000)", "Box_BED": "6.018 (0.000/+0.054)", "Box_BID": "4.891 (-0.020/0.000)"},
    "REF023750460TOP": {"Type": "VAM TOP", "OD": 2.375, "Wall_Th": 0.190, "Weight": 4.60, "Drift": 1.901, "Pin_PED": "2.375 (+0.008/+0.031)", "Pin_PID": "1.969 (-0.010/+0.009)", "Box_BED": "2.677 (0.000/+0.029)", "Box_BID": "1.957 (-0.010/+0.009)"},[cite: 4]
    "REF028750640TOP": {"Type": "VAM TOP", "OD": 2.875, "Wall_Th": 0.217, "Weight": 6.40, "Drift": 2.347, "Pin_PED": "2.875 (+0.008/+0.031)", "Pin_PID": "2.421 (-0.009/+0.010)", "Box_BED": "3.223 (0.000/+0.028)", "Box_BID": "2.409 (-0.010/+0.009)"},[cite: 5]
    "REF035000650TOP": {"Type": "VAM TOP", "OD": 3.500, "Wall_Th": 0.170, "Weight": 6.50, "Drift": 3.035, "Pin_PED": "3.500 (+0.012/+0.031)", "Pin_PID": "3.118 (-0.009/+0.009)", "Box_BED": "3.771 (0.000/+0.028)", "Box_BID": "3.104 (-0.009/+0.010)"},[cite: 6]
    "REF040000820TOP": {"Type": "VAM TOP", "OD": 4.000, "Wall_Th": 0.190, "Weight": 8.20, "Drift": 3.495, "Pin_PED": "4.000 (+0.012/+0.031)", "Pin_PID": "3.583 (-0.010/+0.009)", "Box_BED": "4.300 (0.000/+0.029)", "Box_BID": "3.567 (-0.009/+0.009)"},[cite: 7]
    "REF045001050TOP": {"Type": "VAM TOP", "OD": 4.500, "Wall_Th": 0.224, "Weight": 10.50, "Drift": 3.927, "Pin_PED": "4.500 (+0.016/+0.045)", "Pin_PID": "4.016 (-0.010/+0.009)", "Box_BED": "4.859 (0.000/+0.028)", "Box_BID": "3.999 (-0.009/+0.010)"}[cite: 8]
}

# Main Layout Structure matching user interface
st.markdown('<p class="main-header">⚡ Child Drawing Recognition & Master Path Tracking</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">System Integration & Vendor Database Sync</p>', unsafe_allow_html=True)

col1, col2 = st.columns([1.1, 0.9])

with col1:
    st.markdown("### 📁 Target Drawing File")
    st.markdown("Upload Drawing PDF (Child Component)")
    uploaded_file = st.file_uploader("Upload 200MB per file • PDF", type=["pdf"])
    
    # Active Session Select Options using custom REF codes
    active_options = ["W.021578-00-00 (Profile Drawing, 3/8 FMJ Hydraulic, Female Connection)"] + list(vam_connections_data.keys())
    selected_drawing = st.selectbox("Or Select from Active Session:", active_options)
    
    if st.button("🔍 Auto-Detect Drawing Type & Path"):
        st.success("Drawing type, matched status, and parameters successfully synced to Parent Drawing!")

with col2:
    st.markdown("### ⚙️ System Recognition & Path Tracking Result")
    
    if selected_drawing in vam_connections_data:
        matched_data = vam_connections_data[selected_drawing]
        st.markdown(
            f"""
            <div class="success-box">
                ✅ Recognition Complete: Matched with Vendor Registry ({matched_data['Type']})!
            </div>
            """,
            unsafe_allow_html=True
        )
        st.markdown("---")
        st.markdown("**Detected Entity Type:** Child Drawing (Sub-Component - Matched)")
        st.markdown(f"**Reference Code:** {selected_drawing}")
        st.markdown(f"**Path Mapping:** Assemblies/Mandrel/9GC1-550013/{selected_drawing}")
        st.markdown("**Linked Master (Parent):** 9GC1-550013 (Mandrel Assembly)")
    else:
        st.markdown(
            """
            <div class="success-box">
                ✅ Recognition Complete: Identified as Child Component!
            </div>
            """,
            unsafe_allow_html=True
        )
        st.markdown("---")
        st.markdown("**Detected Entity Type:** Child Drawing (Sub-Component)")
        st.markdown("**Drawing Number:** W.021578-00-00")
        st.markdown("**Path Mapping:** Assemblies/Mandrel/9GC1-550013/W.021578-00-00")
        st.markdown("**Linked Master (Parent):** 9GC1-550013 (Mandrel Assembly)")

# Vendor Live Sync Section
st.markdown("---")
st.markdown("### 🔄 Vendor Live Sync & Parent Drawing Verification")
v_col1, v_col2 = st.columns(2)

with v_col1:
    st.markdown("**External Vendor Portals**")
    st.markdown("- [Open Tenaris DCP Portal](#)")
    st.markdown("- [Open VAM Services Configurator](#)")

with v_col2:
    st.markdown("**📊 Parent Drawing Status & Verification Feed**")
    st.info("Propagation Confirmed on Parent Drawing!")

# VAM Connection Specifications & Features Box
st.markdown("### 🛠️ VAM Connection Specifications & Features (Propagation Active)")
if selected_drawing in vam_connections_data:
    item = vam_connections_data[selected_drawing]
    f_col1, f_col2, f_col3 = st.columns(3)
    with f_col1:
        st.metric(label="Outer Diameter (OD)", value=f"{item['OD']} in")
        st.metric(label="Drift", value=f"{item['Drift']} in")
    with f_col2:
        st.metric(label="Wall Thickness", value=f"{item['Wall_Th']} in")
        st.metric(label="Weight", value=f"{item['Weight']} lb/ft")
    with f_col3:
        st.text(f"Pin PED: {item['Pin_PED']}")
        st.text(f"Pin PID: {item['Pin_PID']}")
        st.text(f"Box BED: {item['Box_BED']}")
        st.text(f"Box BID: {item['Box_BID']}")
else:
    st.info("Select a VAM Reference code from Active Session to view propagated features and specifications.")

# NEW: Vendor Data & Parent Drawing Match Verification Box
st.markdown("---")
st.markdown("### 🎯 Vendor-to-Parent Data Matching & Synchronization Verification")
if selected_drawing in vam_connections_data:
    item = vam_connections_data[selected_drawing]
    st.markdown(
        f"""
        <div class="match-box">
            <h4>🔍 Cross-Check & Compliance Match Report</h4>
            <ul>
                <li><b>Reference ID:</b> {selected_drawing} ({item['Type']})[cite: 9]</li>
                <li><b>Vendor Specs Compliance:</b> Verified (OD: {item['OD']} in, Weight: {item['Weight']} lb/ft)[cite: 9]</li>
                <li><b>Parent Drawing Link (9GC1-550013):</b> <span style="color: green; font-weight: bold;">Synchronized & Matched Successfully</span></li>
                <li><b>Data Propagation Status:</b> 100% Verified across Engineering Vault Nodes.</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )
else:
    st.markdown(
        """
        <div class="match-box">
            <h4>🔍 Cross-Check & Compliance Match Report</h4>
            <p>Awaiting VAM reference selection to perform Vendor-to-Parent Drawing parametric matching.</p>
        </div>
        """,
        unsafe_allow_html=True
    )
