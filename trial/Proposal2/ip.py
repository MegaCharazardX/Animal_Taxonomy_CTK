
import tkinter as tk
import customtkinter as ctk
from scapy.all import ARP, Ether, srp

# Function to scan the local network
def scan_network():
    # Define the network range to scan
    target_ip = "192.168.1.69"#"192.168.1.1"  # Adjust this range based on your local network "192.168.1.69"
    # Create an ARP packet
    arp = ARP(pdst=target_ip)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp

    result = srp(packet, timeout=3, verbose=0)[0]
    
    # A list of discovered devices
    devices = []
    for sent, received in result:
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})
    
    return devices

# Function to update the device list in the GUI
def update_device_list():
    devices = scan_network()
    device_list.delete(0, tk.END)
    for device in devices:
        device_info = f"IP: {device['ip']}, MAC: {device['mac']}"
        device_list.insert(tk.END, device_info)

# Setting up the custom Tkinter GUI
root = ctk.CTk()
root.title("WiFi Users Location")

frame = ctk.CTkFrame(root)
frame.pack(pady=20, padx=20, fill="both", expand=True)

device_list = tk.Listbox(frame, width=50, height=15)
device_list.pack(pady=20)

refresh_button = ctk.CTkButton(frame, text="Refresh", command=update_device_list)
refresh_button.pack(pady=10)

root.mainloop()
