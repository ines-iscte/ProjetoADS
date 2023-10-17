from App import App
import sys

def main():
    print("Olá")
    app = App()
    file_or_url="HorarioDeExemplo.csv"
    input_stream = app.get_input_stream(file_or_url)

    if input_stream is not None:
        # Process the input stream as needed
        print("Input stream obtained successfully.")
    else:
        print("Failed to obtain input stream.")
