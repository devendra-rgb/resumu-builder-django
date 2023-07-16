import gspread

data={
  "Certifications": [
    "Lean Six Sigma (Green Belt) Methodology from KPMG India",
    "Advanced Microsoft Excel from Great Learning\t",
    "Intermediate Tableau certification from DataCamp"
  ],
  "Awards and Achievements": [
    "Member of Placement Committee, Great Lakes Institute of Management, Gurgaon ",
    "Took part in Emerging Leadership Fellowship Program [2019] organized by Ananta Aspen Centre",
    "Conferred Best Student Award for my innovative contributions to various events hosted by the school"
  ],
  "SIP Project Description": "this is dummy",
  "roll_no": "P221D025",
  "Company Name-1": "MicroGO LLP, Chennai",
  "Designation-1": "Outreach Manager",
  "Industry-1": "Information Technology",
  "Duration-1\n (mons)": 10,
  "Role Description-1": ""
}



def update_data(data):
    sa = gspread.service_account(filename='/home/devendra/resumes/resumi/sepi/credi.json')
    sh = sa.open("college_data_info")
    wks = sh.worksheet("Sheet1")

    # Get column names from the first row
    column_names = wks.row_values(1)
    #print(column_names)
    # Find the column index based on the column name
    for k,v in data.items():
        if k!='roll_no':
            print(k,v)
            temp=''
            if type(v) == list:
                for i in v:
                    temp+=i+'.'
                v=temp

            col_index = column_names.index(k)

            # Find the row index based on the registration number
            
            row_index = wks.find(data['roll_no']).row

            # Update the cell value using row and column indexes
            #print(row_index,col_index)
            wks.update_cell(row_index, col_index+1, v)
           # print(f"done {k} {v}")

# update_data(data=data)

from datetime import datetime

def calculate_month_difference(start_timestamp, end_timestamp):
    start_date = datetime.strptime(start_timestamp, "%Y-%m-%d")
    end_date = datetime.strptime(end_timestamp, "%Y-%m-%d")

    # Calculate the difference in months
    months = (end_date.year - start_date.year) * 12 + (end_date.month - start_date.month)

    return months
