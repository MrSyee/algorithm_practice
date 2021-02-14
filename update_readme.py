import os
import pandas as pd


def get_algo_list():
    # Get python filename list
    filelist = list()
    for (dirpath, dirnames, filenames) in os.walk("."):
        for file in filenames:
            if ".py" in file and "unlisted" not in dirpath and file != "update_readme.py":
                filelist += [os.path.join(dirpath, file)]

    # Get algorithms list from filepaths
    algo_list = []
    for filepath in filelist:
        with open(filepath, "r") as f:
            opend_file = f.readlines()

            line1 = opend_file[1]
            title = line1.split(". ")[1].split(" (")[0]
            category = filepath.split("/")[1]
            leetcode_link = opend_file[2][:-2]
            answer_link = "https://github.com/MrSyee/algorithm_practice/blob/master/" + filepath[2:]
            algo_list.append(
                dict(
                    name=title,
                    category=category,
                    leetcode=leetcode_link,
                    answer=answer_link,
                )
            )

    return algo_list


def update_markdown(data_list):
    new_line = ""
    for data_dict in data_list:
        new_line += (
            f"|{data_dict['idx']}    "
            + f"|{data_dict['name']}  "
            + f"|{data_dict['category']}    "
            + f"|[LeetCode]({data_dict['leetcode']})  "
            + f"|[Ans]({data_dict['answer']})  "
            + f"|    |\n"
        )
    with open("./README.md", "r") as f:
        doc = f.read()
        doc += f"{new_line}"
    with open("./README.md", "w") as f:
        f.write(doc)


if __name__ == "__main__":
    csv_path = "./algo_list.csv"

    curr_algo_list = get_algo_list()
    prev_algo_df = pd.read_csv(csv_path, index_col=0)

    # Find new item
    new_list = []
    for algo in curr_algo_list:
        if (prev_algo_df["name"] != algo["name"]).all():
            new_list.append(algo)

    # Update csv
    if new_list:
        curr_algo_df = prev_algo_df.copy()
        idx = len(curr_algo_df.index)

        for new_row in new_list:
            new_row["idx"] = idx
            idx += 1

            curr_algo_df = curr_algo_df.append(new_row, ignore_index=True)
        curr_algo_df.to_csv(csv_path)

        update_markdown(new_list)
