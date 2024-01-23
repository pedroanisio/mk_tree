# mk_tree
Streamline your project setup with this Python script
## Overview

`mk_tree` facilitates the rapid initialization of project environments through a structured, template-driven approach. It's particularly useful for developers who frequently start new projects and require a standardized or custom directory and file structure. By utilizing predefined YAML templates, the script `mk_tree.py` automates the creation of essential directories and files, tailoring the setup to specific project types such as web applications, microservices, or basic programming structures.

## Use Case

Imagine you're starting a new Flask web application. Normally, you'd spend time creating a series of directories and files that are common to such projects. This script eliminates that repetitive task. By selecting the `flask.yaml` template, the script will automatically generate the typical structure of a Flask application, including directories for templates, static files, and a basic app file. This saves time, ensures consistency, and allows you to focus immediately on writing code.

## Directory Tree Structure

The project structure is as follows:

- 📁 templates: Contains YAML files, each defining a unique project structure.
  - 📄 advanced.yaml
  - 📄 flask.yaml
  - 📄 webapp.yaml
  - 📄 flask_microservice.yaml
  - 📄 basic.yaml
- 📄 mk_tree.py: The main Python script.

## Templates and Example Structures

### Template Examples

1. **Flask Template (`flask.yaml`):**
   ```yaml
   structure:
     app.py: 
     templates:
       index.html: 
     static:
       style.css:
   ```

2. **Basic Template (`basic.yaml`):**
   ```yaml
   structure:
     README.md:
     src:
       main.py: 
   ```

### Resulting Folder Structure Example

Using the Flask template, the script will generate the following structure:

```
📁 your_project_folder
  📄 app.py
  📁 templates
    📄 index.html
  📁 static
    📄 style.css
```

## Usage

1. Run `mk_tree.py`.
2. Select a template from the list of available options.
3. Specify the base path where you want the project structure to be created.

The script then generates the directory and file structure at the specified location, based on the chosen template.

## Key Features

- **Diverse Templates:** Cater to various project types with different templates.
- **Customization Capability:** Easily add or modify templates in the `templates` directory to fit specific needs.
- **User-Friendly Interface:** Simple command-line interface for template selection and path specification.
- **Robust Error Handling:** Ensures smooth operation with checks for file/directory creation and YAML parsing.

## Requirements

- Python 3.x
- PyYAML library (Install via `pip install pyyaml`)

## Contributing

We encourage contributions to enhance the project's capabilities:

- **Template Expansion:** Add new templates for different project types.
- **Feature Improvement:** Suggest or implement new features or improvements.
- **Bug Reporting:** Report issues or bugs for prompt resolution.

Please follow standard practices for pull requests and code contributions.
