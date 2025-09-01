#background
I am building a streamlit app to be deployed to streamlit community cloud. Code will be pushed to GitHub
This app should allow users to upload image or take a photo. Then the app will recognize the photo and output the gradiants that are dangerous in text format.
please reference openrouter quick start.md, openrouter image input.md and openrouter streaming.md to setup openrouter. 

#styles
this app should be minimalist, modern, easy to use, clean and simple. works both on desktop and mobile.

#tech stack
1. use openrouter api to call vision language models for the image recognation and dangerous ingradiants output
2. use pillow to resize and compress to under 20MB before sending to openrouter api
3. api keys are stored in .env file in this working folder for desktop testing purposes. I will also store them in streamlit community cloud when deployed