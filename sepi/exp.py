data={
  "roll_no":"P221D025",
  "name": "Kaushik Gopalakrishnan Raman",
  "age": "24",
  "gender": "Male",
  "profilePicture": "",
  "summary": "12 months of experience in B2B digital marketing and sales, achieving organic outreach and sales conversion through custom-built information models, with a good understanding of client relationship management. Goal-focused individual with an analytical approach to solving problems with good communication and presentation skills.",
  "workExperience": [
    {
      "company": "MicroGO LLP, Chennai",
      "position": "Outreach Manager",
      "description": "",
      "keyAchievements": "Developed Branding guidelines and adopted Archetypes for effective sales & marketing\nIn charge of all outbound communication – sales & marketing [Newsletters, Flyers & Pitch Decks]\nCurated & managed Digital Media content, product documentation and website, achieved increased organic growth with Search Engine Optimization\nImplementation of useful information models [SOP] to analyze the flow of products from the early prototype stage [R&D] to its after-sales services [CRM]",
      "startYear": "2020-10-01",
      "endYear": "2021-10-01",
      'industry':"Artificial Intelligence"
    }
  ],
  "summerIntern": [
    {
      "company": "COSGrid Networks, Chennai",
      "position": "Product Marketing Intern",
      "description": "",
      "keyAchievements": "Developed a comprehensive Go-to-Market (GTM) strategy framework, focusing on specific products/services, target markets, and competitive landscape\nAssessed competitor products in the cybersecurity sector, analyzing functionalities and capabilities based on customer reviews.\nConducted market research and analysis to identify product-market fit and target medium-sized businesses in Bengaluru and Chennai\nDevised a bench test to optimize targeting and reduce marketing expenses, contributing to the development of Sales conversion SOP\nLed the development of branding guidelines, including logo design, archetype definition, tone, typography, iconography, and brand palette.",
      "startYear": "2023-04-01",
      "endYear": "2023-06-01"
    }
  ],
  "education": [
    {
      "degree": "PGDM",
      "year": "2024-07-12",
      "school": "Great Lakes Institute of Management, Gurgaon",
      "cgpa": "Pursuing"
    },
    {
      "degree": "B. Tech (Aeronautical)",
      "year": "2021-03-01",
      "school": "Hindustan University, Chennai",
      "cgpa": "77.1%"
    },
    {
      "degree": "12th",
      "year": "2017-03-16",
      "school": "Indian School Wadi Kabir, Muscat, Oman",
      "cgpa": "73.6%"
    },
    {
      "degree": "10th",
      "year": "2015-06-16",
      "school": "Indian School Wadi Kabir, Muscat, Oman",
      "cgpa": "9.4"
    }
  ],
  "projects": [
    {
      "title": "",
      "link": "",
      "description": "",
      "keyAchievements": "Roles & Responsibilities comprise of maintenance of flight-deck instruments, radio comm. & nav. equipment, onboard computers, In-flight entertainment, Weather radar, Displays & Cockpit Voice Recorder [CVR] readout.",
      "startYear": "2019-12-16",
      "endYear": "2020-01-16",
      "name": " Air India Engg. Services Ltd, Mumbai"
    },
    {
      "title": "",
      "link": "",
      "description": "",
      "keyAchievements": "Group project in Marketing Management on Radico Khaitan Ltd. [RKL], analysed the market profile and marketing strategies using concepts such as SWOT, PESTEL analysis, Porter’s 5 forces & STP [2022]",
      "startYear": "2022-03-16",
      "endYear": "2022-04-16"
    },
    {
      "title": "",
      "link": "",
      "description": "",
      "keyAchievements": "Vision-based SLAM Algorithm for Quadcopter, final-year project [Published on IJMA under Vol.10 No.2 (2021)]",
      "startYear": "2020-05-16",
      "endYear": "2021-07-16"
    }
  ],
  "skills": [
    {
      "title": "Skills & Certifications",
      "skills": [
        "Lean Six Sigma (Green Belt) Methodology from KPMG India",
        "Advanced Microsoft Excel from Great Learning\t",
        "Intermediate Tableau certification from DataCamp"
      ]
    }
  ],
  "extraActivities": [
    "Best Director Award in Inter-Collegiate Drama Fest organized by Vaishnav College, Chennai [2019]",
    "Runners-up in Short Film Making Competition – Jhankaar Spectrum hosted by Indian School Muscat [2015]"
  ],
  "awards": [
    "Member of Placement Committee, Great Lakes Institute of Management, Gurgaon ",
    "Took part in Emerging Leadership Fellowship Program [2019] organized by Ananta Aspen Centre",
    "Conferred Best Student Award for my innovative contributions to various events hosted by the school"
  ],
  "SIP":"this is dummy"
}
saving_data={}
saving_data['Certifications']=data['skills'][0]['skills']
saving_data['Awards and Achievements']=data['awards']
saving_data['SIP Project Description']=data['SIP']
saving_data['roll_no']= 'P221D025'
for i in range(len(data['workExperience'])):
    j=data['workExperience'][i]
    #import pdb;pdb.set_trace()
    saving_data[f'Company Name-{i+1}'] = j['company']
    saving_data[f'Designation-{i+1}'] = j['position']
    saving_data[f'Industry-{i+1}'] = j['industry']
    saving_data[f'Duration-{i+1}\n (mons)'] = 10
    saving_data[f'Role Description-{i+1}'] = j['description']
print(saving_data)



# print(data.keys())
#print(data['skills'][0]['skills'])

