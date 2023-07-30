# PDF Merger Web App

<img width="960" alt="Demo" src="https://github.com/Sharan-m-04/PDF-Merger/assets/101189789/21757f34-4e82-4253-84d0-ce91ab259892">

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
4. [Usage](#usage)
5. [Dependencies](#dependencies)
6. [How To Use](#how-to-use)
7. [Contributing](#contributing)
8. [Contact](#contact)

## 1. Introduction <a name="introduction"></a>

PDF Merger Web App is a simple Flask-based web application that allows users to merge multiple PDF files into one single PDF. It uses BytesIO to perform the merging process without uploading the files to the server. The web app provides an intuitive user interface for easy and efficient merging of PDF documents.

## 2. Features <a name="features"></a>

- Merge multiple PDF files into one single PDF.
- Drag and drop files directly onto the website.
- Easy-to-use and user-friendly interface.
- No need to upload files to the server for merging.

## 3. Getting Started <a name="getting-started"></a>

### Prerequisites <a name="prerequisites"></a>

- Python 3.x installed on your system.

### Installation <a name="installation"></a>
To run the PDF Merger Web App locally, follow these steps:
1. Clone the repository or download the project from [GitHub](https://github.com/Sharan-m-04/PDF-Merger).
   ```bash
   git clone https://github.com/Sharan-m-04/PDF-Merger
   git cd PDF-Merger
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 4. Usage <a name="usage"></a>

To run the PDF Merger Web App, follow these steps:

1. Run the Flask application:
  ```bash
flask run
```
2. Open your web browser and navigate to `http://localhost:5000` to access the PDF Merger Web App.
3. Follow the on-screen instructions to merge your PDF files seamlessly.

## 5. Dependencies <a name="dependencies"></a>
The PDF Merger Web App relies on the following key dependencies:
- Flask: A lightweight web application framework in Python.
- PyPDF2: A library to work with PDF files and perform PDF merging operations.

All the dependencies are listed in the `requirements.txt` file and will be installed during the installation process.

## 6. How To Use <a name="how-to-use"></a>
Follow these simple steps to merge PDF files using the PDF Merger Web App:

- **Step 1:** Open the web app by running the application as mentioned in the Usage section.
- **Step 2:** Drag and drop the PDF files you want to merge onto the web page, or click the "Choose" button to browse and select the files from your computer.
- **Step 3:** Arrange the files in the correct order if necessary. If the files are not already named in ascending order, take the time to rename them to ensure the correct merging order.
- **Step 4:** Click on the "Merge" button to start the merging process. The merged PDF file will be generated automatically.
- **Step 5:** The merged PDF file will be downloaded automatically after the merging process is completed.
- **Step 6:** After downloading or saving the merged PDF file, check to make sure that all pages and content are in the correct order and that there are no errors or missing pages.

That's it! With these simple steps, you can quickly and easily merge your PDF files into one organized document.
## 7. Contributing <a name="contributing"></a>
Contributions to this project are welcome. If you find any issues or want to add new features, feel free to open an issue or submit a pull request on [GitHub](https://github.com/Sharan-m-04/PDF-Merger).
## 8. Contact <a name="contact"></a>
For any inquiries or feedback, you can reach out to the project developer:

- **Sharan M**
- GitHub: [Sharan-m-04](https://github.com/Sharan-m-04)
