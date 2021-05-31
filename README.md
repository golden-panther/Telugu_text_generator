# Telugu_text_generator

Link: https://share.streamlit.io/golden-panther/telugu_text_generator/main/telugu_text_gen.py

A simple AI text generator (telugu language) which takes a seed text as input and generates telugu text related to the seed text as output. We can also adjust the amount of text, we want to generate in the range of 1 to 10.

There are two methods of giving input. Choose any one:
  1. Custom input - Here, the user needs to provide a seed/prompt text (telugu).
  2. Select one of the readily available sample seed texts.

I integrated two APIs to achieve telugu language text generator from english text generator.
  1. Googletrans (a python module which enables usage of free Google translate API)
  2. DeepAI's text generation API (it is based on GPT-2)

I used streamlit to host this project online.

This is how the code works.....
  1. Take telugu text as input and store it in "telugu_query"
  2. Translate it to english and strore it in "english_query"
  3. Input this english_query to generate text using DeepAI's API and store it in "english_text"
  4. Translate this "english_text" into "telugu_text"
  5. Display the output

##Usage
1. Open website
2. Select/input seed text
3. Adjust "amount of text" value
4. Click on "submit"
5. The generated text will be displayed with a success message.

## How to run this app
Use the project online with the link.

    (or)

clone this repo then run on your machine with:
```
pip install -r requirements.txt
streamlit run telugu_text_gen.py
```

##You can get some telugu seed texts from here: 
https://te.wikipedia.org/wiki/
