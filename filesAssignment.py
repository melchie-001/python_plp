def process_file():
    filename = input("Enter the filename to read: ")

    try:
        with open(filename, "r") as infile:
            content = infile.read()
            modified = content.upper()
            word_count = len(content.split())

        with open("modified_output.txt", "w") as outfile:
            outfile.write("MODIFIED CONTENT:\n\n")
            outfile.write(modified)
            outfile.write(f"\n\nWord Count: {word_count}\n")

        print("✅ File processed successfully! Check 'modified_output.txt'.")

    except FileNotFoundError:
        print(f"❌ Error: The file '{filename}' does not exist.")
    except IOError:
        print(f"⚠️ Error: Could not read the file '{filename}'.")
    except Exception as e:
        print(f"🚨 Unexpected error: {e}")

process_file()
