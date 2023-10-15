#add import
import question_d

# global global_variable
global_variable = 60
print("global_variable before modify: ",global_variable)
value = question_d.use_global()
print("global_variable after modify: ",value)