import os
from dotenv import load_dotenv

def load_env_variables():
    """
    Load environment variables from .env file.
    Returns a dictionary with the parsed values and their defaults.
    """
    # Load environment variables from .env file
    load_dotenv()
    
    # Get the input path from environment variables or set to None
    input_path = os.getenv('INPUT_PATH')
    
    # Get the output path from environment variables or set to None
    output_path = os.getenv('OUTPUT_PATH')
    
    # Get the file extensions to process
    file_extensions_str = os.getenv('FILE_EXTENSIONS')
    file_extensions = None
    if file_extensions_str:
        # Split by comma and strip whitespace, ensure each extension starts with a dot
        file_extensions = []
        for ext in file_extensions_str.split(','):
            ext = ext.strip()
            if not ext.startswith('.'):
                ext = '.' + ext
            file_extensions.append(ext.lower())
    
    # Get silent mode preference
    silent_mode_str = os.getenv('SILENT_MODE', 'false').lower()
    silent_mode = silent_mode_str in ('true', 'yes', '1', 'y')
    
    # Get organization mode
    mode = os.getenv('ORGANIZATION_MODE')
    if mode and mode.lower() in ('content', 'date', 'type'):
        mode = mode.lower()
    else:
        mode = None
    
    # Return the variables
    return {
        'input_path': input_path,
        'output_path': output_path,
        'file_extensions': file_extensions,
        'silent_mode': silent_mode,
        'mode': mode
    } 