import streamlit as st


# Page config
st.set_page_config(page_title="Tshepang Mmitsinyane | Resume", layout="wide")

# Sidebar
st.sidebar.title("Tshepang Mmitsinyane")
st.sidebar.markdown("**Software Engineer | Data Scientist | AI/ML Engineer | Robotics Engineer**")

# ✅ Profile Picture
st.sidebar.image("images/image.jpeg", width=150)  # <-- Add your image file in same folder

st.sidebar.markdown("---")
st.sidebar.info(
"""
📍 Midrand, Johannesburg  
📞 071 313 2187  
✉️ tshepang.mmitsinyane@gmail.com  
"""
)

# ✅ Links
st.sidebar.markdown("### 🔗 Links")
st.sidebar.markdown("[GitHub](https://github.com/Tshepang-Mmitsinyane)")
st.sidebar.markdown("[Linkedin](https://www.linkedin.com/in/tshepang-mmitsinyane-01514a259)")
st.sidebar.markdown("[Portfolio](https://www.hyperiondev.com/portfolio/157187/)")


st.sidebar.markdown("---")
st.sidebar.markdown("### 🧠 Core Skills")
st.sidebar.markdown("""
- Python  
- Machine Learning  
- SQL  
- Data Science  
- Artificial Intelligence (AI)
- Robotics
""")

# Main content
st.title("👨‍💻 Tshepang Mmitsinyane")

# Summary
st.markdown("## 🧾 Professional Summary")
st.write(
"""
Aspiring Software Engineer, Data Scientist, and AI/ML Engineer with a BSc Honours in Computing (with distinction). 
Strong foundation in Python, Machine Learning, SQL, Data Science, and AI, supported by a 98% Data Science training average. 
Experienced in building data-driven and deep learning solutions using TensorFlow, PyTorch, and Keras. 
Seeking a junior or internship role to apply analytical and AI-driven problem-solving skills in real-world environments.
"""
)

# Education
st.markdown("## 🎓 Education")

with st.expander("BSc Honours in Computing - UNISA"):
    st.write("""
- **Year:** 2024-2026   
- **Average:** 61%  

**Focus Areas:**
- Machine Learning
- AI
- Data Science
- Ontology Engineering 

""")

with st.expander("BSc Information Technology (Robotics) - Eduvos"):
    st.write("""
- **Year:** 2020 – 2022  
- **Average:** 71%  

**Focus Areas:**
- Machine Learning  
- Robotics
- Python
""")

# Certifications
st.markdown("## 📜 Certifications")

st.write("""
- **IBM Data Science Professional Certificate**  
  (Python, SQL, Data Science, Machine Learning)

- **IBM AI Engineering Professional Certificate**  
  (AI, Machine Learning, Deep Learning)

- **Data Science Bootcamp – HyperionDev (98%)**  
  (Python, Data Science, Machine Learning)
""")

# Projects
st.markdown("## 🚀 Projects")

