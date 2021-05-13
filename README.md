r# Telugu_text_generator

A simple AI text generator (telugu language) which takes a seed text as input and generates some text related to the seed text as output.

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
