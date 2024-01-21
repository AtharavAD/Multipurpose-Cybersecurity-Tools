import requests
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin
from tkinter import Tk, Label, Entry, Button, Text, END

# initialize an HTTP session & set the browser
s = requests.Session()
s.headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36"

def get_all_forms(url):
    """Given a `url`, it returns all forms from the HTML content"""
    soup = bs(s.get(url).content, "html.parser")
    return soup.find_all("form")

def get_form_details(form):
    """This function extracts all possible useful information about an HTML `form`"""
    details = {}
    # get the form action (target url)
    try:
        action = form.attrs.get("action").lower()
    except:
        action = None
    # get the form method (POST, GET, etc.)
    method = form.attrs.get("method", "get").lower()
    # get all the input details such as type and name
    inputs = []
    for input_tag in form.find_all("input"):
        input_type = input_tag.attrs.get("type", "text")
        input_name = input_tag.attrs.get("name")
        input_value = input_tag.attrs.get("value", "")
        inputs.append({"type": input_type, "name": input_name, "value": input_value})
    # put everything into the resulting dictionary
    details["action"] = action
    details["method"] = method
    details["inputs"] = inputs
    return details

def is_vulnerable(response):
    """A simple boolean function that determines whether a page 
    is SQL Injection vulnerable from its `response`"""
    errors = {
        # MySQL
        "you have an error in your sql syntax;",
        "warning: mysql",
        # SQL Server
        "unclosed quotation mark after the character string",
        # Oracle
        "quoted string not properly terminated",
    }
    for error in errors:
        # if you find one of these errors, return True
        if error in response.content.decode().lower():
            return True
    # no error detected
    return False

def scan_sql_injection(url, result_text):
    # test on URL
    for c in "\"'":
        # add quote/double quote character to the URL
        new_url = f"{url}{c}"
        result_text.insert(END, f"[!] Trying {new_url}\n")
        result_text.update_idletasks()  # Update the GUI to display the progress
        # make the HTTP request
        res = s.get(new_url)
        if is_vulnerable(res):
            # SQL Injection detected on the URL itself, 
            # no need to proceed for extracting forms and submitting them
            result_text.insert(END, f"[+] SQL Injection vulnerability detected, link: {new_url}\n")
            result_text.update_idletasks()  # Update the GUI to display the result
            return
    # test on HTML forms
    forms = get_all_forms(url)
    result_text.insert(END, f"[+] Detected {len(forms)} forms on {url}.\n")
    result_text.update_idletasks()  # Update the GUI to display the result
    for form in forms:
        form_details = get_form_details(form)
        for c in "\"'":
            # the data body we want to submit
            data = {}
            for input_tag in form_details["inputs"]:
                if input_tag["type"] == "hidden" or input_tag["value"]:
                    # any input form that is hidden or has some value,
                    # just use it in the form body
                    try:
                        data[input_tag["name"]] = input_tag["value"] + c
                    except:
                        pass
                elif input_tag["type"] != "submit":
                    # all others except submit, use some junk data with a special character
                    data[input_tag["name"]] = f"test{c}"
            # join the url with the action (form request URL)
            url = urljoin(url, form_details["action"])
            if form_details["method"] == "post":
                res = s.post(url, data=data)
            elif form_details["method"] == "get":
                res = s.get(url, params=data)
            # test whether the resulting page is vulnerable
            if is_vulnerable(res):
                result_text.insert(END, f"[+] SQL Injection vulnerability detected, link: {url}\n")
                result_text.insert(END, "[+] Form:\n")
                result_text.insert(END, f"{form_details}\n")
                result_text.update_idletasks()  # Update the GUI to display the result
                break

def on_scan_button_click():
    url = url_entry.get()
    if url:
        result_text.delete(1.0, END)
        result_text.insert(END, f"Scanning SQL Injection for URL: {url}\n")
        scan_sql_injection(url, result_text)
    else:
        result_text.delete(1.0, END)
        result_text.insert(END, "Please enter a URL to scan.\n")

# Create the main Tkinter window
root = Tk()
root.title("SQL Injection Vulnerability Scanner")
root.iconbitmap("D:\\Multipurpose Cybersecurity Tool\\Favicon\\SQL Injection.ico")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set fixed window size and make it non-resizable
root.resizable(False, False)
x_coordinate = (screen_width - 800) // 2
y_coordinate = (screen_height - 500) // 2
root.geometry(f"510x400+{x_coordinate}+{y_coordinate}")

# Create and place widgets in the window
label_url = Label(root, text="Enter URL:", font=("Arial", 10))
label_url.place(x=22, y=22)

url_entry = Entry(root, width=40, font=("Arial", 13))
url_entry.place(x=120, y=23)

scan_button = Button(root, text="Scan SQL Injection", command=on_scan_button_click, font=("Arial", 10))
scan_button.place(x=170, y=64)

result_text = Text(root, width=51, height=12, wrap="word", font=("Arial", 13))
result_text.place(x=22, y=110)

# Run the Tkinter event loop
root.mainloop()