with st.expander("AI-Based Spinach Disease Detection System"):
    st.write(
    """

    ## **BSc Honours Research Project Core Focus**: 
    - Computer Vision
    - Deep Learning
    - Smart Agriculture 
    
    ## **Project Overview**
    Developed an automated, low-cost monitoring system designed to identify and classify diseases in spinach crops within greenhouse environments. 
    By leveraging Convolutional Neural Networks (CNNs), the system provides real-time diagnostic feedback, enabling farmers to intervene early and reduce crop loss without the need for expensive laboratory testing. 
    
    ## **Key Technical Contributions** 
    - Deep Learning Architecture: Designed and trained a CNN model specifically for agricultural image classification, utilizing frameworks like TensorFlow and Keras.
    - Computer Vision Pipeline: Implemented advanced image pre-processing and augmentation techniques using OpenCV to ensure model robustness against varying light and humidity conditions found in low-cost greenhouses.
    - End-to-End Data Management: Curated and labeled a specialized dataset of spinach leaf images, managing the full data lifecycle from acquisition to model validation.
    - Precision Agriculture Integration: Focused on a "Smart Farming" approach, bridging the gap between high-level Ontology Engineering and practical, field-deployable AI solutions.
    
    ## **Technical Stack**
    - Languages: Python 
    - AI/ML: TensorFlow, karas, Scikit-learn, CNN Architecture Computer Vision: OpenCV, Image Processing 
    - Research: Methodology, Proposal, and Honours Research Report 
    
    ### **Impact Statement** 
    This research demonstrates how accessible AI technology can empower small-scale farmers with data-driven insights, directly contributing to more sustainable and efficient agricultural practices.
    While the current prototype is optimized for low-cost greenhouse monitoring, the underlying Convolutional Neural Network (CNN) architecture is designed to be platform-agnostic.  
    This modular approach ensures the system can be seamlessly integrated into various edge devices and autonomous platforms:
    - Drone Integration: The model is optimized for integration with drone-mounted cameras, enabling wide-scale aerial field monitoring and rapid disease mapping over large hectares.
    - Cross-Framework Compatibility: Built using TensorFlow/Keras with weights that can be exported for PyTorch or ONNX environments, ensuring flexibility across different software ecosystems.
    - Edge Computing: Designed to run on lightweight hardware (such as Raspberry Pi or Jetson Nano), similar to the manual controller logic used in my Arduino-based Quadcopter project.
     
    """
)
    st.image("images/Picture1.png", caption="Swiss chard classification")
    

with st.expander("Python-Controlled Autonomous Quadcopter"):
    st.write(
    """
    - Robotics Lead & Hardware Architect
    - Arduino (C++)
    - COmputer Vision

    ## **Project Overview**
    Designed and assembled a custom-built quadcopter for my BSc IT Robotics final project, focusing on the integration of microcontrollers with high-level Python control systems. The project demonstrated a practical application of Industry 4.0 principles and real-time systems.

    ## **Key Technical Contributions**
    - Hardware Integration: Engineered the drone's physical architecture using an Arduino board, brushless DC (BLDC) motors, and Electronic Speed Controllers (ESCs) to manage flight dynamics.
    - PID Control Logic: Implemented Proportional-Integral-Derivative (PID) algorithms to stabilize flight and ensure responsive handling during maneuvers.
    - Python Interface: Developed a Python-based command interface to facilitate communication between the workstation and the drone, bridging low-level hardware with high-level logic.
    - Sensor Fusion: Calibrated IMU sensors (accelerometers and gyroscopes) to maintain level flight and altitude hold.
    
    ## **Techincal Stack** 
    - Arduino (C++)
    - Python, PID Control
    - Sensor Fusion
    """)
    st.image("images/drone1.jpeg", caption="Custom Built Quadcopter Prototype")


st.markdown("## 🚀 Upcoming Projects/Certifications")
st.write("""
- Facial Emotion Detector
- Azure Data scientist associate
         
""")

# ✅ GitHub Project Link
st.markdown("[🔗 View Project on GitHub](https://github.com/Tshepang-Mmitsinyane)")

# Skills
st.markdown("## 🛠️ Technical Skills")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### Programming & Databases")
    st.write("""
- Python  
- Machine Learning & Deep Learning
- Robotics
- c++
""")

    st.markdown("### Frameworks")
    st.write("""
- TensorFlow  
- PyTorch  
- Keras
- streamlit  
""")

with col2:
    st.markdown("### Data Science & AI")
    st.write("""
- Machine Learning  
- Data Science  
- Artificial Intelligence  
- Deep Learning  
""")

    st.markdown("### Other")
    st.write("""
- Data Visualization  
- Database Management  
- Research & Problem Solving  
""")

# Soft Skills
st.markdown("## 🤝 Soft Skills")
st.write("""
- Strong communication and teamwork  
- Analytical thinking  
- Ability to work independently  
- Works well under pressure  
""")

# Footer
st.markdown("---")
st.markdown("⭐ Built with Streamlit | © 2026 Tshepang Mmitsinyane")
