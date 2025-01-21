import queue
import requests
import threading

def loadProxies(file_path):
    q = queue.Queue()
    with open(file_path) as f:
        lines = f.read().split("\n")
    for line in lines:
        if line.strip():
            q.put(line.strip())
    return q

def checkProxy(q):
    print("Testing proxies...")
    while not q.empty():
        proxy = q.get()
        try:
            res = requests.get(
                "https://httpbin.org/ip", 
                proxies={"http": proxy, "https": proxy},
                timeout=3
            )
            if res.status_code == 200:
                with open("working_proxy.txt", "a") as f:
                    f.write(proxy)
                    f.write("\n")
        except requests.exceptions.RequestException as e:
            continue
    print("Completed checking proxies.")

def runProxyChecker(file_path, num_threads=10):
    with open("working_proxy.txt","w"):
        pass

    q = loadProxies(file_path)
    threads = []

    for _ in range(num_threads):
        thread = threading.Thread(target=checkProxy, args=(q,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

runProxyChecker("proxy.txt",30)