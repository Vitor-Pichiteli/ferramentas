#installing a library to identify connections and process
import psutil
import socket
import scapy
import pyshark


if __name__ == "__main__":
    teste = psutil.disk_usage('/')

    bit_total = teste[0]


    gigabytes = bit_total / (8 * 1024 * 1024 * 1024)


    print('Total:', gigabytes)
