network_logs = [
    {"time": "10:01", "traffic": 120, "link": "A"},
    {"time": "10:02", "traffic": 450, "link": "A"},
    {"time": "10:03", "traffic": 130, "link": "B"},
    {"time": "10:04", "traffic": 900, "link": "A"},
    {"time": "10:05", "traffic": 140, "link": "B"},
]

link_traffic = {}
for log in network_logs:
    link = log["link"]
    traffic = log["traffic"]
    if link not in link_traffic:
        link_traffic[link] = []
    link_traffic[link].append(traffic)

print("=" * 50)
print("ANALYSIS OF NETWORK TRAFFIC LOGS")
print("=" * 50)

print("\nAVERAGE TRAFFIC PER LINK:")
print("-" * 30)
for link, traffic_list in link_traffic.items():
    avg_traffic = sum(traffic_list) / len(traffic_list)
    print(f"Link {link}: {avg_traffic:.2f} (from {len(traffic_list)} records)")

print("\nMAXIMUM TRAFFIC OVERALL:")
print("-" * 30)
max_traffic = max(log["traffic"] for log in network_logs)
max_logs = [log for log in network_logs if log["traffic"] == max_traffic]
for log in max_logs:
    print(f"Maximum: {max_traffic} at {log['time']} on Link {log['link']}")

print("\nSUSPICIOUS TRAFFIC DETECTION:")
print("-" * 30)
print("Definition: Traffic > 3 standard deviations from link average")
print("(Or traffic > 700 for this small dataset)")

THRESHOLD = 700
suspicious_logs = []
for log in network_logs:
    if log["traffic"] > THRESHOLD:
        suspicious_logs.append(log)

if suspicious_logs:
    for log in suspicious_logs:
        print(f"Suspicious: {log['traffic']} at {log['time']} on Link {log['link']} "
              f"(Threshold: {THRESHOLD})")
else:
    print("No suspicious traffic detected")

print("\nSTATISTICAL ANALYSIS:")
print("-" * 30)
for link, traffic_list in link_traffic.items():
    if len(traffic_list) > 1:
        mean = sum(traffic_list) / len(traffic_list)
        variance = sum((x - mean) ** 2 for x in traffic_list) / len(traffic_list)
        std_dev = variance ** 0.5
        print(f"Link {link}: Mean = {mean:.2f}, Std Dev = {std_dev:.2f}")

print("\n" + "=" * 50)
print("SUMMARY")
print("=" * 50)
print(f"Total records analyzed: {len(network_logs)}")
print(f"Unique links: {list(link_traffic.keys())}")
print(f"Traffic range: {min(log['traffic'] for log in network_logs)} - "
      f"{max(log['traffic'] for log in network_logs)}")

print("\nORIGINAL DATA:")
print("-" * 50)
print(f"{'Time':<10} {'Traffic':<10} {'Link':<10}")
print("-" * 30)
for log in network_logs:
    traffic = log['traffic']
    # علامت‌گذاری مقادیر مشکوک
    marker = " ⚠️" if traffic > THRESHOLD else ""
    print(f"{log['time']:<10} {traffic:<10} {log['link']:<10}{marker}")

print("\n" + "=" * 50)
print("Analysis complete!")
print("=" * 50)

