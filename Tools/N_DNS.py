import dns.resolver
import tkinter as tk
from tkinter import ttk, scrolledtext

def perform_dns_lookup(target_domain, record_types):
    # Create a DNS resolver
    resolver = dns.resolver.Resolver()

    try:
        results_text.delete(1.0, tk.END)  # Clear previous results
        for record_type in record_types:
            # Perform DNS lookup for the specified domain and record type
            answers = resolver.resolve(target_domain, record_type)

            # Append the answers to the results text widget
            results_text.insert(tk.END, f"{record_type} records for {target_domain}:\n")
            for rdata in answers:
                results_text.insert(tk.END, f" {rdata}\n")

    except dns.resolver.NoAnswer:
        results_text.insert(tk.END, f"No records found for {target_domain}\n")
    except dns.resolver.NXDOMAIN:
        results_text.insert(tk.END, f"The domain {target_domain} does not exist.\n")
    except dns.exception.DNSException as e:
        results_text.insert(tk.END, f"An error occurred: {e}\n")

def perform_dns_lookup_from_gui():
    target_domain = domain_entry.get().strip()

    if not target_domain:
        results_text.insert(tk.END, "Please provide a valid domain name.\n")
    else:
        record_types = ["A", "AAAA", "CNAME", "MX", "NS", "SOA", "TXT"]
        perform_dns_lookup(target_domain, record_types)

# Create the main Tkinter window
root = tk.Tk()
root.title("DNS Enumaration")
root.iconbitmap("D:\\Multipurpose Cybersecurity Tool\\Favicon\\DNS Enumeration.ico")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set fixed window size and make it non-resizable
root.resizable(False, False)
x_coordinate = (screen_width - 500) // 2
y_coordinate = (screen_height - 400) // 2
root.geometry(f"500x400+{x_coordinate}+{y_coordinate}")

# Create and place widgets in the window
label_domain = ttk.Label(root, text="Enter the target domain:", font=("Arial", 13))
label_domain.grid(row=0, column=0, padx=10, pady=10)

domain_entry = ttk.Entry(root, font=("Arial", 13))
domain_entry.grid(row=0, column=1, padx=20, pady=10)

style = ttk.Style()
style.configure("TButton", font=("Arial", 10))

lookup_button = ttk.Button(root, text="Perform DNS Lookup", command=perform_dns_lookup_from_gui, style="TButton")
lookup_button.grid(row=1, column=0, padx=20, pady=10)

results_text = scrolledtext.ScrolledText(root, width=50, height=15, wrap=tk.WORD)
results_text.grid(row=2, column=0, columnspan=3, padx=20, pady=10)

# Run the Tkinter event loop
root.mainloop()
