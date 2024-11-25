import ipaddress
from pathlib import Path

def getIPSet(filepath) -> set[str]:
    ip_set = set()
    with open(filepath, 'r') as f:
        for line in f:
            ip_set.add(line.strip())
    print(f"{filepath}: {len(ip_set)}")
    return ip_set


ip_set1 = getIPSet('ipip.txt')

directory = Path('../china-operator-ip')
# 只处理 ipv4
txt_files = [file.name for file in directory.glob('*.txt') if not file.stem.endswith('6')]

for file in txt_files:
    ip_set2 = getIPSet(directory / file)
    ip_set1.union(ip_set2)

assert len(ip_set1) != 0

sorted_ips = sorted(ip_set1, key=lambda ip: ipaddress.ip_network(ip, strict=False))

with open('merge.txt', 'w') as f:
    num = 0
    for ip in sorted_ips:
        num += 1
        f.write(ip + '\n')
    print(f"merge: {num}")

