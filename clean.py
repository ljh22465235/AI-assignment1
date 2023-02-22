import pandas as pd


def clean(input_file1, input_file2):
    rc = pd.read_csv(input_file1)
    ro = pd.read_csv(input_file2)
    merge1 = pd.merge(rc, ro, left_on='respondent_id', right_on='id').drop('id', axis=1)
    merge1 = merge1.dropna()
    merge1 = merge1[merge1['job'].str.contains('insurance', na=False)]
    merge1 = merge1[merge1['job'].str.contains('Insurance', na=False)]
    return merge1


if __name__ == '__main__':

    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('contact_info_file', help='The path to the respondent_contact.csv file')
    parser.add_argument('other_info_file', help='The path to the respondent_other.csv file')
    parser.add_argument('output_file', help='The path to the output file')
    args = parser.parse_args()

    cleaned = clean(args.contact_info_file, args.other_info_file)
    cleaned.to_csv(args.output_file, index=False)
    print('The shape of the cleaned file is: ', cleaned.shape)