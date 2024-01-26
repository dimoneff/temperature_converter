import streamlit as st
from celcius_to_farenheit import celcius_to_farenheit
from farenheit_to_celcius import farenheit_to_celcius
from PIL import Image


def main():
    

    temperature_modes = ("Celcius to Farenheit", "Farenheit to Celcius")
    mode = st.sidebar.selectbox(label="Choose a temperature mode:", options=temperature_modes)
    with Image.open("f_to_c.png") as img_file:
        st.sidebar.image(img_file)

    with st.form(key="value"):        
        container = st.empty()
        if "new_value" in st.session_state:
            INITIAL_VALUE = st.session_state["new_value"]
        else:
            INITIAL_VALUE = 0.00
   

        col_one, col_two = st.columns([1,6])
        value_input = container.number_input(label="Temperature:", 
                                             placeholder="Enter a value:", 
                                             key="value", 
                                             value=INITIAL_VALUE, 
                                             step=1.0)
                
        with col_one:
            enter_btn = st.form_submit_button(label="Convert") 
        with col_two:  
            clear_btn = st.form_submit_button(label="Clear")
        
    if enter_btn and mode == "Celcius to Farenheit":
        st.success(f"{value_input} degrees in °C is {round(celcius_to_farenheit(value_input),2)} in °F.")        
    elif mode == "Farenheit to Celcius" and  enter_btn:
        st.success(f"{value_input} degrees in °F is {round(farenheit_to_celcius(value_input),2)} in °C.")
       
    if clear_btn:
        value_input = container.number_input(label="Temperature:", 
                                             placeholder="Enter a value:", 
                                             key="new_value",
                                             step=1.0,
                                             )
 
        
                
    # only for testing purposes
    #st.session_state
        
if __name__ == "__main__":
    main()


# backup code of the app
# import streamlit as st
# from celcius_to_farenheit import celcius_to_farenheit
# from farenheit_to_celcius import farenheit_to_celcius

# def main():
    
#     temperature_modes = ("Celcius to Farenheit", "Farenheit to Celcius")
#     mode = st.sidebar.selectbox(label="Choose a temperature mode:", options=temperature_modes)

    
#     container = st.empty()
    
#     if "new_value" in st.session_state:
#         INITIAL_VALUE = st.session_state["new_value"]
#     else:
#         INITIAL_VALUE = 0.00
        
#     value_input = container.number_input(label="Temperature:", 
#                                          placeholder="Enter a value:", 
#                                          key="value", value=INITIAL_VALUE)
    
       
         
#     col_one, col_two = st.columns([1, 7])
#     with col_one:
#         enter_btn = st.button(label="Convert", key="enter") 
    
#     if enter_btn and mode == "Celcius to Farenheit":
#         st.success(celcius_to_farenheit(value_input))
#     elif enter_btn and mode == "Farenheit to Celcius":
#         st.success(farenheit_to_celcius(value_input))
    
#     with col_two:
#         clear_btn = st.button(label="Clear", key="clear")

#     if clear_btn:
#         value_input = container.number_input(label="Temperature:", 
#                                              placeholder="Enter a value:", 
#                                              value=0.00, 
#                                              key="new_value")
       
    
#     st.session_state

# if __name__ == "__main__":
#     main()