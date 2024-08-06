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

    path = os.path.expanduser("~/hmd_project/devops_practice/Youtube_data/")
    filename = "data_thuduchospital"
    filepath = os.path.join(path, filename)
    os.makedirs(path, exist_ok=True)

    processed_data.to_csv(filepath + ".csv", index=False)
    processed_data.to_json(filepath + ".json", orient='records', lines=True)

    print(processed_data.tail())
    print()
    print("__________Complete to embedd features into Docker__________")
    print()
