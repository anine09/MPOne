import pyvisa
from rich.console import Console
from rich.markdown import Markdown

console = Console()
rm = pyvisa.ResourceManager()
print("")
number = input("GPIB: ")
inst = rm.open_resource(f'GPIB0::{number}::INSTR')
current_device = inst.query("*IDN? ")
print("")
print("Current Device: ")
print("")
print("\t" + current_device)

n = 1

while True:
    
    command = input(f"In[{n}]@ ")
    if command == "exit":
        break
    elif command[:2] == "q-":
        print(f"\nOut[{n}]: ", inst.query(f"{command[2:]}"))
    elif command == "read":
        print(f"\nOut[{n}]: ", inst.read())
    else:
        print(f"\nOut[{n}]: ", inst.write(f"{command}"))
    console.print(Markdown("---"))
    n += 1