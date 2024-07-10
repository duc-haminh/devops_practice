import pandas as pd

def load_data(train_path, test_path):
    df_train = pd.read_csv(train_path)
    df_test = pd.read_csv(test_path)
    return df_train, df_test

def check_index_train(df_train):
    gender_counts = df_train.Gender.value_counts()
    vehicle_age_counts = df_train.Vehicle_Age.value_counts()
    vehicle_damage_counts = df_train.Vehicle_Damage.value_counts()
    return gender_counts, vehicle_age_counts, vehicle_damage_counts

def check_null(df_train):
    missing_data = df_train.isnull().sum()
    return missing_data

def preprocess_data(df):
    df_processed = pd.get_dummies(df, columns=['Gender', 'Vehicle_Age', 'Vehicle_Damage'], drop_first=True)
    return df_processed
