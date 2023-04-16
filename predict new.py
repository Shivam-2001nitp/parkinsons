import numpy as np
import pickle
import streamlit as st
import streamlit.components.v1 as components

# Loading Save Model
loaded_model = pickle.load(open("C:\\Users\\shiva\\Desktop\\hackathon\\parkinson\\parkinsons_model.sav", 'rb'))

components.html("<html><body></body></html>")
import base64
import streamlit as st

def parkinson_prediction(input_data):
    

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return 'You do not have Parkinson\'s'
    else:
      return 'You have Parkinson\'s'
  
    
  
def main():
    # Title
    st.title("Parkinson\'s Prediction Web App")
    
    # User Input
    Maximum_vocal_fundamental_frequency = st.text_input('MDVP:Fhi(Hz)', value="", max_chars=None, type="default", help=None, autocomplete=None, on_change=None, args=None, kwargs=None, placeholder="Average vocal fundamental frequency", disabled=False, label_visibility="visible")
    Average_vocal_fundamental_frequency = st.text_input('MDVP:Fo(Hz)',placeholder="Maximum vocal fundamental frequency")  
    Minimum_vocal_fundamental_frequency = st.text_input('MDVP:Flo(Hz)',placeholder="Minimum vocal fundamental frequency")
    variation_in_fundamental_frequency1 = st.text_input('MDVP:Jitter(%)',placeholder="Several measures of variation in fundamental frequency")
    variation_in_fundamental_frequency2 = st.text_input('MDVP:Jitter(Abs)',placeholder="Several measures of variation in amplitude")
    variation_in_fundamental_frequency3 = st.text_input('MDVP:RAP',placeholder=" Two measures of ratio of noise to tonal components in the voice")
    variation_in_fundamental_frequency4 = st.text_input('MDVP:PPQ',placeholder=" Health status of the subject (one) - Parkinson's, (zero) - healthy")
    variation_in_fundamental_frequency5 = st.text_input('Jitter:DDP',placeholder="Two nonlinear dynamical complexity measures")
    measures_of_variation_in_amplitude1 = st.text_input('MDVP:Shimmer',placeholder="Several measures of variation in amplitude")
    measures_of_variation_in_amplitude2 = st.text_input('MDVP:Shimmer(dB)',placeholder="Several measures of variation in amplitude")
    measures_of_variation_in_amplitude3 = st.text_input('Shimmer:APQ3',placeholder="Several measures of variation in amplitude")
    measures_of_variation_in_amplitude4 = st.text_input('Shimmer:APQ5',placeholder="Several measures of variation in amplitude")
    measures_of_variation_in_amplitude5 = st.text_input('MDVP:APQ',placeholder="Several measures of variation in amplitude")
    measures_of_variation_in_amplitude6 = st.text_input('Shimmer:DDA',placeholder="Several measures of variation in amplitude")
    measures_of_the_ratio_of_noise_to_tonal_components_in_the_voice1 = st.text_input('NHR',placeholder="Two measures of ratio of noise to tonal components in the voice")
    measures_of_the_ratio_of_noise_to_tonal_components_in_the_voice2 = st.text_input('HNR',placeholder="Two measures of ratio of noise to tonal components in the voice")
    nonlinear_dynamical_complexity_measures1 = st.text_input('RPDE',placeholder="Two nonlinear dynamical complexity measures")
    nonlinear_dynamical_complexity_measures2 = st.text_input('DFA',placeholder="Signal fractal scaling exponent")
    Signal_fractal_scaling_exponent = st.text_input('spread1',placeholder="Three nonlinear measures of fundamental frequency variation")
    nonlinear_measures_of_fundamental_frequency_variation1 = st.text_input('spread2',placeholder="Three nonlinear measures of fundamental frequency variation")
    nonlinear_measures_of_fundamental_frequency_variation2 = st.text_input('D2',placeholder="Two nonlinear dynamical complexity measures")
    nonlinear_measures_of_fundamental_frequency_variation3 = st.text_input('PPE',placeholder="Three nonlinear measures of fundamental frequency variation")
    
    
    # Prediction Code
    diagnosis = ''
    
    # Button(Submission)
    if st.button('Parkinson\'s Test Result'):
        diagnosis = parkinson_prediction([Average_vocal_fundamental_frequency, Maximum_vocal_fundamental_frequency, Minimum_vocal_fundamental_frequency, variation_in_fundamental_frequency1, variation_in_fundamental_frequency2, variation_in_fundamental_frequency3, variation_in_fundamental_frequency4, variation_in_fundamental_frequency5, measures_of_variation_in_amplitude1, measures_of_variation_in_amplitude2, measures_of_variation_in_amplitude3, measures_of_variation_in_amplitude4, measures_of_variation_in_amplitude5, measures_of_variation_in_amplitude6, measures_of_the_ratio_of_noise_to_tonal_components_in_the_voice1, measures_of_the_ratio_of_noise_to_tonal_components_in_the_voice2, nonlinear_dynamical_complexity_measures1, nonlinear_dynamical_complexity_measures2, Signal_fractal_scaling_exponent, nonlinear_measures_of_fundamental_frequency_variation1, nonlinear_measures_of_fundamental_frequency_variation2, nonlinear_measures_of_fundamental_frequency_variation3])
        st.success(diagnosis)
if __name__ == '__main__':
    main()