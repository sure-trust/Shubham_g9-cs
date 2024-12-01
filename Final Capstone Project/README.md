# NetPilot

This project is a Flask-based web application that captures and analyzes network traffic. It supports real-time packet capture and pcap file uploads for traffic analysis. The application uses libraries like Scapy, Pandas, Matplotlib, and Tabulate for packet sniffing, data processing, and generating visual insights.

![Thumbnail](/img.png)

## Features

- **Real-Time Packet Capture:** Capture live network packets and analyze them directly in the browser.
- **PCAP File Analysis:** Upload `.pcap` or `.pcapng` files for analysis.
- **Data Visualization:** Visualize packet distribution using bar charts.
- **Tabular View:** View packet details in a neatly formatted table.

## Tech Stack

- **Backend:** Flask, Scapy, Pandas, Matplotlib, Tabulate
- **Frontend:** HTML, CSS
- **Deployment:** Works in any environment where Flask is supported.

## Setup and Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/prashant-sagar-shakya/NetPilot.git
    cd NetPilot
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the application:
    ```bash
    python app.py
    ```

5. Visit `http://127.0.0.1:5000` in your browser to access the app.

## Usage

### Packet Capture

1. On the homepage, enter the number of packets to capture (default is 10).
2. Click the "Capture" button to start capturing and analyzing packets.

### PCAP File Upload

1. Upload a `.pcap` or `.pcapng` file from the homepage.
2. The app will analyze the file and display the packet data in a table along with a bar chart visualization.
## Project Structure

```
.
├── app.py              # Main Flask application
├── templates/
│   ├── index.html      # Homepage template
│   └── results.html    # Results template
├── uploads/            # Directory for uploaded PCAP files
├── static/             # Static assets (CSS, JS, images)
└── README.md           # Project documentation
```

## Future Enhancements

- Support for additional protocols.
- Filtering options for captured or uploaded packets.
- Advanced visualizations like pie charts and histograms.
- Real-time packet capture with continuous updates.

## Contributing

Feel free to open issues and submit pull requests for improvements and feature requests. Contributions are welcome!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
