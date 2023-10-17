import urllib.request
import urllib.error
import os

class App:
    def get_input_stream(self, file_or_url):
        input_stream = None
        try:
             if file_or_url.startswith("http") or file_or_url.startswith("https"):
                response = urllib.request.urlopen(file_or_url)
                input_stream = response.read()
             else:
                input_stream = open(file_or_url, "rb")
        except urllib.error.URLError as e:
            print("Invalid URL")
        except FileNotFoundError as e:
            print("File not found")
        except IOError as e:
            print("Error reading file")
        return input_stream


    get_input_stream()