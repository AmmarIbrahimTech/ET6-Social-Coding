# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 15:30:30 2025

@author: somai
@editors: Team 9
- Safia Nouman
- Mohamad Firas Etaki
- Sadam Husen
- Ammar Osman
- Yevheniia Rudenko
- Hussaini Ahmed
- Obay Salih
Challenge 2: Digital Access Control
Objective
Use set operations to analyze and improve a company's digital access control system while identifying potential security risks in data access.
Scenario
A secure company vault stores sensitive data, where employees are granted access based on their roles:
Finance Team (F): Needs access to financial records.
Tech Team (T): Needs access to technical documents.
Some employees belong to both teams due to cross-departmental responsibilities.
Access Data (Given)
The security system tracks employee IDs (formatted as "E####").
finance_access = {"E0435", "E1021", "E3098", "E7642", "E8873", "E6590"}
tech_access = {"E7642", "E8873", "E6590", "E9812", "E4520"}
Additionally, two special cases exist:
E0001 (Admin): Has access to all data but is not listed in specific access groups.
E9999 (New Employee): Has no assigned access yet.
Your Task
Analyze the current access structure and identify potential security risks by answering the following:
Who has access to at least one type of data?
"E0435", "E1021", "E3098", "E7642", "E8873", "E6590" "E7642", "E9812", "E4520", "E0001"
Who has access to both financial and technical data?
"E0001", "E8873", "E6590"
Who has exclusive access to only one type of data?
"E0435", "E1021", "E3098", "E7642", "E7642", "E9812", "E4520"
Which employees currently lack access (but exist in the system)?
"E9999"

Are there unnecessary overlaps in access that could pose a security risk?
the employes who have dual access to both tech and financial data

What changes would you recommend to enhance security and minimize excessive access?
for employes who have what dual access the admin should give them permission


# -*- coding: utf-8 -*-

"""
