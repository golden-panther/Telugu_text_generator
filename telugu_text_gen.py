from googletrans import Translator
import streamlit as st
import requests

st.set_option('deprecation.showfileUploaderEncoding', False)

st.write("""
         # ***Telugu Language Text Generator***
         """
         )

st.write("This is a simple AI text generator. It takes a seed text as input and generates telugu text based on seed/prompt as output")

translator = Translator()
# telugu_query = 'దక్షిణ భారతదేశం'
telugu_query = st.text_input("Please enter seed text in telugu")
try:
	temp1 = translator.translate(telugu_query,src="te",dest="en")
	english_query = temp1.text
	r = requests.post(
    		"https://api.deepai.org/api/text-generator",
    		data={
        	'text': english_query,
    		},
    	headers={'api-key': '15a3b63b-c64b-413a-b313-f36a383f3fe1'}
	)
	english_text = r.json()["output"]

	temp2 = translator.translate(english_text,src="en",dest="te")
	telugu_text = temp2.text
except:
	pass




if not telugu_query:
	st.text("You haven't given any seed text in telugu language")
else:
	st.write(telugu_text)
