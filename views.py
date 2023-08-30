import streamlit as st
import pickle
from streamlit_option_menu import option_menu



    
    # sidebar for navigation
with st.sidebar:
        
    selected = option_menu('ML BASED STROKE DISEASES PREDICTION SYSTEM USING ECG AND PPG BIO SIGNALS',['Stroke Prediction',],
                            icons=['activity','heart','person'],
                            default_index=0)
    # Load the saved models
stroke_model = pickle.load(open('stroke_model.sav', 'rb'))

 
        

if (selected == 'Stroke Prediction'):
        
    # page title
    #st.markdown("<h1 style='text-align: center; color: purple;'>Stroke Prediction </h1>", unsafe_allow_html=True)

    #st.title(' \t \t :blue[Stroke Prediction]')
    st.image("Capture.jpg",width=720)
    Age = st.slider("Age",1,100,1)
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    with col1:
        BY = st.text_input('BY')
        
    with col2:
        BI = st.text_input('BI')
    
    with col3:
        AV = st.text_input('AV')
    
    with col1:
        CJ = st.text_input('CJ')
    
    with col2:
        CY = st.text_input('CY')
    
    with col3:
        CO = st.text_input('CO')
    
    with col1:
        FO = st.text_input('FO')
    
    with col2:
        FC = st.text_input('FC')

    with col3:
        GL = st.text_input("GL")

    with col1:
        IF = st.text_input('IF')
    
    with col2:
        KJ = st.text_input('KJ')

    with col3:
        JZ = st.text_input("JZ")

    with col1:
        LG = st.text_input('LG')
    
    with col2:
        BZ = st.text_input('BZ')
    
    #"GL","IF","KJ","JZ","LG","BZ"
    st_diagnosis = ''
    info = ''
    st_prediction = ''
    
    # creating a button for Prediction
    
    if st.button('Stroke Test Result'):
        st_prediction = stroke_model.predict([[Age,BY,BI,AV,CJ,CY,CO,FO,FC,GL,IF,KJ,JZ,LG,BZ]])

        if (st_prediction[0] > 0.5 and st_prediction[0] < 0.6):
            st_diagnosis = 'Minor Stroke'
                        
            
            info = 'Minor stroke is generally defined as an National Institute of Health Stroke Scale (NIHSS) of 5 or less, which takes into account certain deficits but not the fact that some can have a more profound impact on quality of life than others. Hence, the scale does not linearly correlate deficit and disability.'
        
        elif (st_prediction[0] > 0.6 and st_prediction[0] < 0.7):
            st_diagnosis = 'Moderate Stroke' 
                        
            
            info = 'They happen when a blood clot blocks the flow of blood and oxygen to the brain.'

        elif (st_prediction[0] > 0.7 and st_prediction[0] < 0.8):
            st_diagnosis = 'Moderate to Severe Stroke' 
                        
        
            info = 'Cognitive symptoms like memory problems and trouble speaking. Physical symptoms such as weakness, paralysis and difficulty swallowing. Emotional symptoms like depression and impulsivity. Heavy fatigue and trouble sleeping.'

        elif (st_prediction[0] > 0.8):
            st_diagnosis = 'Severe Stroke' 
                        
          
            info = 'The most severe strokes can leave a person unable to respond, or in a sleep-like state. This is sometimes called unconsciousness or coma, and it means that important parts of the brain are not working well. '

        else:
            st_diagnosis = " No stroke"

        

        
    st.success(st_diagnosis)
    
    if (info != ''):
        st.info(info)




