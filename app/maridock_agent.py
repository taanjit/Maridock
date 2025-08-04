# from phi.agent import Agent
# from phi.model.groq import Groq
# from dotenv import load_dotenv
# import os

# # Load environment variables from .env (expects GROQ_API_KEY)
# load_dotenv()

# # Initialize the Groq model
# groq_api_key = os.getenv("GROQ_API_KEY")
# model = Groq(id="llama3-70b-8192", api_key=groq_api_key)

# # Create an agent with the model
# agent = Agent(model=model)

# # Define user input and prompt
# user_input = "Main Engine Fuel Pump Overhauls"

# prompt = f"""
# Draft Professional but Generic Drydock Specifications for:-

# << user input >> "{user_input}"

# and provide report in the format –in the following sections of DESCRIPTION, SCOPE OF WORK/INSTRUCTIONS, MATERIAL & SUPPORT, SERVICE LINES, APPROVAL & SUPERVISION. Report in Uniform Font- Font family - 'Poppins', sans-serif; Font size: 14px, Remove spacing between Paragraphs and lines. Only 1 line spacing for Header/sub header from last section end.

# Print title of the SPECIFICATION in CAPITAL & BOLD

# DESCRIPTION

# This specification covers the…..

# Inventory Identification to be included in the DESCRIPTION Section. Allow Placeholders to list the different inventory on board, specify MAKE, MODEL, TYPE, OUTPUT / RATING, QTY – as RELEVANT for the ITEM & JOB - allow placeholders like [ ], to allow filling of items like MAKE, MODEL, TYPE, QUANTITY, NUMBER OF UNITS, LOCATION and Other Units of Measurements & specific details in the DESCRIPTION SECTION. Function of item / unit in Description NOT required.

# Location: 

# SCOPE OF WORK / INSTRUCTIONS

# Preparatory Measures:

# Job Breakdown:

# Standards & Compliance:

# Documentation:

# MATERIAL & SUPPORT

# Quantity of resources under MATERIAL & SUPPORT not required.

# Yard Supply:

# Test Equipment Required:

# Access & Logistics:

# SERVICE LINES

# APPROVALS & SUPERVISION

# Work Authorization:
# """


# # Run prompt and extract content from first message
# response = agent.run(prompt)
# # print(response.messages[1].content)
# output_text = response.messages[1].content  # ✅ FIXED

# # Format as HTML
# html_output = f"""
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <title>Drydock Specification - {user_input}</title>
#     <link href="https://fonts.googleapis.com/css2?family=Poppins&display=swap" rel="stylesheet">
#     <style>
#         body {{
#             font-family: 'Poppins', sans-serif;
#             font-size: 14px;
#             line-height: 1.4;
#             margin: 40px;
#             white-space: pre-wrap;
#         }}
#         .title {{
#             font-weight: bold;
#             text-transform: uppercase;
#             font-size: 18px;
#             margin-bottom: 1em;
#         }}
#     </style>
# </head>
# <body>
#     <div class="title">{user_input}</div>
#     <div>{output_text}</div>
# </body>
# </html>
# """

# # Save output
# with open("drydock_specification.html", "w", encoding="utf-8") as f:
#     f.write(html_output)

# print("✅ HTML specification page generated: drydock_specification.html")


from phi.agent import Agent
from phi.model.groq import Groq
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize the Groq model
groq_api_key = os.getenv("GROQ_API_KEY")
model = Groq(id="llama3-70b-8192", api_key=groq_api_key)
agent = Agent(model=model)

# Define user input and prompt
user_input = "Main Engine Fuel Pump Overhauls"

prompt = f"""
Draft Professional but Generic Drydock Specifications for:-

<< user input >> "{user_input}"

and provide report in the format –in the following sections of DESCRIPTION, SCOPE OF WORK/INSTRUCTIONS, MATERIAL & SUPPORT, SERVICE LINES, APPROVAL & SUPERVISION. Report in Uniform Font- Font family - 'Poppins', sans-serif; Font size: 14px, Remove spacing between Paragraphs and lines. Only 1 line spacing for Header/sub header from last section end.

Print title of the SPECIFICATION in CAPITAL & BOLD

DESCRIPTION

This specification covers the…..

Inventory Identification to be included in the DESCRIPTION Section. Allow Placeholders to list the different inventory on board, specify MAKE, MODEL, TYPE, OUTPUT / RATING, QTY – as RELEVANT for the ITEM & JOB - allow placeholders like [ ], to allow filling of items like MAKE, MODEL, TYPE, QUANTITY, NUMBER OF UNITS, LOCATION and Other Units of Measurements & specific details in the DESCRIPTION SECTION. Function of item / unit in Description NOT required.

Location: 

SCOPE OF WORK / INSTRUCTIONS

Preparatory Measures:

Job Breakdown:

Standards & Compliance:

Documentation:

MATERIAL & SUPPORT

Quantity of resources under MATERIAL & SUPPORT not required.

Yard Supply:

Test Equipment Required:

Access & Logistics:

SERVICE LINES

APPROVALS & SUPERVISION

Work Authorization:
"""

# Run the agent
response = agent.run(prompt)

# Extract model content
output_text = response.messages[1].content if len(response.messages) > 1 else response.messages[0].content

# Optional: Enhance Inventory Identification with HTML Table
inventory_table = """
<h2>Inventory Identification</h2>
<table border="1" cellspacing="0" cellpadding="8" style="border-collapse: collapse; width: 100%; font-family: 'Poppins', sans-serif; font-size: 14px;">
  <thead style="background-color: #f2f2f2; font-weight: bold;">
    <tr>
      <th>Item</th>
      <th>Make</th>
      <th>Model</th>
      <th>Type</th>
      <th>Output/Rating</th>
      <th>Qty</th>
      <th>Location</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>[Main Engine Fuel Pump]</td>
      <td>[MAKE]</td>
      <td>[MODEL]</td>
      <td>[TYPE]</td>
      <td>[OUTPUT/RATING]</td>
      <td>[QTY]</td>
      <td>[LOCATION]</td>
    </tr>
    <tr>
      <td>[Spare Fuel Pump]</td>
      <td>[MAKE]</td>
      <td>[MODEL]</td>
      <td>[TYPE]</td>
      <td>[OUTPUT/RATING]</td>
      <td>[QTY]</td>
      <td>[LOCATION]</td>
    </tr>
  </tbody>
</table>
"""

# Inject the table into the response if applicable
if "Inventory Identification:" in output_text:
    output_text = output_text.replace("Inventory Identification:", f"Inventory Identification:\n{inventory_table}")
else:
    output_text = inventory_table + "\n" + output_text

# Compose HTML
html_output = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Drydock Specification - {user_input}</title>
    <link href="https://fonts.googleapis.com/css2?family=Poppins&display=swap" rel="stylesheet">
    <style>
        body {{
            font-family: 'Poppins', sans-serif;
            font-size: 14px;
            line-height: 1.4;
            margin: 40px;
            white-space: pre-wrap;
        }}
        .title {{
            font-weight: bold;
            text-transform: uppercase;
            font-size: 18px;
            margin-bottom: 1em;
        }}
        table {{
            margin-top: 1em;
            margin-bottom: 1em;
        }}
    </style>
</head>
<body>
    <div class="title">{user_input}</div>
    <div>{output_text}</div>
</body>
</html>
"""

# Save to file
with open("drydock_specification.html", "w", encoding="utf-8") as f:
    f.write(html_output)

print("✅ HTML specification page generated: drydock_specification.html")
