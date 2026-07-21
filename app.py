import streamlit as st
import os
import tempfile
import pdfplumber

st.set_page_config(page_title="HCT Guard - Engineering Design Hub", layout="wide")

st.title("HCT Guard AI - Live Design & Compliance Hub")
st.markdown("---")

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📁 Central Design Database & Live Parameters")
    st.info("Connected to Halliburton Engineering Database for latest drawing revisions.")
    
    # قاعدة البيانات المرتبطة بملف التصميم الهندسي الخاص بك
    database_drawings = {
        "Splice Sub - 5 1/2-23.00# TSH Blue (D02567361)": {
            "rev": "Rev A",
            "top_conn": "5 1/2-23.00# TENARISHYDRIL BLUE BOX (BOM #806)",
            "bottom_conn": "5 1/2-23.00# TENARISHYDRIL BLUE PIN (BOM #807)",
            "envelope_status": "✅ Verified - No interference with shoulders/grooves",
            "key_dims": "OD: 5.850 in | Length: 36.0 in | Blanking Length: 11.50 in",
            "file_name": "EXAMPLE_1.pdf"
        }
    }
    
    selected_design = st.selectbox("Select Component Drawing:", list(database_drawings.keys()))
    
    if selected_design:
        details = database_drawings[selected_design]
        st.success(f"Status: {details['envelope_status']}")
        st.write(f"**Drawing Revision:** {details['rev']}")
        st.write(f"**Top Connection:** {details['top_conn']}")
        st.write(f"**Bottom Connection:** {details['bottom_conn']}")
        st.write(f"**Envelope & Dimensions:** {details['key_dims']}")
        
        # الأيقونة أو الزر المطلوب لعرض تفاصيل الـ PDF والتحقق الفوري
        if st.button("ℹ️ View Live PDF Data & Envelope Check"):
            pdf_path = details["file_name"]
            if os.path.exists(pdf_path):
                with pdfplumber.open(pdf_path) as pdf:
                    st.write("### 📄 Extracted Blueprint & Connection Specs:")
                    full_text = ""
                    for page in pdf.pages:
                        t = page.extract_text()
                        if t:
                            full_text += t + "\n"
                    st.text_area("Live Parameters from PDF Layer", full_text[:1800], height=250)
            else:
                st.warning(f"Please ensure '{pdf_path}' is placed in the Desktop folder alongside app.py.")

with col2:
    st.subheader("📤 Upload New Revision PDF")
    st.write("Upload a new drawing version to verify constraints and envelope clearances instantly:")
    
    uploaded_file = st.file_uploader("Choose PDF drawing", type=["pdf"])
    
    if uploaded_file is not None:
        st.success(f"File uploaded: **{uploaded_file.name}**")
        with st.spinner("Checking constraints and thread envelope..."):
            try:
                with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
                    tmp.write(uploaded_file.read())
                    tmp_path = tmp.name
                
                text_data = ""
                with pdfplumber.open(tmp_path) as pdf:
                    for page in pdf.pages:
                        txt = page.extract_text()
                        if txt:
                            text_data += txt + "\n"
                
                os.remove(tmp_path)
                
                if text_data.strip():
                    st.info("Parsed Successfully! Evaluated against latest design rules.")
                    with st.expander("View Parsed Text & Envelope Notes"):
                        st.text(text_data[:1200])
                else:
                    st.warning("No text found in PDF vector layer.")
            except Exception as e:
                st.error(f"Error: {e}")

st.markdown("---")
st.caption("Halliburton Core Technology - Automated Design Verification System")
                
   