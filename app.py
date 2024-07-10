import processing
import visualize
import os

# File paths
train_path = '/Users/hmd/hmd_project/git-python/Data/ML_basic/train.csv'
test_path = '/Users/hmd/hmd_project/git-python/Data/ML_basic/test.csv'
output_path = 'images'

# Create directory for images
visualize.create_directory(output_path)

# Load data
df_train, df_test = processing.load_data(train_path, test_path)

# Display dataset info
df_train.info()

# Check index values for categorical columns
gender_counts, vehicle_age_counts, vehicle_damage_counts = processing.check_index_train(df_train)
print(gender_counts)
print(vehicle_age_counts)
print(vehicle_damage_counts)

# Check for missing data
missing_data = processing.check_null(df_train)
print(missing_data)

# Preprocess data
df_train_processed = processing.preprocess_data(df_train)

# Plot correlation heatmap and save as PNG
visualize.plot_correlation_heatmap(df_train_processed, output_path)
visualize.plot_age_distribution(df_train, output_path)
visualize.plot_age_vs_vehicle_age(df_train, output_path)
visualize.plot_gender_comparison(df_train, output_path)
visualize.plot_age_distribution_by_gender(df_train, output_path)
visualize.plot_response_counts(df_train,output_path)
visualize.plot_vehicle_damage_distribution_by_age(df_train, output_path)
#visualize.plot_relationship_region_annual_premium(df_train, output_path)
