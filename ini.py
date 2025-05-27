import heaan_stat
# Initialize HEAAN context
# This code initializes the HEAAN context for encryption and decryption of data.
# This is typically done once at the start of your application.
context = heaan_stat.Context(
            key_dir_path='./keys',
            generate_keys=True,  # To use existing keys, set it to False or omit this
        )