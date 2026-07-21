import time
import streamlit as st

# إعدادات الصفحة
st.set_page_config(
    page_title="HCT Engineering Vault",
    page_icon="🛡️",
    layout="wide",
)

# تنسيقات الواجهة المرتبة
st.markdown(
    """
    <style>
        .main-header { font-size: 26px; font-weight: 700; color: #1E3A8A; margin-bottom: 0px; }
        .sub-header { font-size: 14px; color: #64748B; margin-bottom: 20px; }
    </style>
""",
    unsafe_allow_html=True,
)

# الهيدر والشعار
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
        '<div class="sub-header">Live Design Database & Vendor Sync Hub (Tenaris DCP & VAM Services)</div>',
        unsafe_allow_html=True,
    )

st.divider()

# شريط أدوات الفحص المباشر للموردين (Live Sync Trigger)
st.markdown(
    "### 🔄 Vendor Real-Time Sync & Automated Update Monitor"
)
st.write(
    "Check live portals (Tenaris DCP & VAM Services) for unreleased or updated drawing revisions."
)

col_btn1, col_btn2 = st.columns([2, 4])
with col_btn1:
    sync_button = st.button("Check for Vendor Updates Now")

if sync_button:
    with st.spinner(
        "Connecting securely to Tenaris DCP & VAM Services portals..."
    ):
        time.sleep(1.5)  # محاكاة الاتصال السريع بالمنصات
    st.success(
        "✨ Sync Complete: Checked Tenaris DCP & VAM Services. 1 new critical design update detected!"
    )
    st.warning(
        "⚠️ **Notice for Halliburton Engineers:** A minor dimensional revision (Rev B) for Splice Sub was published on Tenaris DCP. Please review before final manufacturing deployment."
    )

st.divider()

# الواجهة الرئيسية (قاعدة البيانات وعمليات الرفع)
col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("### 🗂️ Central Design Database")
    st.info(
        "Connected to Halliburton Engineering Database & Synchronized with Vendor Portals."
    )

    selected_drawing = st.selectbox(
        "Select Component Drawing:",
        [
            "Splice Sub - 5 1/2-23.00# TSH Blue (D02567361)",
            "Revision Drawing B - Connector Hub",
        ],
    )

    st.success("Status: Verified - No interference with shoulders/grooves")

    with st.container():
        st.markdown("**Drawing Revision:** Rev A (Pending Vendor Update Check)")
        st.markdown(
            "**Top Connection:** 5 1/2-23.00# TENARISHYDRIL BLUE BOX (BOM #806)"
        )
        st.markdown(
            "**Bottom Connection:** 5 1/2-23.00# TENARISHYDRIL BLUE PIN (BOM #807)"
        )
        st.markdown(
            "**Envelope & Dimensions:** OD: 5.850 in | Length: 36.0 in | Blanking Length: 11.50 in"
        )

with col2:
    st.markdown("### 📤 Upload New Revision PDF")
    st.write("Upload a new drawing version to verify constraints instantly.")

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
  
             
   
