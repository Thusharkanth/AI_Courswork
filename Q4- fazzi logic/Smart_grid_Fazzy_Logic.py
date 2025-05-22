# -----------------------------
# Fuzzy Logic-Based Anomaly Detection and Correction
# For Smart Grid Systems
# -----------------------------

# Manual Implementation (No heavy libraries like skfuzzy)

# --- Step 1: Define Membership Functions ---

"""Membership function for Voltage Deviation."""
def voltage_membership(voltage):    
    if voltage < 5:
        return {"Low": 1, "Medium": 0, "High": 0}
    elif 5 <= voltage < 10:
        return {"Low": (10 - voltage) / 5, "Medium": (voltage - 5) / 5, "High": 0}
    elif 10 <= voltage < 15:
        return {"Low": 0, "Medium": (15 - voltage) / 5, "High": (voltage - 10) / 5}
    else:
        return {"Low": 0, "Medium": 0, "High": 1}

"""Membership function for Frequency Variation."""
def frequency_membership(frequency_variation):
    if frequency_variation < 0.2:
        return {"Stable": 1, "Unstable": 0}
    elif 0.2 <= frequency_variation < 0.5:
        return {"Stable": (0.5 - frequency_variation) / 0.3, "Unstable": (frequency_variation - 0.2) / 0.3}
    else:
        return {"Stable": 0, "Unstable": 1}

"""Membership function for Load Imbalance."""
def load_imbalance_membership(imbalance):
    if imbalance < 10:
        return {"Balanced": 1, "Unbalanced": 0}
    elif 10 <= imbalance < 20:
        return {"Balanced": (20 - imbalance) / 10, "Unbalanced": (imbalance - 10) / 10}
    else:
        return {"Balanced": 0, "Unbalanced": 1}

# --- Step 2: Define Fuzzy Rules ---

"""Apply fuzzy rules and determine severity level."""
def evaluate_rules(voltage_fuzzy, frequency_fuzzy, load_fuzzy):
    rules = []

    # Rule 1
    severity_high = min(voltage_fuzzy["High"], frequency_fuzzy["Unstable"], load_fuzzy["Unbalanced"])
    rules.append(("High", severity_high))

    # Rule 2
    severity_medium = min(voltage_fuzzy["Medium"], frequency_fuzzy["Unstable"], load_fuzzy["Unbalanced"])
    rules.append(("Medium", severity_medium))

    # Rule 3
    severity_low = min(voltage_fuzzy["Low"], frequency_fuzzy["Stable"], load_fuzzy["Balanced"])
    rules.append(("Low", severity_low))

    # Rule 4
    severity_medium2 = min(voltage_fuzzy["Medium"], frequency_fuzzy["Stable"], load_fuzzy["Unbalanced"])
    rules.append(("Medium", severity_medium2))

    # Rule 5
    severity_high2 = min(voltage_fuzzy["High"], frequency_fuzzy["Stable"], load_fuzzy["Balanced"])
    rules.append(("Medium", severity_high2))

    return rules

# --- Step 3: Defuzzification ---

"""Convert fuzzy outputs into crisp severity level."""
def defuzzify(rules):
    severity_levels = {"Low": 1, "Medium": 5, "High": 9}  # Numerical scale
    numerator = 0
    denominator = 0

    for severity, strength in rules:
        numerator += severity_levels[severity] * strength
        denominator += strength

    if denominator == 0:
        return 0  # No anomaly detected
    crisp_severity = numerator / denominator
    return crisp_severity

"""Decide corrective action based on severity score and fault type."""
def decide_action(crisp_severity, voltage_fuzzy, frequency_fuzzy, load_fuzzy):
    actions = []

    # High severity action
    if crisp_severity >= 7:
        if voltage_fuzzy["High"] > 0:
            actions.append("High Voltage Deviation: Isolate Faulty Section")
        if frequency_fuzzy["Unstable"] > 0:
            actions.append("Frequency Instability: Frequency Regulation Activated")
        if load_fuzzy["Unbalanced"] > 0:
            actions.append("Load Imbalance: Load Balancing Initiated")
    # Medium severity action
    elif crisp_severity >= 4:
        if voltage_fuzzy["Medium"] > 0:
            actions.append("Medium Voltage Deviation: Adjust Voltage Levels")
        if frequency_fuzzy["Stable"] > 0 and frequency_fuzzy["Unstable"] > 0:
            actions.append("Frequency Instability: Adjust Frequency")
        if load_fuzzy["Unbalanced"] > 0:
            actions.append("Load Imbalance: Adjust Load Distribution")
    # Low severity action
    elif crisp_severity > 0:
        actions.append("Low Severity: Monitoring Only")
    else:
        actions.append("No Action Needed")

    return actions

# --- Step 4: Simulation (Test Cases) ---

"""Simulate a test case."""
def simulate_scenario(voltage_dev, frequency_var, load_imbalance):
    print(f"\nSimulating Scenario: Voltage={voltage_dev}%, Frequency Var={frequency_var}Hz, Load Imbalance={load_imbalance}%")
    
    voltage_fuzzy = voltage_membership(voltage_dev)
    frequency_fuzzy = frequency_membership(frequency_var)
    load_fuzzy = load_imbalance_membership(load_imbalance)

    rules = evaluate_rules(voltage_fuzzy, frequency_fuzzy, load_fuzzy)
    crisp_severity = defuzzify(rules)
    actions = decide_action(crisp_severity, voltage_fuzzy, frequency_fuzzy, load_fuzzy)

    print(f"Detected Severity Score: {crisp_severity:.2f}")
    print(f"Recommended Actions: {', '.join(actions)}")

# --- Step 5: Run Test Cases ---

if __name__ == "__main__":
    # Test Case 1: Normal Condition
    simulate_scenario(voltage_dev=3, frequency_var=0.1, load_imbalance=5)

    # Test Case 2: Medium Anomaly
    simulate_scenario(voltage_dev=8, frequency_var=0.3, load_imbalance=15)

    # Test Case 3: Severe Anomaly
    simulate_scenario(voltage_dev=12, frequency_var=0.6, load_imbalance=25)
