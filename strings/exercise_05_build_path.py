parts = ["usr", "local", "bin"]

# I think I should use joint, and specify / as parameter (no separator) to join

def create_path_with(myList: list[str]) -> str:
    return f"\"{"/".join(myList)}\""

print((create_path_with(parts)))
