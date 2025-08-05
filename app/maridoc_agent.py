# import os
# from dotenv import load_dotenv
# from groq import Groq
# from reflection_pattern.reflection_agent import ReflectionAgent

# load_dotenv()


# def generate_drydock_specification(user_input):
#     # Create reflection agent
#     agent = ReflectionAgent(model="llama3-70b-8192")

#     # === USER INPUT ===
#     # Keep user_input from argument, don't override

#     # === STRUCTURED DRYDOCK PROMPT ===
#     base_prompt = f"""
#     REPAIR SPECIFICATION: MAIN ENGINE – FUEL PUMP OVERHAULS

#     SECTION 1: SFI CODE REFERENCE
#     - SFI Code: <span class="placeholder">[SFI_CODE]</span>
#     - System Classification: <span class="placeholder">[SYSTEM_CLASS]</span>
#     - Component Reference: <span class="placeholder">[COMPONENT_REF]</span>

#     SECTION 2: DESCRIPTION
#     This specification covers the overhaul of Main Engine Fuel Pumps [MAKE: <span class="placeholder">[MAKE]</span> | MODEL: <span class="placeholder">[MODEL]</span> | TYPE: <span class="placeholder">[TYPE]</span> | POWER: <span class="placeholder">[POWER]</span> | RPM: <span class="placeholder">[RPM]</span>].

#     - Location: <span class="placeholder">[LOCATION]</span>
#     - System Type: <span class="placeholder">[SYSTEM_TYPE]</span>
#     - Criticality Level: <span class="placeholder">[CRITICALITY]</span>

#     SECTION 3: SCOPE OF WORK / INSTRUCTIONS

#     Preparatory Measures:
#     - Isolate system, drain fuel lines
#     - Implement LOTO procedures
#     - Prepare work area, lighting, and PPE

#     Job Breakdown:
#     1. Dismount fuel pump
#     2. Disassemble and inspect components
#     3. Replace seals, springs, worn parts
#     4. Calibrate and test
#     5. Reinstall and verify alignment

#     <div class="safety-box">
#     <div class="subsection-title">Safety Controls:</div>
#     <ul>
#         <li>⚠️ Work under PTW system</li>
#         <li>Use appropriate PPE</li>
#         <li>Ensure gas-free and ventilation</li>
#         <li>Secure flammable materials</li>
#     </ul>
#     </div>

#     Standards & Compliance:
#     - OEM guidelines and class approval
#     - Flag state and port state rules
#     - SMMS procedures followed

#     Deliverables:
#     - Overhaul report with photos
#     - Calibration certificates
#     - Updated maintenance logs

#     SECTION 4: MATERIAL & SUPPORT

#     Owner Supply:
#     - <span class="placeholder">[SPARE_PARTS_LIST]</span>
#     - <span class="placeholder">[CONSUMABLES_LIST]</span>

#     Yard Supply:
#     - Basic tools, cleaning materials, PPE
#     - Temporary lighting

#     Test Equipment Required:
#     - Test bench, torque wrench

#     Access & Logistics:
#     - Crane access <span class="placeholder">[CRANE_CAPACITY]</span>
#     - Removal path, staging platform

#     SECTION 5: SERVICE LINES
#     <table>
#     <thead>
#         <tr>
#         <th>Service Line #</th>
#         <th>Description of Service</th>
#         <th>UoM</th>
#         <th>Qty</th>
#         <th>Remarks</th>
#         </tr>
#     </thead>
#     <tbody>
#         <tr>
#         <td>301.1</td>
#         <td>Overhaul of main engine fuel pump</td>
#         <td>Piece</td>
#         <td><span class="placeholder">[QTY]</span></td>
#         <td>Includes calibration and report</td>
#         </tr>
#         <tr>
#         <td>301.2</td>
#         <td>Testing and performance validation</td>
#         <td>Lump Sum</td>
#         <td>1</td>
#         <td>Witnessed by ship staff</td>
#         </tr>
#     </tbody>
#     </table>

#     SECTION 6: APPROVALS & SUPERVISION

#     Work Authorization:
#     - Chief Engineer
#     - Superintendent
#     - Class Surveyor (if required)

