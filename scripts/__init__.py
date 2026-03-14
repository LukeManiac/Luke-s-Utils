from collection_tools import *
from colour_utils import *
from general_utils import *
from math_functions import *
from collections import defaultdict
import types, random

module_functions = defaultdict(list)

for name in dir():
    obj = get_key(globals(), name)
    
    if isinstance(obj, types.FunctionType):
        module_function: list = get_key(module_functions, obj.__module__)
        module_function.append(name)

for module in module_functions:
    module_function: list = get_key(module_functions, module)
    module_function.sort()

sorted_module_functions = dict(sorted(module_functions.items()))

functions_count = 0
modules_count = 0

for module, funcs in sorted_module_functions.items():
    functions_count += len(funcs)
    modules_count += 1
    print(f"Successfully imported {", ".join(funcs)} from {module}.")

print(f"\nSuccessfully imported all {functions_count} functions from {modules_count} modules!\n")

welcome_messages = [
    "Welcome to Luke's Util Module v{version}! Ready to boost your workflow?",
    "Hello! Luke's Util Module v{version} is here to make life easier.",
    "Greetings! You've launched Luke's Util Module v{version}. Let's get started!",
    "Luke's Util Module v{version} says hi! Enjoy smooth coding.",
    "Ahoy! Luke's Util Module v{version} is on board. Adventure awaits!",
    "Welcome back! Luke's Util Module v{version} is ready for action.",
    "Hey there! Luke's Util Module v{version} is loaded and good to go.",
    "Salutations! Luke's Util Module v{version} is here to assist.",
    "Hi! Luke's Util Module v{version} is operational. Let's code smarter.",
    "Cheers! Luke's Util Module v{version} has arrived. Happy utilising!"
]
version = [1, 0, 0]
welcome_message: str = random.choice(welcome_messages)
message = welcome_message.format(version=".".join(str(num) for num in version))

print(message)