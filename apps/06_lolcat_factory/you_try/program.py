import os


def main():
    show_header()

    folder = get_or_create_output_folder()
    print("Found or created folder: " + folder)
    # download cats
    # dispaly cats


def show_header():
    print("--------------------------------")
    print("          CAT FACTORY")
    print("--------------------------------")


def get_or_create_output_folder():
    directory = os.path.dirname(__file__)
    folder = "cat_pictures"
    full_path = os.path.join(directory, folder)

    if not os.path.exists(full_path) or not os.path.isdir(full_path):
        print(f"Creating new directory at {full_path}")
        os.mkdir(full_path)

    return full_path


if __name__ == '__main__':
    main()