#     Quality Control:
#     - Supervision by ship staff
#     - Test reports reviewed
#     - Visual inspection

#     Documentation:
#     - Certificates, logs, reports, photo records
#     """

#     # === RUN REFLECTION AGENT ===
#     output_text = agent.run(
#         user_msg=base_prompt,
#         generation_system_prompt="You are an expert superintendent generating class-compliant drydock specification HTML.",
#         reflection_system_prompt="You are a specification reviewer ensuring formatting, structure, placeholder presence, and HTML style compliance.",
#         n_steps=2,
#         verbose=1
#     )

#     # === EMBED IN WORD-COMPATIBLE HTML ===
#     html_template = f"""
#     <!DOCTYPE html>
#     <html xmlns:o="urn:schemas-microsoft-com:office:office" xmlns:w="urn:schemas-microsoft-com:office:word" xmlns="http://www.w3.org/1999/xhtml">
#     <head>
#         <meta charset="UTF-8">
#         <meta name="ProgId" content="Word.Document">
#         <meta name="Generator" content="Microsoft Word">
#         <meta name="Originator" content="Microsoft Word">
#         <link href="https://fonts.googleapis.com/css2?family=Poppins&display=swap" rel="stylesheet">
#         <style>
#             body {{ font-family: 'Poppins', sans-serif; font-size: 14px; line-height: 1.6; }}
#             .main-title {{ font-weight: bold; text-transform: uppercase; font-size: 16px; margin-bottom: 20px; }}
#             .section-header {{ background-color: #000; color: #fff; font-weight: bold; padding: 8px; margin: 20px 0 10px 0; text-transform: uppercase; }}
#             .subsection-title {{ font-weight: bold; margin-top: 10px; }}
#             .safety-box {{ background-color: #fff3cd; border: 1px solid #ffeeba; padding: 12px; margin: 15px 0; }}
#             .placeholder {{ background-color: #e3f2fd; color: #0d47a1; font-weight: 600; padding: 2px 4px; }}
#             table {{ width: 100%; border-collapse: collapse; margin: 15px 0; font-size: 13px; }}
#             th, td {{ border: 1px solid #000; padding: 8px; text-align: left; }}
#             th {{ background-color: #f8f9fa; }}
#         </style>
#     </head>
#     <body>
#     <div class="main-title">REPAIR SPECIFICATION: {user_input.upper()}</div>
#     {output_text}
#     </body>
#     </html>
#     """

#     # with open(f"html_pages/{user_input.replace(' ', '_')}_drydock_specification.html", "w", encoding="utf-8") as f:
#     safe_filename = user_input.replace(' ', '_').replace('/', '_').replace('\\', '_')
#     with open(f"html_pages/{safe_filename}_drydock_specification.html", "w", encoding="utf-8") as f:
        
#         f.write(html_template)

#     print("✅ Word-compatible drydock specification generated as HTML.")
#     return 

# if __name__ == "__main__":
#     # This block is for testing purposes only
#     user_input = "MAIN ENGINE - FUEL INJECTION PUMP OVERHAUL"
#     print("Drydock specification generation completed successfully.")
#     generate_drydock_specification(user_input)


import os
from dotenv import load_dotenv
from groq import Groq
from reflection_pattern.reflection_agent import ReflectionAgent

load_dotenv()

# Create reflection agent
model1="meta-llama/llama-4-scout-17b-16e-instruct"
model2="llama3-70b-8192"
model3='gemma2-9b-it'
model4='qwen/qwen3-32b'
model5='llama-3.3-70b-versatile'
agent = ReflectionAgent(model=model5)

