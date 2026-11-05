from collections import Counter

log_file = "logs/auth.log"

failed_ips = []

with open(log_file, "r") as file:
    for line in file:
        if "Failed password" in line:
            ip = line.split("from ")[1].strip()
            failed_ips.append(ip)

print("SOC LOG ANALYZER")
print("----------------")

print("Total failed attempts:", len(failed_ips))

print("\nFailed attempts by IP:")

for ip, count in Counter(failed_ips).items():
    print(ip, ":", count)

print("\nSuspicious IPs:")

for ip, count in Counter(failed_ips).items():
    if count >= 3:
        print(ip)
