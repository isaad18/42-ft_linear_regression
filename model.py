from train import train_from_data
from predict import predict_price


def main():
    data_file = "./intra_projects_ft_linear_regression.csv"
    folder_name = "adapters"
    file_name = "model-adapter-000000001.json"

    train_from_data(data_file, folder_name, file_name)
    predict_price(f"{folder_name}/{file_name}")


if __name__ == "__main__":
    main()
