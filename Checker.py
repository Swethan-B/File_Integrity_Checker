import hashlib

def owner_name():
    name = """
    ______ _ _        _____      _                  _ _           _____ _               _             
    |  ___(_) |      |_   _|    | |                (_) |         /  __ \ |             | |            
    | |_   _| | ___    | | _ __ | |_ ___  __ _ _ __ _| |_ _   _  | /  \/ |__   ___  ___| | _____ _ __ 
    |  _| | | |/ _ \   | || '_ \| __/ _ \/ _` | '__| | __| | | | | |   | '_ \ / _ \/ __| |/ / _ \ '__|
    | |   | | |  __/  _| || | | | ||  __/ (_| | |  | | |_| |_| | | \__/\ | | |  __/ (__|   <  __/ |   
    \_|   |_|_|\___|  \___/_| |_|\__\___|\__, |_|  |_|\__|\__, |  \____/_| |_|\___|\___|_|\_\___|_|   
                                          __/ |            __/ |                                      
                                         |___/            |___/    
                                                                    by Swethan
                                                                    
    """
    print(name)

def calculate_hash(file_path):
    with open(file_path, 'rb') as f:
        # Read the file in chunks to handle large files
        chunk_size = 4096
        hasher = hashlib.sha256()
        while True:
            data = f.read(chunk_size)
            if not data:
                break
            hasher.update(data)
    return hasher.hexdigest()

def verify_integrity(file_path, stored_hash):
    
    current_hash = calculate_hash(file_path)
    if current_hash == stored_hash:
        print("File integrity verified.")
    else:
        print("File integrity check failed.")

if __name__ == "__main__":
    owner_name() # For printing the banner 
    file_path =  '# replace the file path here'  # path to the file
    stored_hash = '# replace the original sha256 hash value of the file here'   # Original hash value of the file
    verify_integrity(file_path, stored_hash)
