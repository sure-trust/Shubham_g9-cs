from scapy.all import sniff
import pandas as pd
from tqdm import tqdm
from tabulate import tabulate
from scapy.all import conf
print(conf.use_pcap)


def capture_traffic():
    packets = []

    def packet_handler(packet):
        packets.append([packet.time, packet.summary()])

    print("Starting packet capture...")
    sniff(prn=packet_handler, count=50)  # Capture 50 packets

    df = pd.DataFrame(packets, columns=["Timestamp", "Summary"])
    tqdm.pandas()

    print(tabulate(df, headers="keys", tablefmt="pretty"))

    return df.to_dict(orient='records')
