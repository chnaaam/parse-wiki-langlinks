import gzip
import argparse
import pandas as pd

from tqdm import tqdm


def parse(source_file_name, destination_file_name, lang="all"):
    buffer = []
    with gzip.open(source_file_name, "r") as fp:
        for line in tqdm(fp.readlines()):
            try:
                line = line.decode()
            except:
                line = line.decode("latin1")

            if line.startswith("INSERT INTO `langlinks` VALUES ("):
                line = line.replace("INSERT INTO `langlinks` VALUES (", "")
                other_lang_links = line.split("),(")

                for other_lang_link in other_lang_links:
                    fields = other_lang_link.split(",")

                    if len(fields) == 3:
                        if lang == "all":
                            buffer.append(fields)
                        else:
                            if lang == fields[1]:
                                buffer.append(fields)
                    else:
                        if lang == "all":
                            buffer.append((fields[0], fields[1], ",".join(fields[2:])))
                        else:
                            if lang == fields[1]:
                                buffer.append((fields[0], fields[1], ",".join(fields[2:])))

    df = pd.DataFrame(buffer, columns=["page_num", "lang_type", "text"])
    df.to_csv(destination_file_name, index=False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("-s", required=True, type=str)
    parser.add_argument("-d", default="wiki_interlang.csv")
    parser.add_argument("-lang", default="all")

    args = parser.parse_args()

    parse(source_file_name=args.s, destination_file_name=args.d, lang=args.lang)