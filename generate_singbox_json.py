import json

# Читаем CIDR-списки IPv4 и IPv6
with open("cidr4.txt", "r") as f:
    ipv4_cidrs = [line.strip() for line in f if line.strip()]

with open("cidr6.txt", "r") as f:
    ipv6_cidrs = [line.strip() for line in f if line.strip()]

# Формируем JSON в формате ip_cidr
singbox_rules = {
    "version": 2,
    "rules": [
        "ip_cidr": ipv4_cidrs + ipv6_cidrs
    ]
}

# Сохраняем в JSON-файл
with open("supercell.json", "w") as f:
    json.dump(singbox_rules, f, indent=4)
