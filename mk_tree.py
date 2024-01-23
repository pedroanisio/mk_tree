import os
import yaml
import pathlib

def list_templates(template_dir: str) -> dict:
    """
    List all YAML templates in a specified directory and their manifests.

    Args:
    template_dir (str): The directory containing YAML templates.

    Returns:
    dict: A dictionary of template names and their file paths.
    """
    templates = {}
    for filename in os.listdir(template_dir):
        if filename.endswith('.yaml') or filename.endswith('.yml'):
            full_path = os.path.join(template_dir, filename)
            with open(full_path, 'r') as file:
                try:
                    data = yaml.safe_load(file)
                    manifest = data.get('manifest', {})
                    template_name = manifest.get('name', 'Unnamed Template')
                    templates[template_name] = full_path
                except yaml.YAMLError as exc:
                    print(f"Error reading {filename}: {exc}")
    return templates

def create_files_and_folders(parent_path: str, structure: dict) -> None:
    """
    Recursively create files and folders from a structure dictionary.

    Args:
    parent_path (str): The path to the parent directory.
    structure (dict): The project structure dictionary.
    """
    if not isinstance(structure, dict):
        print(f"Invalid structure format at {parent_path}. Expected a dict, got {type(structure)}.")
        return

    for name, content in structure.items():
        path = os.path.join(parent_path, name)
        if content is None or isinstance(content, str):  # It's a file
            try:
                open(path, 'a').close()
            except IOError as e:
                print(f"Failed to create file {path}: {e}")
        else:  # It's a directory
            try:
                os.makedirs(path, exist_ok=True)
                create_files_and_folders(path, content)
            except OSError as e:
                print(f"Failed to create directory {path}: {e}")


def get_user_input(templates: dict) -> (str, str):
    """
    Get user input for choosing a template and specifying the base path.

    Args:
    templates (dict): A dictionary of templates and their file paths.

    Returns:
    tuple: Contains the path to the chosen template file and the base path for the project.
    """
    print("Available templates:")
    for idx, name in enumerate(templates, start=1):
        print(f"{idx}) {name}")
    choice = input("Choose a template by number: ")
    chosen_template = list(templates.values())[int(choice) - 1]

    base_project_path = input("Enter the base path for the project: ")
    return chosen_template, base_project_path

def create_directory_structure_from_yaml(yaml_path: str, base_path: str) -> None:
    """
    Create a directory structure based on a YAML template.

    Args:
    yaml_path (str): Path to the YAML template file.
    base_path (str): The root directory where the project structure will be created.
    """
    try:
        with open(yaml_path, 'r') as file:
            data = yaml.safe_load(file)
            structure = data.get('structure')  # Extracting the 'structure' part
            if not structure:
                print(f"No 'structure' key found in {yaml_path}.")
                return
    except FileNotFoundError:
        print(f"YAML file not found at {yaml_path}.")
        return
    except yaml.YAMLError as exc:
        print(f"Error in YAML file: {exc}")
        return

    create_files_and_folders(base_path, structure)


# Main execution
if __name__ == "__main__":
    template_dir = "templates"
    available_templates = list_templates(template_dir)
    yaml_path, base_path = get_user_input(available_templates)
    create_directory_structure_from_yaml(yaml_path, base_path)
