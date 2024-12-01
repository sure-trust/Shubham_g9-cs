from flask import Flask, render_template, request
from scapy.all import sniff, rdpcap
import pandas as pd
import matplotlib.pyplot as plt
from tabulate import tabulate
import io
import base64
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['ALLOWED_EXTENSIONS'] = {'pcap', 'pcapng'}

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def capture_packets(packet_count):
    packets = sniff(count=packet_count)
    return packets

def analyze_packets(packets):
    data = []
    for pkt in packets:
        if pkt.haslayer("IP"):
            src = pkt["IP"].src
            dst = pkt["IP"].dst
            proto = pkt["IP"].proto
            length = len(pkt)
            data.append([src, dst, proto, length])
    return pd.DataFrame(data, columns=["Source", "Destination", "Protocol", "Length"])

def generate_visuals(df):
    table = tabulate(df, headers='keys', tablefmt='html')

    plt.figure(figsize=(10, 6))
    df['Length'].plot(kind='bar', color='skyblue')
    plt.title('Packet Length Distribution')
    plt.xlabel('Packet Index')
    plt.ylabel('Length')
    plt.tight_layout()

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    img = base64.b64encode(buffer.getvalue()).decode()
    buffer.close()

    return table, img

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['GET', 'POST'])
def analyze():
    if request.method == 'POST':
        if 'file' in request.files and request.files['file'].filename != '':
            file = request.files['file']
            if allowed_file(file.filename):
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
                file.save(filepath)

                # Read and analyze the uploaded PCAP file
                packets = rdpcap(filepath)
                df = analyze_packets(packets)
                table, img = generate_visuals(df)

                return render_template('results.html', table=table, img=img)

        packet_count = int(request.form.get('packet_count', 10))  # Default to 10 if not provided
        print(packet_count)
        packets = capture_packets(packet_count)
        df = analyze_packets(packets)
        table, img = generate_visuals(df)
        return render_template('results.html', table=table, img=img)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)