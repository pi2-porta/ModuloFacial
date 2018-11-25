import threading
import find_target


macs = ['1','12','123']
results = []
for mac in macs:
    t = threading.Thread(target=find_target.teste, args=(mac,results))
    t.start()
    t.join()

print(results)
