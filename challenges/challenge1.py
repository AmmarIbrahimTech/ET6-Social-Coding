# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 15:30:30 2025

@author: somai
@editors:Team 9
- Safia Nouman
- Mohamad Firas Etaki
- Sadam Husen
- Ammar Osman
- Yevheniia Rudenko
- Hussaini Ahmed
- Obay Salih


Challenge 1: Detecting Suspicious Login Attempts
Objective:
The goal of this challenge is to practice Boolean algebra simplification. Students will write a Python program to simplify a
given Boolean expressions using Boolean Algebra’s law, helping them understand how to optimize logical expressions in 
programming.
Scenario:
A cybersecurity team is investigating an authentication system that occasionally flags legitimate login attempts as 
suspicious. The system checks multiple conditions to determine if a login attempt should be blocked.
One of the core checks involves the following rule:
¬(A∧(B∨¬B))
where:
A: The user has provided the correct login credentials.
B: The login attempt is from a trusted device.
The security team suspects that the system might be blocking users incorrectly due to redundant logic checks. Your task is
to simplify the logic to understand what the system is actually doing and determine if the rule is valid or needs 
modification.

Task:
Analyze the given Boolean expression.
Apply Boolean law to simplify it.
Interpret what the final expression means in the context of allowing or blocking a login attempt.

"""


'''
¬(A ∧(B∨¬B))
not (the user has provided correct credentials and (the device is trusted or untrusted))
¬A v ¬(Bv¬B)
¬A v ¬B ∧ B
¬A v 0
¬A
despite the device is trusted or not if the user hasn't provided correct credentials
he will be blocked
'''
A = True 
def login(A):
    if A:
        return "Login successful"
    else:
        return "Login blocked"
      
      
