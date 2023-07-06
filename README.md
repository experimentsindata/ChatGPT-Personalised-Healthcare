# ChatGPT-Personalised-Healthcare

This code demonstrates a script that connects to the OpenAI GPT-3.5 language model to provide personalized healthcare advice based on user profiles. It reads an Excel file containing user profiles with attributes like name, role, and description, and allows the user to select a profile and ask a question related to healthcare. The code then sends the user's question along with the profile details to the OpenAI API, retrieves the response, and displays it.

The script utilizes the pandas library to read an Excel file and store the data in a dataframe. It prompts the user to select a profile by displaying the available profiles and their corresponding names and roles. The user's selected profile is used to retrieve the profile's description from the dataframe.

To interact with the OpenAI language model, the script uses the OpenAI Python library. It prompts the user to enter a question as the selected profile and constructs a prompt string combining the question, profile name, role, and description. The prompt is then sent to the GPT-3.5 language model via the OpenAI API.

Finally, the script prints the personalized response obtained from the language model, providing tailored healthcare advice based on the user's selected profile and question.

**Readme:**

This repository contains a Python script that connects to the OpenAI GPT-3.5 language model to provide personalized healthcare advice based on user profiles. The script reads an Excel file containing user profiles and allows the user to select a profile and ask a healthcare-related question. The code then sends the question along with the profile details to the OpenAI API, retrieves the response, and displays it.

**Prerequisites:**
- Python 3.x
- pandas library (`pip install pandas`)
- openai library (`pip install openai`)

**Instructions:**
1. Clone the repository or download the script.
2. Install the required libraries by running `pip install pandas openai`.
3. Replace the "UserRolesGPT.xlsx" file with your own Excel file containing user profiles. Make sure the file has columns for "Name", "Role", and "Description".
4. Open the Python script and provide your OpenAI API key by replacing `openai.api_key = "YOUR_API_KEY"`.
5. Run the script using a Python interpreter.
6. Follow the on-screen instructions to select a profile and enter a healthcare-related question.
7. The script will send the question and profile details to the GPT-3.5 language model via the OpenAI API.
8. The personalized response from the language model will be displayed.

Please note that this script is a proof of concept and should not be deployed in a medical setting. It serves as a demonstration of how the OpenAI language model can provide tailored healthcare advice based on user profiles.
