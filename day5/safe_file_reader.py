# safe_reader.py
def read_file_safely(filename):
    try:
        with open(filename, "r") as f:
            data = f.read()
            print("File content:\n", data)
    except FileNotFoundError:
        print(f"❌ File '{filename}' not found!")
    except Exception as e:
        print("Unknown error:", e)
    finally:
        print("Attempted to read the file.")

read_file_safely("missing.txt")