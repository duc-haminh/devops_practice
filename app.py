import os
from scrape_data import scrape_data
from processing import process_data

if __name__ == "__main__":
    urls = []
    for i in range(1, 10):
        url = 'http://www.benhvienkhuvucthuduc.vn/hoi-dap/?p=' + str(i)
        urls.append(url)

    data = scrape_data(urls)

    processed_data = process_data(data)

    path = "/Users/hmd/hmd_project/Youtube_data/"
    filename = "data_thuduchospital"
    filepath = path + filename
    directory = os.path.dirname(filepath)
    os.makedirs(directory, exist_ok=True)

    processed_data.to_csv(filepath + ".csv", index=False)
    processed_data.to_json(filepath + ".json", orient='records', lines=True)

    print(processed_data.head())
    print()
    print("__________Complete to embedd features into Docker__________")
    print()