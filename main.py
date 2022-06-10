import streamlit as st

a = st.selectbox("View Page: ", ["Intro", "Linear Regression", "Quadratic Regression", "Exponential Regression", "Machine Learning"])

if a == "Linear Regression":
    st.title('Linear Regression')
elif a == "Quadratic Regression":
    st.title('"Quadratic Regression')
elif a == "Exponential Regression":
    st.title('Exponential Regression')
elif a == "Machine Learning":
    st.title('Machine Learning')
elif a == "intro":
    st.title('House Price Prediction 🏘️🏙️📈📉')
    st.write('A web application demonstrating the results and conclusions of the House Price Prediction report.')
    st.write('This applet is part of the the final project for the MDM4U course, hosted under the GNU General Public LIcense.')
    with open("House_Price_Prediction_Report.pdf", "rb") as file:
        btn = st.download_button(
            label="Download Report",
            data=file,
            file_name="House_Price_Prediction_Report.pdf",
            mime="application/octet-stream" # Converts file data to byte stream, parsing to cout
        )
    st.write('')