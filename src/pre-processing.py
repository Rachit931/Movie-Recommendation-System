import os

import pandas as pd


def build_ratings_dataset(raw_data_path, output_file):

    # Merging whole data to required format :
    # u_i (user id), m_j (movie_id), r_ij (rating of m_j by u_i), date

    if not os.path.isfile(output_file):

        # Create a file "data.csv" before reading it
        # Read all the files in netflix and store them in one big file
        # Reading from each of the four file and combining them

        data = open(output_file, mode="w")

        row = list()

        files = [
            "combined_data_1.txt",
            "combined_data_2.txt",
            "combined_data_3.txt",
            "combined_data_4.txt",
        ]

        for file in files:

            print("Reading ratings from {}.....".format(file))

            with open(os.path.join(raw_data_path, file)) as f:

                for line in f:

                    line = line.strip()

                    if line.endswith(":"):

                        movie_id = line.replace(":", "")

                    else:

                        row = [x for x in line.split(",")]

                        row.insert(0, movie_id)

                        data.write(",".join(row))
                        data.write("\n")

        print("Done\n")

        data.close()

    else:

        print(f"{output_file} already exists. Skipping creation.")


def load_and_prepare_dataframe(data_file):
    print("Creating dataframe from data.csv......")

    df = pd.read_csv(
        data_file,
        sep=",",
        names=["movie", "user", "rating", "date"],
    )
    df.date = pd.to_datetime(df.date)
    print("Done.\n")

    # Arranging the ratings according to time(date)
    print("Sorting the dataframe by data.....")
    df.sort_values(by="date", inplace=True)
    print("Done.")

    return df


def missing_values_checking(df):
    """
    Checking Nan values in the Dataframe
    """
    nan_count = df.isnull().sum().sum()

    print("There are {} missing(Nan) values in the Dataframe...".format(nan_count))

    return df


def removing_missing_values(df):
    """
    removing data points containing missing values"""
    before = len(df)

    df = df.dropna()

    after = len(df)

    print("Removed {} data points containing Nan values".format(after - before))
    return df


def duplicate_checking(df):
    """
    Checking duplicate data points in the Dataframe
    """
    dup_bool = df.duplicated(["movie", "user", "rating"])
    dups = sum(dup_bool)

    print("There are {} duplicated entries in the data....".format(dups))

    return dup_bool


def removing_duplicates(df):
    """
    Removing duplicate data points in the Dataframe
    """
    before = len(df)

    df = df.drop_duplicates(subset=["movie", "user", "rating"])

    after = len(df)

    print("Removed {} duplicate data points".format(after - before))
    return df


def clean_dataframe(df):
    """
    Running :
    1. Check Nans
    2. Remove Nans
    3. Check duplicates
    4. Remove duplicates
    """
    missing_values_checking(df)

    removing_missing_values(df)

    duplicate_checking(df)

    removing_duplicates(df)

    return df


def splitting_data(df, train_path, test_path):
    if not os.path.isfile(train_path):
        df.iloc[: int(df.shape[0] * 0.80)].to_csv(train_path, index=False)

    if not os.path.isfile(test_path):
        df.iloc[: int(df.shape[0] * 0.80) :].to_csv(test_path, index=False)

    train_df = pd.read_csv(train_path, parse_dates=["date"])
    test_df = pd.read_csv(test_path, parse_dates=["date"])

    return train_df, test_df


if __name__ == "__main__":
    build_ratings_dataset(
        raw_data_path="data/raw",
        output_file="data/processed/data.csv",
    )

    df = load_and_prepare_dataframe(data_file="data/processed/data.csv")

    df = clean_dataframe(df)

    train_df, test_df = splitting_data(
        df,
        train_path="data/processed/train.csv",
        test_path="data/processed/test.csv",
    )
