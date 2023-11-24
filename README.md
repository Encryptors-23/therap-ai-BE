# Backend + AI

## Done by Taavi Kalaluka and Grigory Provodin

### Link to demo on YouTube: [demo](https://www.youtube.com/watch?v=wovVZQlBUZ4)

**The main cryptography-related functions can be found in [encryption.py](./app/encryption.py), and they are used in [routes.py](./app/routes.py)**

The chatbot utilizes the OpenAI API, and the code can be found in [bot.py](./app/bot.py). Much of the setup was done on the OpenAI API panel, meaning that the application itself didn't need much code for inference.

### How to run

1. Clone the repository and navigate to the root directory in the terminal.
2. Create a virtual environment and activate it (optional):
    ```bash
    conda create -n therapy_bot
    conda activate therapy_bot
    ```
3. Install the requirements:
    ```bash
    pip install -r requirements.txt
    ```
4. Run the server:
    ```bash
    python run.py
    ```
