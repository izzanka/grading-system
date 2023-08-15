#!/usr/bin/env python
# coding: utf-8

# In[1]:


import simpful

from simpful import *


# In[2]:


#membuat object fuzzy system
FS = FuzzySystem()


# In[3]:


# mendefinisikan himpunan fuzzy dan variabel linguistic untuk test score
T_1 = FuzzySet(points=[[0., 1.], [28., 0.], [40., 0.]], term="poor")
T_2 = FuzzySet(points=[[28., 0.], [40., 1.], [59., 0.]], term="fair")
T_3 = FuzzySet(points=[[40., 0.], [59., 1.], [71., 0.]], term="good")
T_4 = FuzzySet(points=[[59., 0.], [71., 1.]], term="excellent")

FS.add_linguistic_variable("Test", LinguisticVariable([T_1, T_2, T_3, T_4], concept="Test Score"))


# In[4]:


# mendefinisikan himpunan fuzzy dan variabel linguistic untuk behavior score
B_1 = FuzzySet(points=[[0., 1.], [57., 0.], [65., 0.]], term="poor")
B_2 = FuzzySet(points=[[57., 0.], [65., 1.], [74., 0.]], term="fair")
B_3 = FuzzySet(points=[[65., 0.], [74., 1.], [85., 0.]], term="good")
B_4 = FuzzySet(points=[[74., 0.], [85., 1.]], term="excellent")

FS.add_linguistic_variable("Behavior", LinguisticVariable([B_1, B_2, B_3, B_4], concept="Behavior Score"))


# In[5]:


# menentukan nilai output crisp grade
FS.set_crisp_output_value("D", 42)
FS.set_crisp_output_value("C", 54)
FS.set_crisp_output_value("B", 67)
FS.set_crisp_output_value("A", 77)


# In[6]:


# menentukan aturan fuzzy
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


# In[13]:


# menetapkan nilai test score dan behavior score dari input user
test_score_input = int(input("Input Test Score: "))
behavior_score_input = int(input("Input Behavior Score: "))

FS.set_variable("Test", test_score_input)
FS.set_variable("Behavior", behavior_score_input)


# In[14]:


# melakukan inferensi sugeno dan mencetak hasilnya
print(FS.Sugeno_inference(["Grade"]))


# In[ ]:




