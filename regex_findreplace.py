###############################################
##
##  lines that need to be replaced:
##
##  include "utilities/SP.hh" , with:
##  include <memory>
##
##  typedef SP<InputDB> SP_input; , with:
##  typedef std::shared_ptr<InputDB> SP_Input;
##
##  q = new PolarGL(np); , with:
##  q = std::make_shared<PolarGL>(np);
##
###############################################

import re

line = ""

#  include "utilities/SP.hh" , with:
#  include <memory>

re.sub(r'#include "utilities/SP\.hh"', "#include <memory>", line)

print(line)

#   typedef SP<InputDB> SP_input; , with:
#   typedef std::shared_ptr<InputDB> SP_Input;

reg_ex3 = re.compile(r"typedef SP<(.*)> (.*);")

result = reg_ex1.search(line)
if result:
    1 = result.group(1)
    2 = result.group(2)
    re.sub(reg_ex, "typedef std::shared_ptr<"+1+"> "+2+";", line)

##  q = new PolarGL(np); , with:
##  q = std::make_shared<PolarGL>(np);

print(line)

reg_ex2 = re.complie(r"(.*) = new (.*)/((.*)/);")

result = reg_ex2.search(line)
if result:
    3 = result.group(1)
    4 = result.group(2)
    5 = result.group(3)
    re.sub(reg_ex, 3+" = std::make_shared<"+4+">("+5+");")
    
print(line)


	

