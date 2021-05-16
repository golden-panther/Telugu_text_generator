from googletrans import Translator
import streamlit as st
import requests

st.set_option('deprecation.showfileUploaderEncoding', False)

st.write("""
         # ***Telugu Language Text Generator***
         """
         )

st.write("This is a simple AI text generator. It takes a seed text as input and generates telugu text based on seed/prompt as output.")

with st.form(key='my_form'):
	telugu_query = st.text_input(label='Enter seed text in telugu')
	amount_of_text = st.number_input(label="Amount of Text Required (Ranges from 1 to 10)", min_value = 1, max_value=10, step = 1)
	submit_button = st.form_submit_button(label='Submit')

translator = Translator()

try:
	temp1 = translator.translate(telugu_query,src="te",dest="en")
	english_query = temp1.text
	english_text = ""
	for i in range(amount_of_text):
		r = requests.post(
    			"https://api.deepai.org/api/text-generator",
    			data={
        		'text': english_query,
    			},
    		headers={'api-key': '15a3b63b-c64b-413a-b313-f36a383f3fe1'}
		)
		english_text+= r.json()["output"]

	temp2 = translator.translate(english_text,src="en",dest="te")
	telugu_text = temp2.text
except:
	pass

if not telugu_query:
	st.text("You haven't given any seed text in telugu language")
else:
	st.write(telugu_text)