def generate_drydock_specification(user_input):
    prompt = f"""
    Generate a professional drydock specification in Word-compatible HTML for:
    {user_input}

    ### FORMAT GUIDELINES ###
    - Title: <div class="main-title">REPAIR SPECIFICATION: {user_input.upper()}</div>
    - Sections:
        1. DESCRIPTION ( sample data: This specification covers the overhaul, inspection, calibration, and reinstallation of Main Engine Fuel Injection Pumps, including integrated shock absorbers for the engine. The work shall include all pumps fitted onboard as part of the Main Engine fuel system.
        Inventory Identification:
        MAKE: [ ] 
        MODEL: [ ] 
        TYPE: [ ] 
        OUTPUT / RATING: [ ]  
        QUANTITY / NUMBER OF UNITS: [ ]  
        Location: [] )
        2. SCOPE OF WORK / INSTRUCTIONS (includes Preparatory Measures, Job Breakdown, Safety Controls, Standards & Compliance, Documentation)
            
        3. MATERIAL & SUPPORT
        (sample data: 
        -Owner Supply:
        Yard Supply:
        Test Equipment Required:
        Access & Logistics:)
        4. SERVICE LINES (must be a bordered table)

        5. APPROVALS & SUPERVISION
        (sample data:
        Work Authorization:
        - Work authorized and signed by Chief Engineer
        - Supervision by Owner’s Technical Superintendent
        - Maker’s certified engineer to oversee overhaul
        - Class Surveyor to inspect and endorse.
        Documentation:
        - Overhaul and calibration certificate per pump
        - Class endorsement and CSM entry
        - Photographic evidence of work performed)

    - Use span tags with class="placeholder" for placeholders like [MAKE], [MODEL], [LOCATION]
    - Font: 'Poppins', font-size: 14px, line-height: 1.6
    - Use <ul>, <ol>, and <table> appropriately
    - Include class="safety-box" for Safety Controls section
    - Output HTML body content only (without <html> or <head> tags)
    """

    output = agent.run(
        user_msg=prompt,
        generation_system_prompt="You are a marine technical writer creating structured, class-compliant drydock specification HTML documents for Word.",
        reflection_system_prompt="You are a ship superintendent reviewing HTML drydock specifications. Ensure all 5 required sections are present, formatted correctly, and styled with placeholders and classes (like 'main-title', 'placeholder', 'safety-box', and table structure). If formatting or content deviates, fix it.",
        n_steps=2,
        verbose=1
    )

    safe_filename = user_input.replace(" ", "_").replace("/", "_").replace("\\", "_")

    html_template = f"""
    <!DOCTYPE html>
    <html xmlns:o="urn:schemas-microsoft-com:office:office" xmlns:w="urn:schemas-microsoft-com:office:word" xmlns="http://www.w3.org/1999/xhtml">
    <head>
      <meta charset="UTF-8">
      <meta name="ProgId" content="Word.Document">
      <meta name="Generator" content="Microsoft Word">
      <meta name="Originator" content="Microsoft Word">
      <link href="https://fonts.googleapis.com/css2?family=Poppins&display=swap" rel="stylesheet">
      <style>
        body {{ font-family: 'Poppins', sans-serif; font-size: 14px; line-height: 1.6; margin: 20px; }}
        .main-title {{ font-size: 16px; font-weight: bold; text-transform: uppercase; margin-bottom: 20px; }}
        .section-header {{ background-color: #000; color: #fff; font-weight: bold; padding: 8px 12px; margin: 20px 0 10px 0; text-transform: uppercase; }}
        .placeholder {{ background-color: #e3f2fd; color: #0d47a1; font-weight: 600; padding: 2px 4px; }}
        .subsection-title {{ font-weight: 700; margin: 10px 0 5px 0; }}
        .safety-box {{ background-color: #fff3cd !important; border: 2px solid #ffeaa7; padding: 15px; margin: 15px 0; }}
        table {{ width: 100%; border-collapse: collapse; margin: 15px 0; font-size: 13px; }}
        th, td {{ border: 1px solid #000; padding: 8px; text-align: left; vertical-align: top; }}
        th {{ background-color: #f8f9fa; font-weight: 700; text-align: center; }}
      </style>
    </head>
    <body>
      <div class="main-title">REPAIR SPECIFICATION: {user_input.upper()}</div>
      {output}
    </body>
    </html>
    """

    os.makedirs("html_pages", exist_ok=True)
    with open(f"html_pages/{safe_filename}_drydock_specification.html", "w", encoding="utf-8") as f:
        f.write(html_template)

    print(f"✅ Saved: html_pages/{safe_filename}_drydock_specification.html")
