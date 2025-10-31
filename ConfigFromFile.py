import os

def fix_working_directory():
    current_working_directory = os.getcwd()
    while "test" in current_working_directory or "src" in current_working_directory:
        os.chdir("/")
        current_working_directory = os.getcwd()

def get_config():
    fix_working_directory()
    print(os.getcwd())
    config_path = "resource/properties.cfg"
    property_file = open(config_path, "r")
    property_data = property_file.read().splitlines()
    property_file.close()
    return property_data
