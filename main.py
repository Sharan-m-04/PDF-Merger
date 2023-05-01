from flask import Flask, render_template, request, send_file
from PyPDF2 import PdfMerger
from io import BytesIO

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        pdf_files = request.files.getlist("file")
        merger = PdfMerger()
        for pdf in pdf_files:
            merger.append(pdf)
        buffer = BytesIO()
        merger.write(buffer)
        buffer.seek(0)
        return send_file(buffer, as_attachment=True, download_name="Merged.pdf")

    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact-us")
def contact():
    return render_template("contact-us.html")

if __name__ == '__main__':
    app.run(debug=True)