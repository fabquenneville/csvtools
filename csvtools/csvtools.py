#!/usr/bin/env python3

# Normal import
try:
    from csvtools.library.tools import load_arguments, load_config, print_csv, print_longest, translate_csv, combine_csvs, transcode, compare_columns, test01
# Allow local import for development purposes
except ModuleNotFoundError:
    from library.tools import load_arguments, load_config, print_csv, print_longest, translate_csv, combine_csvs, transcode, compare_columns, test01


def main():
    arguments = load_arguments()
    source = arguments['source']
    sources = arguments['sources']
    destination = arguments['destination']
    if arguments['task'] == "combine":
        id = arguments['id']
        combine_csvs(sources, destination, id)
    elif arguments['task'] == "compare_columns":
        compare_columns(source, destination)
    elif arguments['task'] == "print":
        print_csv(source)
    elif arguments['task'] == "print_longest" and source:
        print_longest(source)
    elif arguments['task'] == "transcode":
        transcode(source, destination)
    elif arguments['task'] == "translate":
        translate_csv()
    elif arguments['task'] == "test":
        test01(source, destination)


if __name__ == '__main__':
    main()
