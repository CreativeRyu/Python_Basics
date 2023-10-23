# # # # Lv 13 Debugging and Errorhandling # # # #

"""
  _                                  _   
 | |_ _ _ _  _   _____ ____ ___ _ __| |_ 
 |  _| '_| || | / -_) \ / _/ -_) '_ \  _|
  \__|_|  \_, | \___/_\_\__\___| .__/\__|
          |__/                 |_|       
"""

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

"""
+=============+
|   ToolBox   |
+=============+
"""

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# try:
# 	# It's a place where
# 	# you can do something 
#     # without asking for permission.
# except:
# 	# It's a spot dedicated to 
#     # solemnly begging for forgiveness.

try:
    value = int(input('Enter a natural number: '))
    print('The reciprocal of', value, 'is', 1/value)        
except:
    print('I do not know what to do.')

# # # # # # # # # # # # # # # # # # # # # # # # #

# mehrfache Exceptions behandeln
# wenn ein Zweig ausgelöst wird werden die anderen nicht mehr beachtet
# default Exception immer an letzter Stelle
try:
    value = int(input('Enter a natural number: '))
    print('The reciprocal of', value, 'is', 1/value)        
except ValueError:
    print('I do not know what to do.')    
except ZeroDivisionError:
    print('Division by zero is not allowed in our Universe.') 
except:
    print('Something strange has happened here... Sorry!')


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


"""
+=============+
|  Questline  |
+=============+
"""

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

"""
+================================+
|                                |
|  Lv 9 Quest 1 Grading Program  |
|                                |
+================================+
"""