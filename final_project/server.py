from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def english_tfFrench():
    textToTranslate = request.args.get('textToTranslate')
    text=transalator.english_tofrench( textToTranslate)
    # Write your code here
    return text

@app.route("/frenchToEnglish")
def french_toenglish():
    textToTranslate = request.args.get('textToTranslate')
    text1=transalator.french_toenglish( textToTranslate)
    # Write your code here
    return text1

@app.route("/")
def renderIndexPage():
    return render_template('index.html')
    # Write the code to render template

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
