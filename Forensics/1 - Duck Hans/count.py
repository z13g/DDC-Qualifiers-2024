from collections import Counter

log_file_path = 'Network Log.txt'

ip_counter = Counter()

with open(log_file_path, 'r') as file:
    for line in file:
        fields = line.strip().split(' | ')
        if len(fields) >= 2:
            source_ip = fields[1]
            ip_counter[source_ip] += 1

for ip, count in ip_counter.items():
    if count > 10:
        print(f"IP-adresse: {ip}, Count: {count}")
