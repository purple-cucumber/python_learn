# 8.15
import printing_functions
unprinted_designs = ['phon case','robot pendant' , 'dodecahedron']
completed_models = []
printing_functions.print_models(unprinted_designs,completed_models)
#8.16
# import num8_5
# from num8_5 import sanwiches_make
# from num8_5 import sanwiches_make as sanwich
# import num8_5 as sanwich
from num8_5 import *
sanwiches_make("Sausage","cherry")
car = make_car('subaru', 'outback' , color = 'blue',tow_package = True)
print(car)