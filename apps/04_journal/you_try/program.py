def main():
    show_header()
    run_event_loop()


def show_header():
    print("--------------------------")
    print("--------Dagboek app--------")
    print("--------------------------")


def run_event_loop():
    print("What do you wanne do with your journal?")
    cmd = None

    while cmd != 'x':
        cmd = input("List entries, Add an entry, Exit: ")
        cmd = cmd.lower().strip()
        journal_data = []

        if cmd == 'l':
            print("L")
            list_entries(journal_data)
        elif cmd == 'a':
            print("A")
            add_entry(journal_data)
        elif cmd != 'x':
            print(f"Sorry, we don't understand {cmd}")

    print("Done, goodbye.")


def list_entries(data):
    print("Listing...")



def add_entry(data):
    print("adding...")
    text = input("Type your entry, <enter>")


if __name__ == '__main__':
    main()
