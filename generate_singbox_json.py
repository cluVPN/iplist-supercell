import json

# Читаем CIDR-списки IPv4 и IPv6
with open("cidr4.txt", "r") as f:
    ipv4_cidrs = [line.strip() for line in f if line.strip()]

with open("cidr6.txt", "r") as f:
    ipv6_cidrs = [line.strip() for line in f if line.strip()]

# Формируем JSON в формате ip_cidr
singbox_rules = {
    "rules": [
        {"ip_cidr": cidr} for cidr in ipv4_cidrs + ipv6_cidrs
        }
    ]
}

# Сохраняем в JSON-файл
with open("singbox_rules.json", "w") as f:
    json.dump(singbox_rules, f, indent=4)
