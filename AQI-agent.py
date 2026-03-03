import csv

class AQIModelBasedAgent:
    def __init__(self, rule_set="Official_Breakpoints"):
        self.rules = rule_set

    def perceive(self, file_path):
        try:
            with open(file_path, mode='r') as file:
                reader = csv.DictReader(file)
                return [float(row['pm25']) for row in reader]
        except FileNotFoundError:
            return []

    def act(self, x):
        if x <= 30:
            return x * 50 / 30
        elif x <= 60:
            return 50 + (x - 30) * 50 / 30
        elif x <= 90:
            return 100 + (x - 60) * 100 / 30
        elif x <= 120:
            return 200 + (x - 90) * 100 / 30
        elif x <= 250:
            return 300 + (x - 120) * 100 / 130
        elif x > 250:
            return 400 + (x - 250) * 100 / 130
        else:
            return 0

    def run(self, file_path):
        readings = self.perceive(file_path)
        for val in readings:
            aqi_value = self.act(val)
            print(f"{val}: {aqi_value:.2f}")

if __name__ == "__main__":
    agent = AQIModelBasedAgent()
    agent.run('sensor_data.csv')
