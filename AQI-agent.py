import csv

class AQIReflexAgent:
    def __init__(self, rule_set):
        self.rules = rule_set

    def perceive(self, file_path):
        try:
            with open(file_path, mode='r') as file:
                reader = csv.DictReader(file)
                return [float(row['pm25']) for row in reader]
        except FileNotFoundError:
            return []

    def act(self, pm_value):
        if pm_value <= 12.0:
            return "Good (Green)"
        elif pm_value <= 35.4:
            return "Moderate (Yellow)"
        elif pm_value <= 55.4:
            return "Unhealthy for Sensitive Groups (Orange)"
        elif pm_value <= 150.4:
            return "Unhealthy (Red)"
        else:
            return "Hazardous (Purple)"

    def run(self, file_path):
        readings = self.perceive(file_path)
        for val in readings:
            status = self.act(val)
            print(f"{val}: {status}")

agent = AQIReflexAgent(rule_set="EPA_Standard")
agent.run('sensor_data.csv')
