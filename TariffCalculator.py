TARIFF_RATES = {
    "electronics": 0.05,
    "clothing": 0.12,
    "automobile": 0.025,
    "agriculture": 0.08,
    "furniture": 0.1,
    "other": 0.15
}

# Country-specific reciprocal tariff adjustment (as a multiplier, e.g., 30% = 1.30)
COUNTRY_RECIPROCAL_TARIFF = {
    "Algeria": 1.30, "Angola": 1.32, "Bangladesh": 1.37,
    "Bosnia and Herzegovina": 1.35, "Botswana": 1.37, "Brunei": 1.24,
    "Cambodia": 1.49, "Cameroon": 1.11, "Chad": 1.13, "China": 1.34,
    "Côte d`Ivoire": 1.21, "Democratic Republic of the Congo": 1.11,
    "Equatorial Guinea": 1.13, "European Union": 1.20, "Falkland Islands": 1.41,
    "Fiji": 1.32, "Guyana": 1.38, "India": 1.26, "Indonesia": 1.32,
    "Iraq": 1.39, "Israel": 1.17, "Japan": 1.24, "Jordan": 1.20,
    "Kazakhstan": 1.27, "Laos": 1.48, "Lesotho": 1.50, "Libya": 1.31,
    "Liechtenstein": 1.37, "Madagascar": 1.47, "Malawi": 1.17,
    "Malaysia": 1.24, "Mauritius": 1.40, "Moldova": 1.31,
    "Mozambique": 1.16, "Myanmar (Burma)": 1.44, "Namibia": 1.21,
    "Nauru": 1.30, "Nicaragua": 1.18, "Nigeria": 1.14,
    "North Macedonia": 1.33, "Norway": 1.15, "Pakistan": 1.29,
    "Philippines": 1.17, "Serbia": 1.37, "South Africa": 1.30,
    "South Korea": 1.25, "Sri Lanka": 1.44, "Switzerland": 1.31,
    "Syria": 1.41, "Taiwan": 1.32, "Thailand": 1.36, "Tunisia": 1.28,
    "Vanuatu": 1.22, "Venezuela": 1.15, "Vietnam": 1.46,
    "Zambia": 1.17, "Zimbabwe": 1.18
}

def get_tariff_rate(category):
    return TARIFF_RATES.get(category.lower(), TARIFF_RATES["other"])

def get_trade_multiplier(country):
    return COUNTRY_RECIPROCAL_TARIFF.get(country, 1.50)  # Default to highest if unknown

def calculate_tariff(value_per_item, quantity, tariff_rate, trade_multiplier):
    base_tariff = value_per_item * quantity * tariff_rate
    adjusted_tariff = base_tariff * trade_multiplier
    return round(adjusted_tariff, 2)

def main():
    print("US Tariff Calculator")
    print("------------------------")

    product_name = input("Enter product name: ")
    category = input("Enter product category (electronics, clothing, automobile, agriculture, furniture, other): ").strip().lower()
    origin_country = input("Enter country of origin (case-sensitive): ").strip()

    try:
        value_per_item = float(input("Enter value per item (USD): "))
        quantity = int(input("Enter quantity: "))
    except ValueError:
        print("Invalid number input.")
        return

    tariff_rate = get_tariff_rate(category)
    trade_multiplier = get_trade_multiplier(origin_country)

    tariff = calculate_tariff(value_per_item, quantity, tariff_rate, trade_multiplier)

    print("\n--- Tariff Summary ---")
    print(f"Product: {product_name}")
    print(f"Category: {category.title()}")
    print(f"Origin: {origin_country}")
    print(f"Declared Value: ${value_per_item * quantity:.2f}")
    print(f"Base Tariff Rate: {tariff_rate * 100:.2f}%")
    print(f"Reciprocal Adjustment Multiplier: x{trade_multiplier:.2f}")
    print(f"Total Tariff: ${tariff:.2f}")

if __name__ == "__main__":
    main()