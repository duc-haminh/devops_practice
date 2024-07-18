import processing
import visualize
import os
from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

# Using environment variables for file paths (set in Dockerfile or local environment)
train_path = os.environ.get('TRAIN_PATH')
test_path = os.environ.get('TEST_PATH')
output_path = os.environ.get('OUTPUT_PATH')

# Create directory for images
visualize.create_directory(output_path)

# Load data
df_train, df_test = processing.load_data(train_path, test_path)

# Store print outputs in a list
output_logs = []

# Capture print output in a custom function
def log_output(output):
    output_logs.append(output)

# Display dataset info
info = df_train.info(buf=None)
log_output(info)

# Check index values for categorical columns
gender_counts, vehicle_age_counts, vehicle_damage_counts = processing.check_index_train(df_train)
log_output(gender_counts)
log_output(vehicle_age_counts)
log_output(vehicle_damage_counts)

# Check for missing data
missing_data = processing.check_null(df_train)
log_output(missing_data)

# Preprocess data
df_train_processed = processing.preprocess_data(df_train)

# Plot correlation heatmap and save as PNG
visualize.plot_correlation_heatmap(df_train_processed, output_path)
visualize.plot_age_distribution(df_train, output_path)
visualize.plot_age_vs_vehicle_age(df_train, output_path)
visualize.plot_gender_comparison(df_train, output_path)
visualize.plot_age_distribution_by_gender(df_train, output_path)
visualize.plot_response_counts(df_train, output_path)
visualize.plot_vehicle_damage_distribution_by_age(df_train, output_path)

@app.route('/')
def index():
    images = sorted(os.listdir(output_path))  # Sort the list of images
    return render_template('index.html', images=images, logs=output_logs)

@app.route("/images/<filename>", methods=["GET"])
def serve_image(filename):
    return send_from_directory(output_path, filename)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
