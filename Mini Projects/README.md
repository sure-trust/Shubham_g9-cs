# Text Encoder & Decoder

![Caesar Cipher](https://img.shields.io/badge/Flask-2.3.2-blue.svg) ![License](https://img.shields.io/badge/license-MIT-green.svg) ![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg) ![HTML](https://img.shields.io/badge/HTML5-239120.svg?&logo=html5&logoColor=white) ![CSS](https://img.shields.io/badge/CSS3-%231572B6.svg?&logo=css3&logoColor=white)

A simple and interactive Text Encoder-Decoder web application built using Flask, HTML, and CSS. This app allows you to encode and decode messages with utilizing the classic Cipher technique.

## Features

- **Encrypt & Decrypt**: Switch between encrypting and decrypting messages with a simple selection.
- **Interactive Interface**: User-friendly design with form validation.
- **Responsive Design**: Optimized for both desktop and mobile devices.
  
## Demo

![Image](img.jpg)

## Installation

To run this project locally, follow these steps:

### Prerequisites

- Python 3.8+
- pip (Python package manager)
- Virtual Environment (Optional but recommended)

### Clone the Repository

```bash
git clone https://github.com/shubhamisongit/encoder-decoder.git
cd encoder-decoder
```

### Set Up a Virtual Environment

**On Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**On macOS/Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
python app.py
```

Open your web browser and visit [http://127.0.0.1:5000](http://127.0.0.1:5000) to access the application.

## Usage

1. **Enter Text**: Type the text you wish to encrypt or decrypt in the provided input field.
2. **Choose Mode**: Click either "Encode" or "Decode" to determine the operation.

## Project Structure

```
CeaserCipher/
│
├── app.py                    # Main Flask application file
├── requirements.txt          # List of dependencies
├── static/                   # Static files directory
│   ├── css/
│   │   └── styles.css        # Custom CSS styles
│   ├── img/                  # Image directory for icons and images
│   │   └── favicon.ico       # Favicon file
└── templates/
    └── index.html            # HTML template for the web interface
```

## Contact

For any inquiries or support, please contact:

- **Name**: Shubham Choudhary
- **Email**: shubhamisonmail@gmail.com
- **GitHub**: [shubhamisongit](https://github.com/shubhamisongit)

---