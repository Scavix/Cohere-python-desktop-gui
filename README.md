# Cohere-python-desktop-gui
A (basic and unofficial) Python desktop app utilizing PySimpleGUI and requests to interact via the Cohere LLM API based on user prompts.
This project is a Python application that interacts with the Replicate AI API to generate images using a given prompt and seed. It utilizes the PySimpleGUI library for creating a user interface, as well as the requests library for making API calls and the Pillow library (PIL) for handling images.

## Getting Started

1. Clone this repository to your local machine.

```
git clone https://github.com/Scavix/Cohere-python-desktop-gui.git
cd Cohere-python-desktop-gui
```

2. Install the required dependencies. Make sure you have Python and pip installed.

```
pip install -r requirements.txt
```
3.  Obtain an API key from Cohere dashboard (the GUI allows you to save it locally)

## Usage
Run the main.py script to start the application.

```
python main.py
```

1. The application window will appear, allowing you to input the prompt and the API token.

2. If you want to save the API key for future use, check the "Save KEY" checkbox.

3. Click the "Ok" button to receive a response based on the provided input.

4. Once the response is received and the images are generated, they will be displayed in the interface.

5. If the API response indicates an error, the request content will be displayed.

## GUI Screenshot
<p align="center">
    <img src="https://github.com/Scavix/Cohere-python-desktop-gui/blob/main/GUI.PNG" />
</p>

## License
This project is licensed under the [MIT License](https://choosealicense.com/licenses/mit/) .

Feel free to modify and enhance the project as needed. If you encounter any issues or have questions, please don't hesitate to open an issue on this repository.
