from flask import Flask, request, render_template
from query import getResponse
import pyttsx3

# Flask constructor
app = Flask(__name__)

# A decorator used to tell the application
# which URL is associated function

def speak(audio):
    """
    This function convert text to 
    speech using pyttsx3 module. male voice.
    """
    try:
        engine = pyttsx3.init()
        # engine.setProperty()
        engine.say(audio)
        engine.runAndWait()
    except Exception as e:
        print(e) 
             
def getResponse(query):
    if 'hey' in query:
        speak("Hello bro")

@app.route('/', methods=["GET", "POST"])
def sendData():
    if request.method == "POST":
        # getting input with name = query in HTML form
        print("Getting post request")
        # user_query = request.form.get("userInput")
        message = request.form.get('userInput')
        print(message)
        getResponse(message)
        # print(user_query,+message)
        # response = getResponse(user_query)
        # print(response) 
        # return response
        # print("Submitted")
    return render_template("index.html")


  


    #               ___
    #              (. .)
    #             |.   .|
    #             |.   .|
    #             |.   .|
    #             |.   .|
    #             |.   .|
    #             |.   .|  _____    ____
    #      ____   |.   .|  |.  .|  /  .|
    #     /.   |. |.   .|  |.  .| |.  .|
    #     |.    |.|.   .|  |.  .| |.   /
    #     \.    |.|.   .| /.   .|     ./
    #      \.                        ./
    #       \.                      ./
    #         \.                   ./
    #           \.               ./
    #            \.           ./

     

if __name__ == '__main__':
    app.run(debug = True)
  