import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
authenticator = IAMAuthenticator('x7_SYX3wo1QiWo_jCxuYfN7s6YCHKCwHIfxsmiwfKyEH')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.us-south.language-translator.watson.cloud.ibm.com/instances/9b10d0c4-fdcf-478a-939e-10f0f3bd42b8')
def english_tofrench(english_text):
    """ translate english to french"""
    if english_text=="":
        french_text="null input"
    else:
        conv=language_translator.translate(english_text,model_id='en-fr').get_result()
        french_text=(['translations'][0]["translation"])
    #write the code here
    return french_text
def french_toenglish(english_text):
    """ translate french to english"""
    if french_text=="":
        english_text="null input"
    else:
        conv=language_translator.translate(french_text,model_id='fr-en').get_result()
        english_text=(['translations'][0]["translation"])
    #write the code here
    return english_text
