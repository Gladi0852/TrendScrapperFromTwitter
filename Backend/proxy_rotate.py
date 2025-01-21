def rotateProxyList(file_path):
    first_proxy = ""
    with open(file_path, 'r') as f:
        proxies = f.readlines()

    proxies = [proxy.strip() for proxy in proxies]

    if proxies:
        first_proxy = proxies.pop(0)
        proxies.append(first_proxy)

        with open(file_path, 'w') as f:
            for proxy in proxies:
                f.write(proxy + "\n")
    return first_proxy

# proxy = rotateProxyList("working_proxy.txt")

# print(proxy)
