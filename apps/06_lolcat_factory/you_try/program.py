import os
import platform
import subprocess

from you_try import cat_service


def main():
    show_header()

    folder = get_or_create_output_folder()
    print("Found or created folder: " + folder)
    download_cats(folder)
    display_cats(folder)


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


def download_cats(folder):
    print("Contacting server to download cats.....")
    cat_count = 8
    for i in range(1, cat_count + 1):
        name = f"lolcat_{i}"
        print(f"Downloading cat {name}")
        cat_service.get_cat(folder, name)

    print("Done")


def display_cats(folder):
    print(folder)
    print("Displaying cats in OS Window")
    if platform.system() == "Darwin":
        subprocess.call(["open", folder])
    elif platform.system() == "Windows":
        subprocess.call(["start", folder], shell=True)
    elif platform.system() == "Linux":
        subprocess.call(["xdg-open", folder])
    else:
        print(f"We don't support your os: {platform.system()}")


if __name__ == '__main__':
    main()
