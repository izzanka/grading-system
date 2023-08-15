#!/usr/bin/env python
# coding: utf-8

# In[1]:


import simpful as sf
from simpful import *


# In[2]:


FS = FuzzySystem()

T_1 = FuzzySet(function=Triangular_MF(a=0, b=28, c=40), term="poor")
T_2 = FuzzySet(function=Triangular_MF(a=28, b=40, c=59), term="fair")
T_3 = FuzzySet(function=Triangular_MF(a=40, b=59, c=71), term="good")
T_4 = FuzzySet(function=Triangular_MF(a=59, b=71, c=71), term="excellent")
FS.add_linguistic_variable("Test", LinguisticVariable([T_1, T_2, T_3, T_4], concept="Test Score", universe_of_discourse=[0,71]))


B_1 = FuzzySet(function=Triangular_MF(a=0, b=57, c=65), term="poor")
B_2 = FuzzySet(function=Triangular_MF(a=57, b=65, c=74), term="fair")
B_3 = FuzzySet(function=Triangular_MF(a=65, b=74, c=85), term="good")
B_4 = FuzzySet(function=Triangular_MF(a=74, b=85, c=85), term="excellent")
FS.add_linguistic_variable("Behavior", LinguisticVariable([B_1, B_2, B_3, B_4], concept="Behavior Score", universe_of_discourse=[0,85]))


# In[3]:


G_1 = FuzzySet(function=Triangular_MF(a=0, b=42, c=54), term="D")
G_2 = FuzzySet(function=Triangular_MF(a=42, b=54, c=67), term="C")
G_3 = FuzzySet(function=Triangular_MF(a=54, b=67, c=77), term="B")
G_4 = FuzzySet(function=Triangular_MF(a=67, b=77, c=100), term="A")
FS.add_linguistic_variable("Grade", LinguisticVariable([G_1, G_2, G_3, G_4], universe_of_discourse=[0,100]))


# In[4]:


R1 = "IF (Test IS poor) AND (Behavior IS poor) THEN (Grade IS D)"
R2 = "IF (Test IS fair) AND (Behavior IS poor) THEN (Grade IS D)"
R3 = "IF (Test IS good) AND (Behavior IS poor) THEN (Grade IS D)"
R4 = "IF (Test IS excellent) AND (Behavior IS poor) THEN (Grade IS D)"
R5 = "IF (Test IS poor) AND (Behavior IS fair) THEN (Grade IS D)"
R6 = "IF (Test IS fair) AND (Behavior IS fair) THEN (Grade IS D)"
R7 = "IF (Test IS good) AND (Behavior IS fair) THEN (Grade IS D)"
R8 = "IF (Test IS excellent) AND (Behavior IS fair) THEN (Grade IS C)"
R9 = "IF (Test IS poor) AND (Behavior IS good) THEN (Grade IS C)"
R10 = "IF (Test IS fair) AND (Behavior IS good) THEN (Grade IS C)"
R11 = "IF (Test IS good) AND (Behavior IS good) THEN (Grade IS B)"
R12 = "IF (Test IS excellent) AND (Behavior IS good) THEN (Grade IS B)"
R13 = "IF (Test IS poor) AND (Behavior IS excellent) THEN (Grade IS B)"
R14 = "IF (Test IS fair) AND (Behavior IS excellent) THEN (Grade IS A)"
R15 = "IF (Test IS good) AND (Behavior IS excellent) THEN (Grade IS A)"
R16 = "IF (Test IS excellent) AND (Behavior IS excellent) THEN (Grade IS A)"

FS.add_rules([R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12, R13, R14, R15, R16])


# In[7]:


test_score_input = int(input("Input Test Score: "))
behavior_score_input = int(input("Input Behavior Score: "))

FS.set_variable("Test", test_score_input)
FS.set_variable("Behavior", behavior_score_input)


# In[8]:


print(FS.Mamdani_inference(["Grade"]))


# In[ ]:





# In[ ]:




