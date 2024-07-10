import matplotlib.pyplot as plt
import seaborn as sns
import os

def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def plot_correlation_heatmap(df, output_path):
    title = "Correlatio matrix of dataset"
    fig, ax = plt.subplots(figsize=(10, 10))
    ax = sns.heatmap(df.corr(), linewidths=0.1, square=True, annot=True)
    plt.savefig(os.path.join(output_path, "1." + title + ".png"))
    plt.close()

def plot_age_distribution(df, output_path):
    title = 'Normal distribution of Age'
    fig, ax = plt.subplots(figsize=(12,5))
    ax = sns.distplot(df.Age)
    ax.set_title(title, fontsize=20)
    plt.savefig(os.path.join(output_path, "2." + title + ".png"))
    plt.close()


def plot_age_vs_vehicle_age(df, output_path):
    title = 'Age vs Vehicle Age Boxplot'
    fig, ax = plt.subplots(figsize=(12, 5))
    sns.boxplot(y='Age', x='Vehicle_Age', hue='Previously_Insured', data=df, ax=ax)
    ax.set_title(title, fontsize=20)
    plt.savefig(os.path.join(output_path, "3." + title + ".png"))
    plt.close()

def plot_gender_comparison(df, output_path):
    title = 'Gender Comparison'
    fig, ax = plt.subplots(figsize=(8, 6))
    ax = sns.countplot(x="Gender", data=df, palette="plasma")

    # Add annotations to each bar
    for p in ax.patches:
        ax.annotate(f'\n{p.get_height()}', (p.get_x()+0.4, p.get_height()), ha='center', va='top', color='white', size=12)

    ax.set_title(title, fontsize=20)
    plt.savefig(os.path.join(output_path, "4." + title + ".png"))
    plt.close()

def plot_age_distribution_by_gender(df, output_path):
    title = 'Comparison of Age Distribution by Gender'
    fig_dims = (30, 15)  # Adjust the figure size as needed
    fig, ax = plt.subplots(figsize=fig_dims)
    ax.set_title(title, fontsize=50)
    sns.countplot(x='Age', hue='Gender', data=df, ax=ax)

    plt.savefig(os.path.join(output_path, "5." + title + ".png"))
    plt.close()    

def plot_response_counts(df, output_path):
    title = 'Number of Responses in Dataset'
    fig, ax = plt.subplots(figsize=(8, 6))
    ax = sns.countplot(x="Response", data=df, palette="plasma")
    
    # Add annotations to each bar
    for p in ax.patches:
        ax.annotate(f'\n{p.get_height()}', (p.get_x()+0.4, p.get_height()), ha='center', va='top', color='white', size=12)

    ax.set_title(title, fontsize=12)
    plt.savefig(os.path.join(output_path, "6." + title + ".png"))
    plt.close()

def plot_vehicle_damage_distribution_by_age(df, output_path):
    title = 'Normal distribution of Vehicle Damage by Age'
    x = df.groupby(["Age", "Vehicle_Damage"])
    x = x["id"].count().to_frame()
    x = x.rename(columns={"id": "count"}).reset_index()
    y = x.loc[x["Age"] < 36]

    fig_dims = (12, 8)
    fig, ax = plt.subplots(figsize=fig_dims)
    sns.barplot(x="Age", y="count", hue="Vehicle_Damage", data=y, ax=ax)

    ax.set_title(title, fontsize=14)
    ax.set_xlabel('Age')
    ax.set_ylabel('Count')

    plt.savefig(os.path.join(output_path, "7." + title + ".png"))
    plt.close()

"""def plot_relationship_region_annual_premium(df, output_path):
    title = 'Relationship between Region and Annual Premium'
    fig, ax = plt.subplots(figsize=(12, 5))
    sns.pairplot(hue='Response', data=df)
    ax.set_title(title, fontsize=20)
    plt.savefig(os.path.join(output_path, "8." + title + ".png"))
    plt.close()"""