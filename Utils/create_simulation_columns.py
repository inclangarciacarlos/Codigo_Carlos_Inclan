import os


def extract_folder_names(folder_path):
    """
    Extracts the names of folders in the given directory.

    Args:
        folder_path (str): Path to the directory containing folders.

    Returns:
        list: List of folder names.
    """
    items = os.listdir(folder_path)
    folders = [item for item in items if os.path.isdir(os.path.join(folder_path, item))]
    return folders


def extract_cd_cl_from_folder_name(folder_path, folder_name):
    """
    Extracts the Cd and Cl values from the folder name.

    Args:
        folder_path (str): Path to the directory containing the folder.
        folder_name (str): Name of the folder.

    Returns:
        tuple: Cd and Cl values as floats.
    """
    cd_file = \
    [f for f in os.listdir(os.path.join(folder_path, folder_name)) if f.startswith('cd') and f.endswith('.txt')][0]
    cl_file = \
    [f for f in os.listdir(os.path.join(folder_path, folder_name)) if f.startswith('cl') and f.endswith('.txt')][0]

    # read all the lines in the cd file and extract the second float value in the last line
    with open(os.path.join(folder_path, folder_name, cd_file), 'r', encoding="utf-8") as f:
        lines = f.readlines()
        cd_value = float(lines[-1].split()[1])

    # read all the lines in the cl file and extract the second float value in the last line
    with open(os.path.join(folder_path, folder_name, cl_file), 'r', encoding="utf-8") as f:
        lines = f.readlines()
        cl_value = float(lines[-1].split()[1])
    return cd_value, cl_value


def create_simulation_columns(folder_path):
    """
    Creates simulation columns from the folder names in the given directory.

    Args:
        folder_path (str): Path to the directory containing folders.

    Returns:
        list: Two arrays containing Cd and Cl values for each folder.
    """
    folder_names = extract_folder_names(folder_path)
    cd_values = []
    cl_values = []
    for folder_name in folder_names:
        cl_value, cd_value = extract_cd_cl_from_folder_name(folder_path, folder_name)
        cl_values.append(cl_value)
        cd_values.append(cd_value)
    return cd_values, cl_values