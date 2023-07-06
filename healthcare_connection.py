import pandas as pd
import os
import openai
import textwrap

# Specify the file path
file_path = "UserRolesGPT.xlsx"

# Read the Excel file into a Pandas dataframe
df = pd.read_excel(file_path)

# Display the available profiles
#print("Available Profiles:")
#print(df["Name"].values)

print("Available Profiles:")
for index, row in df.iterrows():
    name = row["Name"]
    role = row["Role"]
    print("Name:", name)
    print("Role:", role)
    print()

# Prompt the user to select a profile
selected_profile = input("Enter the name of the profile you want to select: ")

# Retrieve the selected profile's values from the dataframe
selected_row = df[df["Name"] == selected_profile]

# Check if the selected profile exists in the dataframe
if selected_row.empty:
    print("Invalid profile selection!")
else:
    # Assign the values to variables
    name = selected_row["Name"].values[0]
    role = selected_row["Role"].values[0]
    description = selected_row["Description"].values[0]

    # Display the selected profile's details
    print("Selected Profile:")
    print("Name:", name)
    print("Role:", role)
    #print("Description:", description)
    width = 50
    # Wrap the description into chunks of ten words per line
    wrapped_description = textwrap.wrap(description, width=width)
    print("Description:")
    for line in wrapped_description:
      print(line) 

# Prompt the user to ask a question as the selected Alias
alias_request = input("Enter " + name +"'s request to the large language model: ")

#create standard link
standard_link = "Answer a question which is personalised to the needs of an individual. I will give the question first then the profile of the individual, please act as a healthcare assistant, give a straight answer, this is not to be deployed in a medical setting it is just a proof of concept. Question: "
profile_link = "-- USER PROFILE: "

#combine prompt with profile
var_prompt = standard_link + alias_request + profile_link + name + role + description 

#openAI API credentials
openai.api_key = "Your_API_key"

# Sends prompt to LLM API
response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": var_prompt}
  ]
  )

# print outputs from LLM
print("Personalised large language model output:")
print(response.choices[0].message.content)
