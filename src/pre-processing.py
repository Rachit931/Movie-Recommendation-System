import os
import pandas as pd
from datetime import datetime


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

    df = pd.read_csv(data_file, sep=",", names=["movie", "user", "rating", "date"])
    df.date = pd.to_datetime(df.date)
    print("Done.\n")

    # Arranging the ratings according to time(date)
    print("Sorting the dataframe by data.....")
    df.sort_values(by="date", inplace=True)
    print("Done.")


if __name__ == "__main__":
    build_ratings_dataset(
        raw_data_path="data/raw", output_file="data/processed/data.csv"
    )


if __name__ == "__main__":
    load_and_prepare_dataframe(data_file="data/processed/data.csv")
