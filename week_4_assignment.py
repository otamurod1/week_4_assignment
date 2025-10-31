def calculate_delivery_revenue(order_type, deliveries_completed, time_period):
    if order_type == "express":
        if time_period == "morning":
            rate = 8
        elif time_period == "lunch":
            rate = 12
        else:
            rate = 18
    elif order_type == "regular":
        if time_period == "morning":
            rate = 5
        elif time_period == "lunch":
            rate = 8
        else:
            rate = 12
    elif order_type == "bulk":
        if time_period == "morning":
            rate = 15
        elif time_period == "lunch":
            rate = 22
        else:
            rate = 30
    else:
        rate = 0

    total_revenue = rate * deliveries_completed
    return total_revenue


def calculate_completion_rate(driver_months, baseline_orders, completed_orders):
    expected_orders = 1000 + (driver_months * 100)
    order_capacity = expected_orders - baseline_orders
    completion_percent = ((completed_orders - baseline_orders) / order_capacity) * 100
    return round(completion_percent, 1)


def determine_driver_tier(completion_percent):
    if completion_percent < 50:
        return "Starter Tier"
    elif completion_percent < 60:
        return "Bronze Tier"
    elif completion_percent < 70:
        return "Silver Tier"
    elif completion_percent < 85:
        return "Gold Tier"
    else:
        return "Elite Tier"


def calculate_total_earnings(revenue, deliveries, tier):
    if tier == "Starter Tier":
        tier_bonus = 0.5
    elif tier == "Bronze Tier":
        tier_bonus = 1.0
    elif tier == "Silver Tier":
        tier_bonus = 1.2
    elif tier == "Gold Tier":
        tier_bonus = 1.5
    else:
        tier_bonus = 1.8

    base_earnings = revenue * 0.05 + deliveries * 2
    total = base_earnings * tier_bonus
    return round(total, 1)


def needs_route_optimization(delivery_days, total_deliveries, avg_completion):
    if delivery_days >= 6 and avg_completion < 50:
        return True
    elif total_deliveries < 100 and avg_completion < 60:
        return True
    elif delivery_days >= 4 and avg_completion < 40:
        return True
    else:
        return False


def generate_delivery_summary(driver_name, order_type, deliveries, time_period,
                              driver_months, baseline_orders, completed_orders, delivery_days):
    print(f"Delivery Summary for: {driver_name}")
    print("----------------------------------------")
    print(f"Order Type: {order_type}")
    print(f"Deliveries Completed: {deliveries}")
    print(f"Time Period: {time_period}")

    revenue = calculate_delivery_revenue(order_type, deliveries, time_period)
    print(f"Delivery Revenue: ${revenue}")

    completion_rate = calculate_completion_rate(driver_months, baseline_orders, completed_orders)
    tier = determine_driver_tier(completion_rate)

    print("Completion Analysis:")
    print(f"  Experience: {driver_months} months, Baseline: {baseline_orders}, Completed Orders: {completed_orders}")
    print(f"  Completion Rate: {completion_rate}%")
    print(f"  Driver Tier: {tier}")

    total_earnings = calculate_total_earnings(revenue, deliveries, tier)
    print(f"Total Earnings: ${total_earnings}")

    optimization_needed = needs_route_optimization(delivery_days, deliveries, completion_rate)
    print(f"Delivery Days: {delivery_days}")
    if optimization_needed:
        print("Route Optimization Needed: Yes")
    else:
        print("Route Optimization Needed: No")
    print()


print("FOOD DELIVERY PERFORMANCE TRACKER")
print("========================================")

generate_delivery_summary("Drew", "bulk", 45, "dinner", 3, 800, 1150, 3)
print("========================================")

generate_delivery_summary("Ellis", "regular", 60, "lunch", 5, 900, 1300, 5)
print("========================================")

generate_delivery_summary("Frankie", "express", 30, "morning", 8, 850, 950, 7)
