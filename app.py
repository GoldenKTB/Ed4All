from flask import Flask, render_template, request
from translation import english, spanish, german, mandarin, finnish

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/problem")
def problem():
    return render_template("problem.html")

@app.route("/solution")
def solution():
    return render_template("Goals of solution.html")

@app.route("/prototype", methods=['GET', 'POST'])
def prototype():
    if request.method == "POST":
        select_start = request.form.get('start')
        select_end = request.form.get('end')
        translate = request.form.get('text_to_translate')
        match select_start:
            case "English":
                result = english(select_end.lower(), translate)
                print(result)
                return render_template("prototype.html", data=[{"languages":"English"}, {"languages":"Spanish"}, {"languages":"Finnish"}, {"languages":"German"}, {"languages":"Mandarin"}], translation_text=result)

            case "Spanish":
                result = spanish(select_end.lower(), translate)
                return render_template("prototype.html", data=[{"languages":"English"}, {"languages":"Spanish"}, {"languages":"Finnish"}, {"languages":"German"}, {"languages":"Mandarin"}], translation_text=result) 

            case "German":
                result = german(select_end.lower(), translate)
                return render_template("prototype.html", data=[{"languages":"English"}, {"languages":"Spanish"}, {"languages":"Finnish"}, {"languages":"German"}, {"languages":"Mandarin"}], translation_text=result) 

            case "Mandarin":
                result = mandarin(select_end.lower(), translate)
                return render_template("prototype.html", data=[{"languages":"English"}, {"languages":"Spanish"}, {"languages":"Finnish"}, {"languages":"German"}, {"languages":"Mandarin"}], translation_text=result) 

            case "Finnish":
                result = finnish(select_end.lower(), translate)
                return render_template("prototype.html", data=[{"languages":"English"}, {"languages":"Spanish"}, {"languages":"Finnish"}, {"languages":"German"}, {"languages":"Mandarin"}], translation_text=result) 

    return render_template("prototype.html", data=[{"languages":"English"}, {"languages":"Spanish"}, {"languages":"Finnish"}, {"languages":"German"}, {"languages":"Mandarin"}], translation_text="Translation")

if __name__ == "__main__":
    app.run()