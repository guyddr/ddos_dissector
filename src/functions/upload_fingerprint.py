import json
import requests


def upload(pcap_file, fingerprint_path, username, password, key):
    """
    Upload a fingerprint and attack vector to DDoSDB
    :param pcap_file: Path to the pcap file
    :param fingerprint_path: Path to the fingerprint file
    :param username: DDoSDB username
    :param password: DDoSDB password
    :param key: ID to identify this attack, also the filename of the pcap_file.
    :return:
    """
    files = {
        "json": open(fingerprint_path, "rb"),
        "pcap": open(pcap_file, "rb")
    }
    headers = {
        "X-Username": username,
        "X-Password": password,
        "X-Filename": key
    }
    r = requests.post("https://ddosdb.org/upload-file", files=files, headers=headers)

    print(r.status_code)