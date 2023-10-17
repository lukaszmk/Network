
def get_osi_layer_choice():
    while True:
        try:
            layer_number = int(input("\nEnter the OSI layer number (1-7) or type 'Exit' to quit: "))
            if 1 <= layer_number <= 7:
                return layer_number
            else:
                print("Invalid OSI layer number. Please enter a number between 1 and 7.")
        except ValueError:
            choice = input("Invalid choice. Type a number between 1-7 or 'Exit' to quit: ")
            if choice.lower() == 'exit':
                return None


def main():
    osi_layers = {
        1: {
            "name": "Physical",
            "description": "Defines the physical connection between the data link device and the transmission medium."
                           "WiFi, Bluetooth, and cable standard such as CAT5 and CAT6 operate at this layer.",
            "attacks": ["Jamming", "Eavesdropping", "Physical Tampering"],
            "protocols": ["USB", "Ethernet"]
        },
        2: {
            "name": "Data Link",
            "description": "Responsible for MAC addressing and physical addressing of frames.",
            "attacks": ["MAC spoofing", "ARP poisoning"],
            "protocols": ["Ethernet", "PPP"]
        },
        3: {
            "name": "Network",
            "description": "Determines the best path through the network for data and routes it. Describes how data "
                           "packets are routed between wider network such as the internet.",
            "attacks": ["IP spoofing", "Man-in-the-Middle", "Smurf Attack", "ICMP flood", "Route poisoning"],
            "protocols": ["IP", "ICMP", "RIP", "OSPF"]
        },
        4: {
            "name": "Transport",
            "description": "Ensures complete data transfer, error recovery, and flow control. Refers to how data "
                           "is actually transferred.",
            "attacks": ["SYN flood", "Session hijacking", "UDP Flood", "Sequence Prediction"],
            "protocols": ["TCP", "UDP", "SCTP"]
        },
        5: {
            "name": "Session",
            "description": "Establishes, maintains, and terminates user connections.",
            "attacks": ["Session hijacking", "Session fixation", "Main-in-the-middle attacks"],
            "protocols": ["NetBIOS", "RPC", "PPTP"]
        },
        6: {
            "name": "Presentation",
            "description": "Ensures that data is in a readable format for the application layer and the end user.",
            "attacks": ["SSL Stripping", "Data modification"],
            "protocols": ["SSL/TLS", "JPEG"]
        },
        7: {
            "name": "Application",
            "description": "Directly interacts with end-user applications, such as web browsers and email clients.",
            "attacks": ["DNS amplification", "Phishing", "SQL injection", "DDoS"],
            "protocols": ["HTTP/HTTPS", "FTP", "DNS", "SNMP", "SMTP"]
        }
    }

    while True:
        layer_number = get_osi_layer_choice()
        if layer_number is None:
            break

        layer_info = osi_layers.get(layer_number, None)

        if layer_info:
            print(f"\nLayer {layer_number}: {layer_info['name']}")
            print(f"Description: {layer_info['description']}")
            while True:
                choice = input("\nChoose an option:\n1. Common attacks\n2. Protocols\nType 'Exit' to go back.\n> ")

                if choice == "1":
                    print(f"\nCommon Attacks on {layer_info['name']} Layer:")
                    for attack in layer_info['attacks']:
                        print(f"- {attack}")
                elif choice == "2":
                    print(f"\nProtocols associated with {layer_info['name']} Layer:")
                    for protocol in layer_info['protocols']:
                        print(f"- {protocol}")
                elif choice.lower() == "exit":
                    break
                else:
                    print("Invalid choice. Try again or type 'Exit' to go back.")
        else:
            print("Invalid OSI layer number. Please enter a number between 1 and 7.")


if __name__ == "__main__":
    main()


