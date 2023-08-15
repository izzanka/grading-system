#!/usr/bin/env python
# coding: utf-8

# In[18]:


import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt


# In[19]:


# New Antecedent/Consequent objects hold universe variables and membership functions
test_score = ctrl.Antecedent(np.arange(0, 72, 1), 'test_score')
behavior_score = ctrl.Antecedent(np.arange(0, 86, 1), 'behavior_score')
grade = ctrl.Consequent(np.arange(0, 101, 1), 'grade')

# Custom membership functions for test score
test_score['poor'] = fuzz.trimf(test_score.universe, [0, 28, 40])
test_score['fair'] = fuzz.trimf(test_score.universe, [28, 40, 59])
test_score['good'] = fuzz.trimf(test_score.universe, [40, 59, 71])
test_score['excellent'] = fuzz.trimf(test_score.universe, [59, 71, 71])

test_score.view()


# In[20]:


# Custom membership functions for behavior score
behavior_score['poor'] = fuzz.trimf(behavior_score.universe, [0, 57, 65])
behavior_score['fair'] = fuzz.trimf(behavior_score.universe, [57, 65, 74])
behavior_score['good'] = fuzz.trimf(behavior_score.universe, [65, 74, 85])
behavior_score['excellent'] = fuzz.trimf(behavior_score.universe, [74, 85, 85])

behavior_score.view()


# In[21]:


# Custom membership functions for grade score
grade['D'] = fuzz.trimf(grade.universe, [0, 42, 54])
grade['C'] = fuzz.trimf(grade.universe, [42, 54, 67])
grade['B'] = fuzz.trimf(grade.universe, [54, 67, 77])
grade['A'] = fuzz.trimf(grade.universe, [67, 77, 100])

grade.view()


# In[22]:


# Fuzzy rules
rule1 = ctrl.Rule(behavior_score['poor'] & test_score['poor'], grade['D'])
rule2 = ctrl.Rule(behavior_score['poor'] & test_score['fair'], grade['D'])
rule3 = ctrl.Rule(behavior_score['poor'] & test_score['good'], grade['D'])
rule4 = ctrl.Rule(behavior_score['poor'] & test_score['excellent'], grade['D'])
rule5 = ctrl.Rule(behavior_score['fair'] & test_score['poor'], grade['D'])
rule6 = ctrl.Rule(behavior_score['fair'] & test_score['fair'], grade['D'])
rule7 = ctrl.Rule(behavior_score['fair'] & test_score['good'], grade['D'])
rule8 = ctrl.Rule(behavior_score['fair'] & test_score['excellent'], grade['C'])
rule9 = ctrl.Rule(behavior_score['good'] & test_score['poor'], grade['C'])
rule10 = ctrl.Rule(behavior_score['good'] & test_score['fair'], grade['C'])
rule11 = ctrl.Rule(behavior_score['good'] & test_score['good'], grade['B'])
rule12 = ctrl.Rule(behavior_score['good'] & test_score['excellent'], grade['B'])
rule13 = ctrl.Rule(behavior_score['excellent'] & test_score['poor'], grade['B'])
rule14 = ctrl.Rule(behavior_score['excellent'] & test_score['fair'], grade['A'])
rule15 = ctrl.Rule(behavior_score['excellent'] & test_score['good'], grade['A'])
rule16 = ctrl.Rule(behavior_score['excellent'] & test_score['excellent'], grade['A'])

print(rule1)
rule1.view()


# In[23]:


grading_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10, rule11, rule12, rule13, rule14, rule15, rule16])


# In[24]:


grading = ctrl.ControlSystemSimulation(grading_ctrl)

test_score_input = int(input("Input Test Score: "))
behavior_score_input = int(input("Input Behavior Score: "))

# Pass inputs to the ControlSystem using Antecedent labels with Pythonic API from user input
grading.input['test_score'] = test_score_input
grading.input['behavior_score'] = behavior_score_input

# Crunch the numbers
grading.compute()


# In[25]:


print(grading.output['grade'])

test_score.view(sim=grading)
behavior_score.view(sim=grading)
grade.view(sim=grading)


# In[ ]:




