"""
You need to run the app from the root
To run the app
$ streamlit run app.py
"""

import json
import pandas as pd
import streamlit as st
from PIL import Image
import requests



# with st.sidebar:
    
    
st.title('IT Service Management')


description = st.text_input('Description: ')
if description:
    pass

"""
To cover
- please make sure that there are NO titles (age, sex, bmi, bp, ... ) in the begining of .csv file
- reading csv one time
- executing only if data is loaded
"""