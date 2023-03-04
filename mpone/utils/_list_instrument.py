import pyvisa

def list_instrument():
    rm = pyvisa.ResourceManager()
    list_resources = rm.list_resources()
    
    return list_resources

if __name__ == "__main__":
    print(list_instrument())