import bluetooth

def find_target(addr, results):
    services = bluetooth.find_service(address= addr)

    if not services:
        results.append(False)
    else:
        results.append(True)

    return
