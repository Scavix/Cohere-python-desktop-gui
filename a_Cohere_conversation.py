import PySimpleGUI as sg
import requests
from TokenManager import TokenManager
import os

#https://docs.cohere.com/reference/chat

def main():
    url = 'https://api.cohere.ai/v1/chat'

    api_manager = TokenManager("api_key.key")
    if os.path.exists("api.txt"):
        with open("api.txt", "rb") as f:
            encrypted_api = f.read()
        api = api_manager.decrypt(encrypted_api)
    else:
        api='INSERT API KEY HERE'

    layout = [
        [sg.Text('Enter API token'), sg.InputText(key='-API-', default_text=api)],
        [sg.Text("Enter your message: "), sg.InputText(key="-MESSAGE-", default_text="Who invented the Internet?")],
        [sg.Button("Send"), sg.Button("Generate source"), sg.Button("Build script"),sg.Checkbox(text='Save KEY',key='-CBOX-', default=True), sg.Button("Exit")],
        [sg.Output(size=(60, 10))]
    ]

    window = sg.Window("Cohere local LLM GUI", layout, element_justification='c')

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == "Exit":
            break

        if event == "Generate source":
            response = requests.get("https://raw.githubusercontent.com/Scavix/Cohere-python-desktop-gui/main/a_Cohere_conversation.py")
            if response.status_code == 200:
                f = open("a_Cohere_conversation.py", "w")
                f.write(response.text)
                f.close()
                sg.popup("Done main source code")
            response = requests.get("https://raw.githubusercontent.com/Scavix/Cohere-python-desktop-gui/main/TokenManager.py")
            if response.status_code == 200:
                f = open("TokenManager.py", "w")
                f.write(response.text)
                f.close()
                sg.popup("Done TokenManager source code")
            else:
                sg.popup("Web site does not exist or is not reachable")
                        
        if event == "Build script":
            response = requests.get("https://raw.githubusercontent.com/Scavix/Cohere-python-desktop-gui/main/a_Cohere_conversation_build_script.bat")
            if response.status_code == 200:
                f = open("a_Cohere_conversation_build_script.bat", "w")
                f.write(response.text)
                f.close()
                sg.popup("Done")
            else:
                sg.popup("Web site does not exist or is not reachable")

        if event == "Send":
            if window['-CBOX-'].get():
                api = window['-API-'].get()
                encrypted_api = api_manager.encrypt(api)
                with open("api.txt", "wb") as f:
                    f.write(encrypted_api)

            message = values["-MESSAGE-"]

            headers = {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + api,
                'accept': 'application/json'
            }

            data = {
                'message': message,
                'connectors': [
                    {
                        'id': 'web-search'
                    }
                ]
            }
            response = requests.post(url, headers=headers, json=data)
            if response.status_code == 200:
                print(response.json()['text'])
            else:
                print(response.status_code + response.text)

    window.close()

if __name__ == "__main__":
    main()