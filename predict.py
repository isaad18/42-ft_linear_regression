import json


class Predict:

    theta0 = 0.0
    theta1 = 0.0

    min_x = 0
    max_x = 0

    min_y = 0
    max_y = 0

    def __init__(self, data_file):
        data: dict

        with open(data_file, "r") as file:
            data = json.loads(file.read())

        self.theta0 = float(data["theta0"])
        self.theta1 = float(data["theta1"])

        self.min_x = int(data["min_x"])
        self.max_x = int(data["max_x"])

        self.min_y = int(data["min_y"])
        self.max_y = int(data["max_y"])

    def predict(self, mileage):
        return self.theta0 + (self.theta1 * mileage)

    def predict_real(self, mileage):
        normalized_mileage = (mileage - self.min_x) / (self.max_x - self.min_x)
        normalized_prediction = self.predict(normalized_mileage)
        return normalized_prediction * (self.max_y - self.min_y) + self.min_y


def predict_price(data_file: str):
    try:
        model = Predict(data_file)
    except (FileNotFoundError, FileExistsError):
        print("Error: File not found.")
        return
    km = input("km: ")

    try:
        float_km = int(km)
    except ValueError:
        print("ValueError: Value must be an integer.")
        return

    print(model.predict_real(float_km))


if __name__ == "__main__":
    folder_name = "adapters"
    file_name = "model-adapter-000000001.json"
    predict_price(f"{folder_name}/{file_name}")
