import numpy as np
from load_csv import load
import os
import json


class Train:
    learning_rate = 0.1

    theta0 = 0.0
    theta1 = 0.0

    temp_theta0 = 0.0
    temp_theta1 = 0.0

    average_theta0_error = 0.0
    average_theta1_error = 0.0

    data_x = np.array([])
    data_y = np.array([])

    min_x = 0
    max_x = 0
    min_y = 0
    max_y = 0

    m = 0

    iterations = 0
    iterations_done = 0

    def __init__(
        self,
        data_x: np.ndarray,
        data_y: np.ndarray,
        learning_rate: float = 0.1,
        iterations: int = 1000
    ):
        self.min_x = np.min(data_x)
        self.max_x = np.max(data_x)
        self.min_y = np.min(data_y)
        self.max_y = np.max(data_y)
        self.data_x = (data_x - self.min_x) / (self.max_x - self.min_x)
        self.data_y = (data_y - self.min_y) / (self.max_y - self.min_y)
        self.m = len(data_x)
        self.learning_rate = learning_rate
        self.iterations = iterations
        self.theta0 = 0.0
        self.theta1 = 0.0

    def predict(self, mileage):
        return self.theta0 + (self.theta1 * mileage)

    def calculate_errors(self):
        predictions = self.predict(self.data_x)
        errors = predictions - self.data_y

        self.average_theta0_error = np.sum(errors) / self.m
        self.average_theta1_error = np.sum(errors * self.data_x) / self.m

    def calculate_theta(self):
        self.temp_theta0 = self.learning_rate * self.average_theta0_error
        self.theta0 = self.theta0 - self.temp_theta0

        self.temp_theta1 = self.learning_rate * self.average_theta1_error
        self.theta1 = self.theta1 - self.temp_theta1

    def train_model(self):
        while self.iterations_done < self.iterations:
            self.calculate_errors()
            self.calculate_theta()
            self.iterations_done += 1


def train_from_data(
    data_file: str,
    output_folder_name: str,
    output_file_name: str
):
    data = load(data_file)
    if data is None:
        return
    data_x = data["km"].to_numpy()
    data_y = data["price"].to_numpy()
    model = Train(data_x, data_y, iterations=5000)

    folder_name = output_folder_name
    file_name = output_file_name

    model.train_model()

    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    data = {
        "theta0": float(model.theta0),
        "theta1": float(model.theta1),
        "max_x": int(model.max_x),
        "min_x": int(model.min_x),
        "max_y": int(model.max_y),
        "min_y": int(model.min_y),
    }

    with open(f"{folder_name}/{file_name}", "w") as file:
        file.write(json.dumps(data))


if __name__ == "__main__":
    data_file = "./intra_projects_ft_linear_regression.csv"
    output_folder_name = "adapters"
    output_file_name = "model-adapter-000000001.json"

    train_from_data(data_file, output_folder_name, output_file_name)
